from queue import *

run = True

while run:
    arrive = int(input("How many people arrive per hour: "))
    service = int(input("How many people are served per hour: "))

    print(
        """
    You can check:
1. Probability of 0 people on the queue
2. Probabilty of n people on the queue
3. Expected length of people in the queue
4. Expected length of people in the system
5. Expected wait time in the queue
6. Expected wait time in the system
    \n"""
    )

    answer = input("Pick a number from the ones listed above: ")
