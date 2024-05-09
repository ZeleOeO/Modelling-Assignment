class SingleServerInfinite:
    def __init__(self, arivalRate, serviceRate, serrverNum=1):
        self.arrive = arivalRate
        self.service = serviceRate
        self.c = serrverNum

        self.rho = self.arrive / self.service
        self.lengthofSystem = self.rho / (1 - self.rho)


def calculateProbablity(self, n):
    return (self.rho**n) * (1 - self.rho)
