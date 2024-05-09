from queue import SingleServerInfinite

run = True

while run:
    arrive = int(input("How many people arrive per hour: "))
    service = int(input("How many people are served per hour: "))

    q = SingleServerInfinite(arrive, service)

    print(
        """
    You can check:
1. Probability of 0 people on the queue
2. Probabilty of n people on the queue
3. Expected length of people in the queue
4. Expected length of people in the system
5. Expected wait time in the queue
6. Expected wait time in the system
7. QUIT
    \n"""
    )

    answer = input("Pick a number from the ones listed above: ")

    match answer:
        case 1:
            print(f"Probabilty of 0 people on the queue is {q.calculateProbability(0)})

        case 2:
            n = int(input("What is the number of people: "))
            print(f"Probabilty of {n} number of people on the queue is {q.calculateProbability(n)})

        case 3:
            print(f"Expected length of people in the queue is {q.expectedPeopleQueue()}")
        case 4:
            print(f"Expected length of people in the system is {q.expectedPeopleSystem()}")
        case 5:
            print(f"Expected wait time of people in the queue is {q.expectedQueueWait()}")
        case 6:
            print(f"Expected wait time of people in the queue is {q.expectedSystemWait()}")
        case 7:
            run = False
