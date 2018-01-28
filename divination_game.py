print("**************************************")
print ("** Welcome to The Divination Game! **")
print("**************************************")
print("")

sort_number = 42
attempts_number = 3

for count in range(1, attempts_number + 1):

    print("Attempt {} of {}".format(count, attempts_number))
    guess_number  = int(input("Enter a number between 0 and 100! \n"))
    
    if guess_number < 1 or guess_number > 100:
        print("Invalid number!")
        continue

    message = "right." if (guess_number == sort_number) else "wrong."
    message_approximate = "The entered number is minor!" if guess_number < sort_number else "The entered numer is greater!" if guess_number > sort_number else ""

    print("This number is", message, message_approximate)
    print("")
    
    if guess_number == sort_number:
        break

print("End of game!")
