class Prvok:
    def __init__(self, data):
        self.data = data
        self.dalsi_prvok = None
class LinkedList:
    def __init__(self):
        self.head = None
    def vloz(self, data):
        novy_prvok = Prvok(data)
        if not self.head:
            self.head = novy_prvok
        else:
            aktualny = self.head
            while aktualny.dalsi_prvok:
                aktualny = aktualny.dalsi_prvok
            aktualny.dalsi_prvok = novy_prvok

    def vypis(self):
        aktualny = self.head
        while aktualny:
            print(aktualny.data)
            aktualny = aktualny.dalsi_prvok
        print("None!")

zoznam = LinkedList()
zoznam.vloz(1)
zoznam.vloz(2)
zoznam.vloz(3)
zoznam.vloz(4)
zoznam.vloz(5)
zoznam.vloz(6)
zoznam.vypis()


