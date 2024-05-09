run = True
arrivalRate = int(input("How many people arrive per hour: "))

serviceRate = int(input("How many people are served per hour: "))

if arrivalRate < serviceRate:
    p = arrivalRate / serviceRate


def pofn(n: int, atmost: bool = False):

    if n == 0:
        return 1 - p
    if atmost == True:
        return pofn(n - 2) + pofn(n - 1)

    else:
        return (p**n) * (1 - p)


noofpeople = int(input("What are the number of people in the system: "))

print(
    f"The probability that there are {
        noofpeople} number of people is {pofn(noofpeople)}"
)
