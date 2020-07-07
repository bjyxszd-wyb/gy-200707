class bbbb():
    a = None
    b = None
    res = None

    def input(self, a, b):
        self.a = a
        self.b = b
    def sum(self):
        self.res = self.a + self.b
    def div(self):
        self.res = self.a / self.b

    def cccc(self):
        print(self.res)

c = bbbb()

c.input(10,30)
c.sum()
c.cccc()
c.div()
c.cccc()