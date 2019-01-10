import datetime
import random
import time

print("REACTION GAME")
player1 = input("Player 1 name?: ")
player2 = input("Player 2 name?: ")



print(player1 + " Let's test your reaction time")
time.sleep(1)

print("get ready to press enter...")
time.sleep(random.randint(3,10))
then1 = datetime.datetime.now()
t1 = input("GO!!")
now1 = datetime.datetime.now()

dif1 = then1 - now1

reactionTime1 = abs(dif1.total_seconds())

print(reactionTime1)

print(player2 + " Let's test your reaction time")
time.sleep(1)

print("get ready to press enter...")
time.sleep(random.randint(3,10))
then2 = datetime.datetime.now()
t2 = input("GO!!")
now2 = datetime.datetime.now()

dif2 = then2 - now2

reactionTime2 = abs(dif2.total_seconds())

print(reactionTime2)


if reactionTime1 < reactionTime2:
    print(player1 + " wins by " + str((reactionTime2 - reactionTime1))+ " seconds!")

else:
    print(player2 + " wins by " + str((reactionTime1 - reactionTime2)) + " seconds!")
