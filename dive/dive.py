input = open('input.txt', 'r').read().split('\n')


def dive(list):
    directionDict = {
        "forward": 0,
        "down": 0,
        "up": 0
    }
    for instruction in list:
        direction = instruction.split(' ')[0]
        intensity = int(instruction.split(' ')[1])
        directionDict[direction] += intensity
    return (directionDict["down"] - directionDict["up"]) * directionDict["forward"]


def diveB(list):
    route = {
        "forward": 0,
        "down": 0,
        "up": 0,
        "aim": 0,
        "depth": 0
    }
    for instruction in list:
        direction = instruction.split(' ')[0]
        intensity = int(instruction.split(' ')[1])
        route[direction] += intensity
        if (direction == "forward"):
            route["aim"] = route["down"] - route["up"]
            route["depth"] += route["aim"] * intensity
    return (route["forward"] * route["depth"])


print(diveB(input))
