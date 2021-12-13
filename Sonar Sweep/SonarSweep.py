input = open('input.txt', 'r').read().split('\n')


def sonarSweep(arr):
    lastNum = None
    status = ""
    total = 0
    for number in arr:
        if (lastNum == None):
            status = "(N/A - no previous measurement)"
        else:
            status = "(increased)" if int(number) > int(
                lastNum) else "(decreased)"
        lastNum = number
        if(status == "(increased)"):
            total += 1
    return total


def sonarSweepB(arr):
    lastNum = None
    status = ""
    total = 0
    for index in range(0, len(arr)-2):
        numbers = [int(x) for x in arr[index:index+3]]
        if (lastNum == None):
            status = "(N/A - no previous measurement)"
        elif (sum(numbers) == lastNum):
            status = "(no change)"
        else:
            status = "(increased)" if sum(numbers) > lastNum else "(decreased)"
        lastNum = sum(numbers)
        if(status == "(increased)"):
            total += 1
    return total


print(sonarSweepB(input))
