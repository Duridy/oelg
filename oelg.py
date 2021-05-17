kolvo = int(input())
class Oelg:

    heal = 100
    name = "Oleg"
    smoke = 5

    def __init__(self, heal):
        self.heal = self.heal + self.smoke * kolvo
    def stat(self):
        print("Здоровье стало =", str(self.heal) + '.' " Имя -", str(self.name) + '.' " Кол-во скуренных сигарет -", self.smoke)
        
oelg = Oelg(kolvo)
oelg.stat()
