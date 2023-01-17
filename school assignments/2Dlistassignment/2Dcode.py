import random
is_available = 0

def makelists():
    list_base = [[], [], [], []]
    for i in range(4):
        for j in range(1, 31):
            list_base[i].append(random.randint(0,1))
    return list_base


Dlist = makelists()
print(Dlist)
choice = int(input("Which Period Do you need(input a number 1-4): "))
comp = int(input("Which Computer number Do you need(input a number 1-30): "))
if Dlist[choice-1][comp-1]:
    print("That computer is available")
else:
    print("That computer is taken")