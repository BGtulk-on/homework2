class Slujitel:
    def __init__(self, ime, slujeben_nomer):
        self._ime = ime
        self.slujeben_nomer = slujeben_nomer
        self.zaplati = []

    def dobavi_zaplata(self, zaplata):
        if self.proverka_zaplata(zaplata):
            self.zaplati.append(zaplata)
        else:
            raise ValueError("Невалидна заплата")

    def sredna_zaplata(self):
        if not self.zaplati:
            return 0
        return sum(self.zaplati) / len(self.zaplati)

    @staticmethod
    def proverka_zaplata(zaplata):
        return 1200 <= zaplata <= 4000

    @classmethod
    def ot_niz(cls, niz):
        ime, slujeben_nomer = niz.split(", ")
        return cls(ime, slujeben_nomer)

    @property
    def ime(self):
        return self._ime

    @ime.setter
    def ime(self, novo_ime):
        if all(x.isalpha() or x.isspace() for x in novo_ime):
            self._ime = novo_ime
        else:
            raise ValueError("Невалидно име")


slujitel = Slujitel("Иван Желязков", "12345")
slujitel.dobavi_zaplata(1500)
slujitel.dobavi_zaplata(2000)
print(slujitel.sredna_zaplata())
print(f"Средната заплата на {slujitel.ime} е {slujitel.sredna_zaplata()}")
slujitel.ime = "Преслав Колев"
print(slujitel.ime)
new_slujitel = slujitel.ot_niz("Йоан Козарев, 67890")
print(new_slujitel.ime)