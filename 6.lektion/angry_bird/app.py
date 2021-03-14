from Bird import Bird
from Pig import Pig
import random

bird = Bird('Bird', 0, 0)
pig = Pig('Pig', random.randint(0,9), random.randint(0,9))

while(True):
    ## move control
    player = input()
    if(player == 'w'):
        bird.y = bird.y + 1
    elif(player == 's'):
        bird.y = bird.y - 1
    elif(player == 'd'):
        bird.x = bird.x + 1
    elif(player == 'a'):
        bird.x = bird.x -1
    else:
        print("wrong input")

    print('Bird location: ' + str(bird.x) + ',' + str(bird.y))


