class C1:
    def meth1(self): self.X = 88                # I assume X is mine
    def meth2(self): print(self.X)

class C2:
    def metha(self): self.X = 99                # Me too
    def methb(self): print(self.X)

class C3(C1, C2): ...

I = C3()                                        # Only 1 X in I!
