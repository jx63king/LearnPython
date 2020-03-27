import threading
# x is a shared value
x = 0
COUNT = 1000000

def inc():
    global x
    for _ in range(COUNT):
        x += 1

def dec():
    global x
    for _ in range(COUNT):
        x -= 1

t1 = threading.Thread(target=inc)
t2 = threading.Thread(target=dec)
t1.start()
t2.start()
t1.join()
t2.join()

print(x)