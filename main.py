import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def bal_qoshish(self, points):
        self.score += points

    def bal_olish(self):
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
                    player.bal_qoshish(10)
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
