import sys
from pathlib import Path
import gzip
from collections import Counter
import json
import unittest
import io


def is_gzipped(fastq_fhand):
    magic = fastq_fhand.peek(2)[:2]
    return magic == b"\x1f\x8b"


def parse_fastq(fhand):
    while True:
        name = fhand.readline()
        if not name:
            break
        seq = fhand.readline().strip().upper()
        plus = fhand.readline().strip()
        assert plus == b"+"
        fhand.readline()
        yield seq


def create_kmers_for_seq(seq, kmer_len):
    for i in range(len(seq) - kmer_len + 1):
        yield seq[i : i + kmer_len]


def count_kmers(fastq_fhand, kmers_fhand, kmers_distrib_fhand, kmer_len):
    if not isinstance(fastq_fhand, io.BufferedReader):
        fastq_fhand = io.BufferedReader(fastq_fhand)

    if is_gzipped(fastq_fhand):
        fastq_fhand = gzip.open(fastq_fhand, "rb")

    # Count kmers
    counts = Counter()
    for seq in parse_fastq(fastq_fhand):
        counts.update(create_kmers_for_seq(seq, kmer_len))

    # Write down the kmers
    for kmer, count in counts.most_common():
        if count < 2:
            break
        kmers_fhand.write(f"{kmer.decode()}\t{count}\n")
    kmers_fhand.flush()

    # Create the kmer distribution
    kmer_distrib = Counter(counts.values())

    json.dump(kmer_distrib, kmers_distrib_fhand, indent=4)
    kmers_distrib_fhand.flush()


class TestKmerCounting(unittest.TestCase):
    def test_kmer_counting(self):
        fhand = io.BytesIO(
            b"@seq1\nACTGGATCTTGCC\n+\nIIIIIIIIIII\n@seq2\nACTGGATATGCG\n+\nIIIIIIIIIIII\n@seq3\nTTCATGC\n+\nIIIIIII\n"
        )
        kmers_fhand = io.StringIO()
        stats_fhand = io.StringIO()
        count_kmers(fhand, kmers_fhand, stats_fhand, 5)
        assert kmers_fhand.getvalue() == "ACTGG\t2\nCTGGA\t2\nTGGAT\t2\n"

        assert json.loads(stats_fhand.getvalue()) == {"2": 3, "1": 14}


if __name__ == "__main__":
    # unittest.main()

    if len(sys.argv) != 3:
        print("Usage: python count_kmers.py <fastq_file> <kmer_len>")
        sys.exit(1)
    fastq_path = Path(sys.argv[1])
    if fastq_path == "-":
        fastq_fhand = sys.stdin.buffer
    else:
        fastq_fhand = fastq_path.open("rb")
    kmer_len = int(sys.argv[2])
    kmers_distrib_path = Path("kmers_distrib.json")
    kmers_distrib_fhand = kmers_distrib_path.open("wt")
    kmers_path = Path("kmers.txt")
    kmers_fhand = kmers_path.open("wt")
    count_kmers(fastq_fhand, kmers_fhand, kmers_distrib_fhand, kmer_len)
