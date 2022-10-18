import time
import os

def esc(code):
    return f'\u001b[{code}m'

BLACK = esc(107)
WHITE = esc(47)
END = esc(0)
RED = esc(41)

rep = 50
r = 0
while r < 51:
    os.system('cls')
    print(BLACK + "  " * rep + RED + "  " + BLACK + "  "* r + END)
    time.sleep(0.5)
    rep -= 1
    r = r + 1

print('               КОНЕЦ ФИЛЬМА')
