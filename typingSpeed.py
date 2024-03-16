from time import *
# counts the seconds from 1971 to today
# print(time())

import random as r  # to type multiple strings


def mistake(partest, usertest):  # test # testinput
    # we are going to check the result of test1 and testinput and match them
    # and checking the number of mistakes
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error


def speed_time(time_start, time_end, userinput):
    # here we need round off time. not decimal
    time_delay = time_end - time_start
    time_roundoff_time = round(time_delay, 2)
    speed = len(userinput) / time_roundoff_time
    return round(speed)


test = ["hello! i am vani from bharuch.Nice to meet youu. see you soon!", "I study in charusat changa.",
        "always doing hehehehehe"]

# i want only one string from the list
# creating a variable which gives one string from test variable through random module
test1 = r.choice(test)
print("----Typing speed----")
print(test1)
print()
print()
time_1 = time()
# going to take input form user
testinput = input(" Enter :")
time_2 = time()

# discuss what we need here
# 1. Speed calculation
# 2.number of mistakes(errors)

print('Speed : ', speed_time(time_1, time_2, testinput),'Word per second')
print('Error : ',mistake(test1,testinput))
