import player

class Room:
    def __init__(self):
        self.data = []
        self.data.append([" ##"] + ["###" for i in range(10)] + ["## "])
        for i in range(10):
            self.data.append([" # "] + [" . " for i in range(10)] + [" # "])
        self.data.append([" ##"] + ["###" for i in range(10)] + ["## "])

        self.obj = {"Wall" : " # ", 
                    "Box"  : " B "}

    def __str__(self):
        s = ""
        for i in self.data:
            for j in i:
                s += j
            s += "\n"
        return s

    def __getitem__(self, pos):
        return self.data[pos]
    
    def modify(self, x, y, tp):
        self.data[x][y] = self.obj[tp]

    def modiList(self, modLst):
        for x, y, tp in modLst:
            self.modify(x, y, tp)

def near(rm: Room, tp: str, p: player.Player):
    dire = [rm[p.y + i][p.x + j] for i in (1, -1, 0) for j in (1, -1, 0) if i == 0 or j == 0]
    if rm.obj[tp] in dire:
        return True
    else:
        return False

if __name__ == "__main__":
    a = Room()
    ml = [(1, 1, "Wall"),
          (2, 2, "Box")]
    a.modiList(ml)
    a[3][3] = " o "
    # a.modify(1, 1, "Wall")
    # a.modify(10, 10, "Box")
    print(a)

