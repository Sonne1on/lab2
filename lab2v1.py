def esc(code):
    return f'\u001b[{code}m]'
RED = esc(41)
WHITE = esc(47)
END = esc(0)
BLACK = esc(40)

def Pol_fl(): # Рисуем флаг Польши

    for i in range(5):
        print(WHITE + ' ' * (50) + END)
    for i in range(5):
        print(RED + ' ' * (50) + END)

Pol_fl()
print()

def Patt(): # Рисуем узор

    print(BLACK + '   ' * 13 + END)
    print(WHITE + '   ' * 6 + BLACK + '   ' * 1 + WHITE + '   ' * 6 + END)
    print(WHITE + '   ' * 6 + BLACK + '   ' * 1 + WHITE + '   ' * 6 + END)
    print(BLACK + '   ' * 13 + END)
    print(WHITE + '   ' * 2 + BLACK + '   ' * 1 + WHITE + '   ' * 7 + BLACK + '   ' * 1 + WHITE + '   ' * 2 + END)
    print(WHITE + '   ' * 2 + BLACK + '   ' * 1 + WHITE + '   ' * 7 + BLACK + '   ' * 1 + WHITE + '   ' * 2 + END)
    print(BLACK + '   ' * 13 + END)

Patt()
print()