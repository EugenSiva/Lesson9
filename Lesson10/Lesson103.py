class Platba:
    def zaplat(self):
        raise NotImplementedError("Subclasses must implement the zaplat method")

class Kreditna_Karta(Platba):
    def zaplat(self):
        return print("Zaplatil si 50 kreditnou kartou.")

class PayPal(Platba):
    def zaplat(self):
        return print("Zaplatil si 50 cez PayPal.")


class Hotovost(Platba):
    def zaplat(self):
        return print("Zaplatil si 50 v hotovosti.")