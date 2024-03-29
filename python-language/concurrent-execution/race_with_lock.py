import threading
from time import sleep
from random import random

counter = 0
randsleep = lambda: sleep(0.1 * random())
incr_lock = threading.Lock()

def incr(n):
    global counter
    for count in range(n):
        with incr_lock:
            current = counter
            randsleep()
            counter = current + 1
            randsleep()

n = 5
t1 = threading.Thread(target=incr, args=(n, ))
t2 = threading.Thread(target=incr, args=(n, ))
t1.start()
t2.start()
t1.join()
t2.join()
print(f'Counter: {counter}')