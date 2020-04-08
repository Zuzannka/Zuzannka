#1. Utwórz klasę (o dowolnej, sensownej nazwie), która będzie implementowała metodę foo(),
# która będzie printować komunikat “Jestem w klasie nadrzędnej”.
#2. Utwórz dwie klasy podrzędne, dziedziczące po klasie z punktu 2.
# Jedną z nich nazwij dowolnie, drugą Liar.
# Liar przy wywołaniu foo() powinien printować komunikat “Jestem w klasie nadrzędnej”.
# Druga klasa ma pisać “Jestem w podklasie”.
#3. Utwórz po dwie instancję każdej z klas i na wszystkich po kolei wywołaj metodę foo(). Zastosuj do tego pętlę.


class animals:
    def foo(self):
        print('jestem w klasie nadrzędnej')
idk = animals()

#husky = animals('fluffboi', 'yes')
class doggies (animals):
    def foo(self):
        print('jestem w klasie podrzędnej')
piesek = doggies()

class liar(animals):
    def foo(self):
        print('jestem w klasie nadrzędnej')
kot = liar()
#class pieski(zwierzaczki):
 #   def __init__(self, gatunek, rozmiar):
  #      print('jestem w podklasie')
   #     self.gatunek = gatunek
    #    self.rozmiar = rozmiar
#my_doggy=pieski('husky','duży')
#my_dog = zwierzaczki("husky", "duży")
#class liar(zwierzaczki):
 #   def __init__(self, gatunek, rozmiar):
  #      print('jestem w klasie nadrzędnej')
   #     self.gatunek = gatunek
#kot=liar('niepies','malutki')



idk.foo()

piesek.foo()

kot.foo()


