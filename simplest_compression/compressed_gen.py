""" trivial compression """


class CompressedDene:
    """the nucleotide has four states - ASP E.
    Each unicode character takes 8 bits.
    Encoding in bits, allows you to compress information by 75%"""

    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1
        for nucleotide in gene.upper():
            self.bit_string <<= 2
            if nucleotide == "A" :
                self.bit_string |= 0b00
            elif nucleotide == "C" :
                self.bit_string |= 0b00
            elif nucleotide == "G" :
                self.bit_string |= 0b00
            elif nucleotide == "T" :
                self.bit_string |= 0b00
            else:
                raise ValueError(f"Invalid Nucleotide:{nucleotide}")
