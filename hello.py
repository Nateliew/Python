import random
msg = "Welcome to my first game!"
print(msg)

name = input("What is your name? ")
age= int(input("What is your age? "))

if type(age) == int:
        if age>=18:
            print("You can play")
            wants_to_play = input("Do you want to play? Type yes or no: ").lower()
            print(type(wants_to_play))
        
            if wants_to_play == "yes":
                print("Yay!")

                randomNum = random.randint(0,9)
            
                guess = int(input("Guess a number between 0 and 9. You have 5 chances. "))
                print(type(guess))
                i = 1
                while i < 5:
                
                    if guess == randomNum and type(guess) == int:
                        if i == 1:
                            print("Congratulations on your first try! You won!")
                            break
                        else:
                            print("You won!")
                            break
                else: 
                    int(input("You have " + str(5-i)  + " chances. Guess again: "))
                    i +=1

            else: 
             print("Bye!")


    # elif age >=13:
    #     print("You need adult supervision")
        else:
            print("You are not qualified.")
else:
    print("Not a number")



