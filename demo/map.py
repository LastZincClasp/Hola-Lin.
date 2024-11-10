from obj import *

class Room:
    def __init__(self):
        self.data = []
        self.data.append([Wall(0, j) for j in range(0, 12)])
        for i in range(1, 11):
            self.data.append([Wall(i, 0)] + [Ground(i, j) for j in range(1, 11)] + [Wall(i, 11)])
        self.data.append([Wall(11, j) for j in range(0, 12)])

        self.obj = {"Wall" : Wall, 
                    "Box"  : Box,
                    "Grnd" : Ground,
                    "Plyr" : Player}

    def __str__(self):
        s = ""
        for i in self.data:
            for j in i:
                s += str(j)
            s += "\n"
        return s

    def __getitem__(self, pos):
        return self.data[pos]
    
    def modify(self, y, x, tp):
        self.data[y][x] = self.obj[tp](y, x)

    def erase(self, y, x):
        self.modify(y, x, "Grnd")

    def modiList(self, modLst):
        for y, x, tp in modLst:
            self.modify(y, x, tp)

def near(rm: Room, tp: str, p: Player):
    dire = [rm[p.y + i][p.x + j] for i in (1, -1, 0) for j in (1, -1, 0) if i == 0 or j == 0]
    if rm.obj[tp] in dire:
        return True
    else:
        return False

if __name__ == "__main__":
    a = Room()
    ml = [(3, 1, "Wall"),
          (2, 2, "Box"),
          (5, 6, "Plyr")]
    a.modiList(ml)
    # a[2][3] = " o "
    a.modify(1, 1, "Wall")
    a.modify(10, 10, "Box")
    print(a)

