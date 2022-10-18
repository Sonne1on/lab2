def esc(code):
    return f'\u001b[{code}m'

GREEN = esc(42)
END = esc(0)
YELLOW = esc(43)
RED = esc(41)
WHITE = esc(47)

def func():  # Рисуем график функции
    for i in range(0, 10):
        y = 9-i
        x=y**0.5
        x10=int(x*10)
        print(YELLOW + str(9 - i) + WHITE+ ' ' * (x10) + GREEN + '  ' * 1 + END,'  ', "{0:.2f}".format(x))
func()
print(YELLOW + ' 0.........1..........2.........3...' + END)
