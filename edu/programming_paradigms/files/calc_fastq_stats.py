import sys
import gzip
from pathlib import Path
from collections import namedtuple, defaultdict
import json
import io
import unittest

Seq = namedtuple("Seq", ["seq", "quals"])


def is_gzipped(fastq_fhand):
    magic = fastq_fhand.peek(2)[:2]
    return magic == b"\x1f\x8b"


def parse_fastq(fhand):
    if not isinstance(fhand, io.BufferedReader):
        fhand = io.BufferedReader(fhand)

    if is_gzipped(fhand):
        fhand = gzip.open(fhand, "rb")

    while True:
        name = fhand.readline()
        if not name:
            break
        seq = fhand.readline().strip().lower()
        plus = fhand.readline().strip()
        assert plus == b"+"
        quals = list(map(lambda x: x - 33, fhand.readline().strip()))
        yield Seq(seq, quals)


def calc_fastq_stats(fastq_fhand, out_stats_fhand):
    num_seqs = 0
    seq_len_distrib = defaultdict(int)
    gc_distrib = defaultdict(int)
    mean_qual_distrib = defaultdict(int)
    for seq in parse_fastq(fastq_fhand):
        gc = round((seq.seq.count(b"c") + seq.seq.count(b"g")) / len(seq.seq) * 100)
        mean_qual = round(sum(seq.quals) / len(seq.quals))
        num_seqs += 1
        seq_len_distrib[len(seq.seq)] += 1
        gc_distrib[gc] += 1
        mean_qual_distrib[mean_qual] += 1

    stats = {
        "num_seqs": num_seqs,
        "seq_len_distrib": dict(seq_len_distrib),
        "gc_distrib": dict(gc_distrib),
        "mean_qual_distrib": dict(mean_qual_distrib),
    }

    json.dump(stats, out_stats_fhand, indent=4)
    out_stats_fhand.flush()


class TestFastqStats(unittest.TestCase):
    def test_calc_fastq_stats(self):
        fastq = b"@seq1\nATGC\n+\nIIII\n"
        fastq_fhand = io.BytesIO(fastq)
        out_stats_fhand = io.StringIO()
        calc_fastq_stats(fastq_fhand, out_stats_fhand)
        out_stats = json.loads(out_stats_fhand.getvalue())
        self.assertEqual(out_stats["num_seqs"], 1)
        self.assertEqual(out_stats["seq_len_distrib"], {"4": 1})
        self.assertEqual(out_stats["gc_distrib"], {"50": 1})
        self.assertEqual(out_stats["mean_qual_distrib"], {"40": 1})


if __name__ == "__main__":
    # unittest.main()

    if len(sys.argv) != 2:
        print("Usage: python calc_fastq_stats.py <fastq_file>")
        sys.exit(1)
    fpath = sys.argv[1]
    if fpath == "-":
        fastq_fhand = sys.stdin.buffer
    else:
        fpath = Path(fpath)
        if not fpath.exists():
            print(f"File {fpath} does not exist")
            sys.exit(1)
        fastq_fhand = open(fpath, "rb")
    fastq_fhand = io.BufferedReader(fastq_fhand)

    output_stats_path = Path("fastq_stats.json")
    with open(output_stats_path, "w") as out_stats_fhand:
        calc_fastq_stats(fastq_fhand, out_stats_fhand)
