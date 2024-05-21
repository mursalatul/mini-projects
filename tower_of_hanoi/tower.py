class Tower:
    def __init__(self, tower1: list, tower2: list, tower3: list) -> None:
        self.tower1 = tower1
        self.tower2 = tower2
        self.tower3 = tower3

        # make it true before calling transfer to see the currect status
        # of the towers after each move [NOTE: it can generate longer output
        # as the total move = 2^totalDisk - 1, and for each move it will print
        # 3 towers]
        self.showTowerAfterEachMove = False

    def identifyDiskTower(self):
        self.totalDisk = max(len(self.tower1), len(self.tower2), len(self.tower3))
        if len(self.tower1):
            self.towerA = self.tower1
            self.towerB = self.tower2
            self.towerC = self.tower3
        elif len(self.tower2):
            self.towerA = self.tower2
            self.towerB = self.tower1
            self.towerC = self.tower3

        else:
            self.towerA = self.tower3
            self.towerB = self.tower2
            self.towerC = self.tower1

    def verifiedTower(self, towerX) -> bool:
        towerX2 = towerX.copy()
        towerX2.reverse()
        return towerX2 == sorted(towerX2) and len(towerX2) == self.totalDisk

    def transfer(self):
        self.identifyDiskTower()
        # store total number of moves (2^totalDisk - 1)
        self.total_move = 0

        print("Moves:")
        while True:
            # A <-> B
            if len(self.towerB) == 0:
                self.move(self.towerA, self.towerB)
                self.showMove("A", "B")
            elif len(self.towerA) == 0:
                self.move(self.towerB, self.towerA)
                self.showMove("B", "A")
            elif self.towerB[len(self.towerB) - 1] > self.towerA[len(self.towerA) - 1]:
                self.move(self.towerA, self.towerB)
                self.showMove("A", "B")
            else:
                self.move(self.towerB, self.towerA)
                self.showMove("B", "A")

            self.total_move += 1
            if self.verifiedTower(self.towerB):
                break

            # A <-> C
            if len(self.towerC) == 0:
                self.move(self.towerA, self.towerC)
                self.showMove("A", "C")
            elif len(self.towerA) == 0:
                self.move(self.towerC, self.towerA)
                self.showMove("C", "A")
            elif self.towerC[len(self.towerC) - 1] > self.towerA[len(self.towerA) - 1]:
                self.move(self.towerA, self.towerC)
                self.showMove("A", "C")
            else:
                self.move(self.towerC, self.towerA)
                self.showMove("C", "A")

            self.total_move += 1
            if self.verifiedTower(self.towerC):
                break

            # B <-> C
            if len(self.towerB) == 0:
                self.move(self.towerC, self.towerB)
                self.showMove("C", "B")
            elif len(self.towerC) == 0:
                self.move(self.towerB, self.towerC)
                self.showMove("B", "C")
            elif self.towerB[len(self.towerB) - 1] > self.towerC[len(self.towerC) - 1]:
                self.move(self.towerC, self.towerB)
                self.showMove("C", "B")
            else:
                self.move(self.towerB, self.towerC)
                self.showMove("B", "C")

            self.total_move += 1
            if self.verifiedTower(self.towerB) or self.verifiedTower(self.towerC):
                break

        print(f"Total moves: {self.total_move}")

    def showMove(self, x: str, y: str):
        print(f"{x} -> {y}")

        if self.showTowerAfterEachMove:
            a, b, c = "", "", ""
            if x == "A":
                a = "->"
            elif x == "B":
                b = "->"
            else:
                c = "->"
            if y == "A":
                a = "<-"
            elif y == "B":
                b = "<-"
            else:
                c = "<-"

            print(
                "A: ",
                self.towerA,
                a,
                "\n",
                "B: ",
                self.towerB,
                b,
                "\n",
                "C: ",
                self.towerC,
                c,
                sep="",
                end="\n\n",
            )

    def move(self, towerX: list, towerY: list):
        towerY.append(towerX.pop())


def main():
    tower1 = [3, 2, 1]
    tower2 = []
    tower3 = []

    t = Tower(tower1, tower2, tower3)

    print("Before Transfer:")
    print(tower1, tower2, tower3, sep="\n", end="\n\n")

    # t.showTowerAfterEachMove = True # make it false or comment out or remove for simple view
    t.transfer()

    print("\nAfter Transfer:")
    print(tower1, tower2, tower3, sep="\n")


main()
