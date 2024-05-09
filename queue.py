class SingleServerInfinite:
    def __init__(self, arivalRate, serviceRate, serverNum=1):
        self.arrive: int = arivalRate
        self.service: int = serviceRate
        self.c = serverNum

        self.rho = self.arrive / self.service
        self.lengthofSystem = self.rho / (1 - self.rho)
        self.lenghtofQueue = self.lengthofSystem - self.rho
        self.waitingTimeSystem = self.lengthofSystem / self.arrive
        self.waitingTimeQueue = self.lenghtofQueue / self.arrive

    def calculateProbability(self, n, atmost=False):
        probability = 0
        for i in range(n + 1):
            probability += (self.rho**i) * (1 - self.rho)
        if atmost:
            return probability

        return (self.rho**n) * (1 - self.rho)

    def expectedPeopleSystem(self):
        return self.lengthofSystem

    def expectedPeopleQueue(self):
        return self.lenghtofQueue

    def expectedSystemWait(self):
        return self.waitingTimeSystem

    def expectedQueueWait(self):
        return self.waitingTimeQueue
