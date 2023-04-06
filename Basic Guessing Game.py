
the_word = "Kevin"
uguess = ""
attempts = 0
attempts_limit = 5
out_of_attempts = False


while uguess != the_word and not(out_of_attempts):
    if attempts < attempts_limit:
        uguess = input("Whats the word?: ")
        print("WRONG!")
        attempts += 1
    else:
        out_of_attempts = True

if out_of_attempts:
    print("You lose")
else:
    print("YOU WON in " + str(attempts) + " attempts")
