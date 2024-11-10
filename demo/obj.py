class Obj:
    def __init__(self, y, x, apr, passable):
        self.appearence = apr
        self.y, self.x = y, x
        self.passable = passable

    def __str__(self):
        return self.appearence

class Player(Obj):
    def __init__(self, y, x):
        super().__init__(y, x, " O ", False)

class Wall(Obj):
    def __init__(self, y, x):
        if (y, x) in ((0, 0), (11, 0)):
            apr = " ##"
        elif (y, x) in ((0, 11), (11, 11)):
            apr = "## "
        elif x in (0, 11):
            apr = " # "
        elif y in (0, 11):
            apr = "###"
        else:
            apr = " # "
        super().__init__(y, x, apr, False)


class Ground(Obj):
    def __init__(self, y, x):
        super().__init__(y, x, " . ", True)


class Iteractable(Obj):
    def __init__(self, y, x, apr, passable, func):
        super().__init__(y, x, apr, passable)
        self.functional = func

class Box(Iteractable):
    def __init__(self, y, x):
        super().__init__(y, x, "(B)", False, self.randItem)
        self.item = [("Sword", 0.6), 
                     ("Cat", 0.4)]

    def randItem(self):
        pass
        # not yet think about returning


