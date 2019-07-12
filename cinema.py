#Exercise 5 (Cinema): This is a program that checks whether a user is 
#old enough to watch a film and whether there are enough seats left. 
#The system also updates itself when somebody buys a film ticket
#and reduces the number of seats by one when someone purchases a ticket.

#Create a dictionary [age limit, no. of seats)
films = {
    "Finding Dory": [3,5],
    "Bourne": [18,5],
    "Tarzan": [15,5],
    "Ghost Busters": [12,5]
    }

while True:
    choice = input("What film would you like to watch?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())

            #check user age
        if age >= films[choice][0]:
            #check enough seats

            if films[choice][1] > 0:
                print("Enjoy the film!")
                films[choice][1]=films[choice][1]- 1
            else:
                print("Sorry, we are sold out!")
        else:
            print("You are too young to see that film!")
    else:
        print("We don't have that film...")
