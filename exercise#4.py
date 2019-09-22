nameUser = input("Hello new user, please type in your name: ").title()
study = input("Hello " + nameUser + ", nice meeting you. What do you study here at KEA: ").upper()

if study == "BE-IT":
    print("We study the same thing, BE-IT!")
else:
        print("Oh you study " + study + ", well I'm studying BE-IT.")

print("Was nice meeting you! Have a pleasent day. Goodbye " + nameUser)
