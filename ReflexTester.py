import time
import random


print("This is a reflex Tester when Console prints 'goooooo!' you have to press ENTER as fast as posible")
time.sleep(1)
print("ready?")

time.sleep((random.randint(5, 50)/10))

print("goooooo!")

start= time.time()

a=input()

stop = time.time()


print ("your reaction time is " + str(stop-start) + " Secounds")
