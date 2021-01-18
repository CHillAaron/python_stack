# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(num):
    for i in range(0 , len(num) - 1, 1):
        if num[i] >= 0:
            num[i] = "big"
        else:
            pass
    return num

print(biggie_size([-1, 3, 5, -5]))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(num):
    # print(num)
    count = 0
    for i in range(0 , len(num) - 1, 1):
        if num[i] > 0:
            count += num[i]
    num[-1] = count
    # print(count)
    # print(num)
    return num

print(count_positives([2,4,-6, 5, 2, -1]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(num):
    count = 0 
    for i in range(0 , len(num), 1):
        count += num[i]
    return count
    
print(sum_total([6, 3, -2]))

# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5


def average(num):
    count = 0 
    for i in range(0 , len(num), 1):
        count += num[i]
    print("this is the count before divide:",count)
    count = count /len(num)
    print("this is the count after divide:",count)
    return count
    
average([5,7,9,11])


# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(num):
    count = len(num)
    return count

length([2,4,6])

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def min(num):
    print(len(num))
    if len(num) == 0:
        return False
    count = num[0]
    for i in range(0 , len(num), 1):
        if count > num[i]:
            count = num[i]
            print("this is the min count:",count)
        elif count < num[i]:
                print("The count did nothing:")
                pass

    return count

min([])

# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def max(num):
    if len(num) == 0:
        return False
    count = num[0]
    for i in range(0 , len(num), 1):
        if count < num[i]:
            count = num[i]
        elif count > num[i]:
            pass
    return count

print(max([]))



# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(num):
    final = []
    sum_total = 0 
    for i in range(0 , len(num), 1):
        sum_total += num[i]
    final.append(sum_total)
    for i in range(0, len(num), 1):
        avg = sum_total / len(num)
    final.append(avg)
    if len(num) == 0:
       return False
    min = num[0]
    max = num[0]
    for i in range(0 , len(num), 1):
        if min > num[i]:
            min= num[i]
        elif min < num[i]:
                pass
    final.append(min)
        
    for i in range(0, len(num), 1):
        if max < num[i]:
            max = num[i]
        elif max > num[i]:
            pass
    final.append(max)

    final.append(len(num))
    print(final)
    

ultimate_analysis([7,2,8,4,7])

# 'length': 4 }
# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]


#option 1 the short way
def reverse(num):
    num.reverse()
    print(num)

#option 2 the step by step
def reverse2(num):
    length = len(num)
    for i in range(0, length / 2, 1):
        length = length - 1
        temp = num[i]
        num[i] = num[length]
        num[length] = temp
    print(num)
    return num


reverse([2, 4, 6,8,5])
