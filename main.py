# class Isuzi:
    
#     def __init__(self):
#         self.dvigatel = Dvigatel()
#         self.boshqarish = Boshqarish()
#         self.tormozlar = Tormozlar()
#         self.kotarish = Kotarish()
#         self.havo_boshqargich = Havo_boshqargich()
#         self.
#         self.fuel_efficiency = 0
#         self.safety_rating = 0

#         def tezlanish(self):
#             self.dvigatel.tezlashtirish()

#         def tormoz(self):
#             self.tormozlar.tormoz_pedalini_bosmoq()

#         def burilish(self, yonalish):
#             self.boshqarish.burilish(yonalish)

#         def set_fuel_efficiency(self, efficiency):
#             self.fuel_efficiency = efficiency

#         def set_safety_rating(self, rating):
#             self.safety_rating = rating

#     class Dvigatel:
#         def __init__(self):
#             self.rpm = 0

#         def tezlashtirish(self):
#             self.rpm += 10

#     class Boshqarish:
#         def __init__(self):
#             self.rul = 0

#         def burilish(self, yonalish):
#             if yonalish == "chap":
#                 self.rul -= 1
#             elif yonalish == "o'ng":
#                 self.rul += 1

#     class Tormozlar:
#         def __init__(self):
#             self.bosish = 0

#         def tormoz_pedalini_bosmoq(self):
#             self.bosish += 10


import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, points):
        self.score += points

    def get_score(self):
        return self.score

    def __str__(self):
        return f"{self.name}: {self.score}"

class Game:
    def __init__(self, players):
        self.players = players

    def start_game(self):
        print("O'yinni boshlaymiz!")

        while True:
            for player in self.players:
                print(f"{player.name}ning navbati")

                number = random.randint(1, 10)

                taxmin = int(input("1 dan 10 gacha bo'lgan raqamni taxmin qiling: "))

                if taxmin == number:
                    print("To'g'ri taxmin qildingiz!")
                    player.add_score(10)
                else:
                    print("Kechirasiz taxminingiz hato:)")

            for player in self.players:
                print(player)
            a = input("O'yinni davom ettirasizlarmi? H yoki Y: ")
            if a =="H":
                continue
            else:
                print("O'yin yakunlandi:(")
                break


player1 = Player("Xolmirza")
player2 = Player("Mirafzal")
player3 = Player("Humoyun")
players = [player1, player2, player3]

game = Game(players)
game.start_game()
