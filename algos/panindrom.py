def isPalindrome(stringInput):
    reverse = ""
    for i in range(len(stringInput)):
        reverse += stringInput[i]
    return reverse == stringInput

isPalindrome('bigib')

# 'potato'
# ''


def isPalindrome(stringInput):
    # print(stringInput)
    reversedVersion = ''
    for i in range(len(stringInput)-1, -1, -1):
        # print(stringInput[i])
        reversedVersion += stringInput[i]
    
    # print(reversedVersion)
    # if reversedVersion == stringInput:
    #     return True
    # else:
    #     return False
    return reversedVersion == stringInput
    
print(isPalindrome('potato')) #return false
print(isPalindrome('racecar')) #return true


def isPal2(stringInput):
    for i in range(0, len(stringInput)//2, 1):
        # print(stringInput[i])
        # print(stringInput[len(stringInput)-1-i])
        if stringInput[i] != stringInput[len(stringInput)-1-i]:
            return False
    return True

print(isPal2("aabcbaa"))