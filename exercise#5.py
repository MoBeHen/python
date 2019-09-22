age = input("Hello new user, what is your age? \n")
age = int(age)
myAge = 30
myAge = int(myAge)

newAge = (myAge + age)

ageAverage = (newAge / 2)
ageAverage = int(ageAverage)

print("It would seem the average age between us is " + str(ageAverage) + " years.")

ageDifference = (age - myAge)
ageDifference = int(ageDifference)

print("And the age difference from me to our ages, is " + str(ageDifference) + " years.")
