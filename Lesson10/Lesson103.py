class Platba:
    def zaplat(self, suma):
        raise NotImplementedError("Subclasses must implement the zaplat method")

class Kreditna_Karta(Platba):
    def zaplat(self, suma):
        print(f"Zaplatil si {suma} eur kreditnou kartou.")

class PayPal(Platba):
    def zaplat(self, suma):
        print(f"Zaplatil si {suma} eur cez PayPal.")


class Hotovost(Platba):
    def zaplat(self, suma):
        print(f"Zaplatil si {suma} v hotovosti.")


if __name__ == "__main__":
    suma = 50

    kreditna_karta = Kreditna_Karta()
    kreditna_karta.zaplat(suma)

    paypal = PayPal()
    paypal.zaplat(suma)

    hotovost = Hotovost()
    hotovost.zaplat(suma)

