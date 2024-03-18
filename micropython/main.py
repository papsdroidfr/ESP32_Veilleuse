import time, random
import machine, neopixel

np = neopixel.NeoPixel(machine.Pin(16), 12)

def allumage(np):
    n = np.n

    # cycle
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)


    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()

    # clear
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()

def veilleuse(np):
    n = np.n
    # bounce
    for i in range(4 * n):
        delta = 15-random.randrange(30)
        for j in range(n):
            np[j] = (128+delta, 0, 128+delta)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(random.randrange(20,200))    
    
try:
    allumage(np)
    while True:
        veilleuse(np)
except KeyboardInterrupt:  # interruption clavier CTRL-C: appel à la méthode destroy() de appl.
    print('bye')
