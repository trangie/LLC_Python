from random import randint

x = randint(1,5)

print "the value generated randomly is: " + str(x)

user_input = raw_input("Please guess the value that I have selected randomly: ")

while int(user_input) != x:
    print"Your value " + user_input +" is not correct"
    #Force user to guess again
    user_input = raw_input("Please guess again: ")

print "*****YAY! You got the value!!!"