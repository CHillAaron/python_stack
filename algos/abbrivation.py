"National Basketball Association" = "NBA"
"Central intelligence agency" = "CIA"


def acronym(stringInput):
    result = []
    for i in range(len(stringInput)):
        if stringInput[i] == " ":
            result.append(stringInput[i] +1)
        else: 
            pass
        print("this is the acronym:",result)
    # return acm

acronym(["National Basketball Association"])



