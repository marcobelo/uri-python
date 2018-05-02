ave = {'carnivoro': 'aguia', 'onivoro': 'pomba'}
mamifero = {'onivoro': 'homem', 'herbivoro': 'vaca'}
vertebrado = {'ave': ave, 'mamifero': mamifero}

inseto = {'hematofago': 'pulga', 'herbivoro': 'lagarta'}
anelideo = {'hematofago': 'sanguessuga', 'onivoro': 'minhoca'}
invertebrado = {'inseto': inseto, 'anelideo': anelideo}
animal = {'vertebrado': vertebrado, 'invertebrado': invertebrado}

a = input()
b = input()
c = input()

print(animal[a][b][c])
