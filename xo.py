class XoGame:
    def __init__(self):
        self. map = [[], [], []]
        for x in range(3):
            for y in range(3):
                self.map[x].append(-1)
        self.type = "1"

    def draw(self, map):
        for x in range(3):
            print("---------------------------------------")
            for y in range(3):
                shape = "     " + "     "
                if map[x][y] != -1:
                    shape = "     "+map[x][y] + "     "
                print(shape, end="|")
            print("")
            print("---------------------------------------")

    def read(self, map, type):

        print("torn player number " + type)
        print("enter X ")
        x = input()
        X = int(x)
        while X > 2 or X < 0:
            print("reprte enter X")
            x = input()
            X = int(x)

        print("enter Y")
        y = input()
        Y = int(y)
        while Y > 2 or Y < 0:
            print("reprte enter Y")
            y = input()
            Y = int(y)
        if type == "1":
            map[X][Y] = "O"
        else:
            map[X][Y] = "X"

    def check_read_value(self, map, x, y):

        pass

    def check(self, map, type):
        resalut = False
        value = "X"
        if type == "1":
            value = "O"
        for i in range(3):
            if map[i][0] == value and map[i][1] == value and map[i][2] == value:
                resalut = True
            if map[0][i] == value and map[1][i] == value and map[2][i] == value:
                resalut = True
        return resalut

    def play(self):
        OK = True
        while(OK):
            self.draw(self.map)
            self.read(self.map, self.type)
            OK = not self.check(self.map, self.type)
            if self.type == "1":
                self.type = "2"
            else:
                self.type = "1"
