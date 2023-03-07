# Alfredo - 06032023 - Isto é um contador de 10 segundos impreciso

import time
import os

x = 0

while x < 10:
    x = x + 1
    time.sleep(1)
    os.system('cls')
    print("Counting: " + str(x))
