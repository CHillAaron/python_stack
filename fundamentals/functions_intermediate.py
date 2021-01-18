import random
def randInt(min=0 , max=100   ):
    num = random.random() * 100
    num = round(num)
    return num
print("this is the first number:",randInt()) 		    # should print a random integer between 0 to 100
print("this is the second number:",randInt(max=50)) 	    # should print a random integer between 0 to 50
print("this is the third number:",randInt(min=50)) 	    # should print a random integer between 50 to 100
print("this is the last number:",randInt(min=50, max=500))    # should print a random integer between 50 and 500