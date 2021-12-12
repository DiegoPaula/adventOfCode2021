input = open('input.txt', 'r').read().split('\n')

def sonarSweep(arr):
    lastNum = None
    status = ""
    total = 0
    for number in arr:
        if (lastNum == None):
            status = "(N/A - no previous measurement)"
        else:
            status = "increased" if int(number) > int(lastNum) else "decreased"
        lastNum = number
        if(status == "increased"):
            total += 1
    return total
print(sonarSweep(input))
