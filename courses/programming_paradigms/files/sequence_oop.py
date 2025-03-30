import unittest
from typing import Self

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


class Seq:
    def __init__(self, name: str, seq: str, qual: None | list[int] = None):
        self._name = name
        self._seq = seq
        self._qual = qual
        if qual is not None and len(seq) != len(qual):
            raise ValueError("Length of sequence and quality do not match")

    @property
    def name(self) -> str:
        return self._name

    @property
    def seq(self) -> str:
        return self._seq

    @property
    def qual(self) -> None | list[int]:
        return self._qual

    def __len__(self) -> int:
        return len(self._seq)

    def to_fastq(self) -> str:
        if self._qual is None:
            raise RuntimeError("Quality scores are not available")
        else:
            return f"@{self._name}\n{self._seq}\n+\n{''.join(chr(q + 33) for q in self._qual)}\n"

    def to_fasta(self) -> str:
        return f">{self._name}\n{self._seq}\n"

    def reverse(self) -> Self:
        seq = "".join([COMPLEMENT_NUCL[nucleotide] for nucleotide in self.seq[::-1]])
        return Seq(
            f"{self.name}_rev",
            seq,
            self.qual[::-1] if self._qual is not None else None,
        )


class SequenceTest(unittest.TestCase):
    def test_seq_creation(self):
        seq = Seq("seq1", "ATGC")
        assert seq.name == "seq1"
        assert seq.seq == "ATGC"
        assert seq.qual is None

        seq = Seq("seq2", "ATGC", [10, 20, 30, 40])
        assert seq.name == "seq2"
        assert seq.seq == "ATGC"
        assert seq.qual == [10, 20, 30, 40]

        try:
            Seq("seq3", "ATGC", [10, 20, 30])
            self.failed("Should have raised a ValueError")
        except ValueError:
            pass
        try:
            Seq("ATGC")
            self.failed("Should have raised a TypeError")
        except TypeError:
            pass

    def test_seq_len(self):
        seq = Seq("seq1", "ATGC")
        assert len(seq) == 4

        seq = Seq("seq2", "ATGC", [10, 20, 30, 40])
        assert len(seq) == 4

    def test_to_fastq(self):
        seq = Seq("seq1", "ATGC")
        try:
            assert seq.to_fastq()
            self.fail("Should have raised a RuntimeError")
        except RuntimeError:
            pass

        seq = Seq("seq2", "ATGC", [10, 20, 30, 40])
        assert seq.to_fastq() == "@seq2\nATGC\n+\n+5?I\n"

    def test_to_fasta(self):
        seq = Seq("seq1", "ATGC")
        assert seq.to_fasta() == ">seq1\nATGC\n"
        seq = Seq("seq2", "ATGC", [10, 20, 30, 40])
        assert seq.to_fasta() == ">seq2\nATGC\n"

    def test_reverse(self):
        seq = Seq("seq1", "aTGC")
        seq = seq.reverse()
        assert seq.name == "seq1_rev"
        assert seq.seq == "GCAt"

        seq = Seq("seq2", "ATGC", [10, 20, 30, 40])
        seq = seq.reverse()
        assert seq.seq == "GCAT"
        assert seq.qual == [40, 30, 20, 10]


if __name__ == "__main__":
    unittest.main()
