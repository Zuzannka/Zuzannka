class animals:
    def foo(self):
        print('jestem w klasie nadrzędnej')
krówka = animals()

class angels (animals):
    def foo(self):
        print('jestem w klasie podrzędnej')
piesek = angels()

class liar(animals):
    def foo(self):
        print('jestem w klasie nadrzędnej')
kot = liar()

krówka.foo()

piesek.foo()

kot.foo()


