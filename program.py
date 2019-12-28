class J:
    def __init__(self, one):
        self.one = one

    def __repr__(self):
        return "This is a J class"

    def __add__(self, one , two):
        return one + two

j1 = J('fdf')
j2 = J('dfdf')
print(j1+j2)