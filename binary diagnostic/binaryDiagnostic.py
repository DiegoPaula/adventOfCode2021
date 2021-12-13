input = open('input.txt', 'r').read().split('\n')


def binaryDiagnostic(arr):
    gamma = ""
    epsilon = ""

    for index in range(0, len(arr[0])):
        counter = 0
        for binary in arr:
            counter = counter + 1 if binary[index] == "1" else counter - 1
        gamma += "1" if counter >= 0 else "0"
        epsilon += "1" if counter <= 0 else "0"
    return int(gamma, 2) * int(epsilon, 2)


def binaryDiagnosticB(arr):
    oxygenGeneratorRating = ""
    CO2ScrubberRating = ""
    oxygenDiagnostic = ""
    CO2Diagnostic = ""

    for index in range(0, len(arr[0])):
        counterOxygen = 0
        counterCO2 = 0
        for binary in arr:
            if(binary[:index] == oxygenGeneratorRating):
                oxygenDiagnostic = binary
                counterOxygen += 1 if binary[index] == "1" else -1

            if(binary[:index] == CO2ScrubberRating):
                CO2Diagnostic = binary
                counterCO2 += 1 if binary[index] == "1" else -1

        oxygenGeneratorRating += "1" if counterOxygen >= 0 else "0"
        CO2ScrubberRating += "0" if counterCO2 >= 0 else "1"
    return int(oxygenDiagnostic, 2) * int(CO2Diagnostic, 2)


print(binaryDiagnosticB(input))
