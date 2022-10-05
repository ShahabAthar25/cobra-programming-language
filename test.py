class A:
    def __init__(self):
        self.a = 123

class B:
    def __init__(self):
        self.b = 321

class C(A, B):
    def __init__(self):
        super().__init__()

    def print_all(self):
        print(self.a, self.b)

C_instance = C()
C_instance.print_all()