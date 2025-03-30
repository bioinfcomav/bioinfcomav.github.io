import unittest

COMPLEMENT_NUCL = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C",
    "N": "N",
    "Y": "R",
    "R": "Y",
    "S": "S",
    "W": "W",
    "K": "M",
    "M": "K",
    "B": "V",
    "V": "B",
    "D": "H",
    "H": "D",
}
COMPLEMENT_NUCL.update(
    {nucl.lower(): rev_nucl.lower() for nucl, rev_nucl in COMPLEMENT_NUCL.items()}
)


def calc_len(seq):
    if len(seq) == 3:
        if len(seq[1]) != len(seq[2]):
            raise ValueError("Sequence and quality length differ")
    return len(seq[1])


def to_fastq(seq):
    if len(seq) == 2:
        raise RuntimeError("Quality not provided")
    return f"@{seq[0]}\n{seq[1]}\n+\n{''.join(chr(q + 33) for q in seq[2])}\n"


def to_fasta(seq):
    return f">{seq[0]}\n{seq[1]}\n"


def reverse(seq):
    name = f"{seq[0]}_rev"
    seq_ = "".join([COMPLEMENT_NUCL[nucleotide] for nucleotide in seq[1][::-1]])
    if len(seq) == 2:
        return (name, seq_)
    elif len(seq) == 3:
        seq = (name, seq_, seq[2][::-1])
    return seq


class SequenceTest(unittest.TestCase):
    def test_seq_len(self):
        seq = ("seq1", "ATGC")
        assert calc_len(seq) == 4

        seq = ("seq2", "ATGC", [10, 20, 30, 40])
        assert calc_len(seq) == 4

        seq = ("seq2", "ATGC", [10, 20, 30])
        try:
            assert calc_len(seq) == 4
            self.fail("Should have raised a ValueError")
        except ValueError:
            pass

    def test_to_fastq(self):
        seq = ("seq1", "ATGC")
        try:
            assert to_fastq(seq)
            self.fail("Should have raised a RuntimeError")
        except RuntimeError:
            pass

        seq = ("seq2", "ATGC", [10, 20, 30, 40])
        assert to_fastq(seq) == "@seq2\nATGC\n+\n+5?I\n"

    def test_to_fasta(self):
        seq = ("seq1", "ATGC")
        assert to_fasta(seq) == ">seq1\nATGC\n"
        seq = ("seq2", "ATGC", [10, 20, 30, 40])
        assert to_fasta(seq) == ">seq2\nATGC\n"

    def test_reverse(self):
        seq = ("seq1", "aTGC")
        seq = reverse(seq)
        assert seq[0] == "seq1_rev"
        assert seq[1] == "GCAt"

        seq = ("seq2", "ATGC", [10, 20, 30, 40])
        seq = reverse(seq)
        assert seq[1] == "GCAT"
        assert seq[2] == [40, 30, 20, 10]


if __name__ == "__main__":
    unittest.main()
