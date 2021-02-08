# -*- coding: utf-8 -*-
import datetime

def convertDay(x):
    return {
		0: 'Monday',
		1: 'Tuesday',
		2: 'Wednesday',
		3: 'Thursday',
		4: 'Friday',
		5: 'Saturday',
		6: 'Sunday',
    }[x]


print ("What's the matching day of the week for your date ?")

def getTheDate():
    isCorrect=False
    while not isCorrect:
        fromUser = raw_input("Please enter your date (use this format dd/mm/yyyy):")
        try:
            day,month,year = fromUser.split('/')
            d=datetime.datetime(int(year),int(month),int(day))
            isCorrect=True
        except:
            print ("\n\n\033[1;31m ੨( ･᷄ ︵･᷅ )ｼ The date format is not correct, please retry ! \033[0;0m \n\n")
    return d.weekday()

print ("\n \\0/ Your date is a \033[1;32m" + convertDay(getTheDate()) + "\033[0;0m")
