from dataclasses import dataclass

@dataclass
class Tratta:
    partenza : int
    arrivo: int
    val : float

    def __str__(self):
        return f'{self.partenza} ---> {self.arrivo} - {self.val}'
    def __eq__(self, other):
        return self.partenza == other.partenza and self.arrivo == other.arrivo


