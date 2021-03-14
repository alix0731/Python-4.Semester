navn = "Ali"
gæt = ""
count = 0
guess_limit = 3
out_of_guesses = False

while gæt != navn and not(out_of_guesses):
    if count < guess_limit:
         gæt = input("Enter guess: ")
         count += 1
         print("lives left: " + str(guess_limit - count))
    else:
        out_of_guesses = True
   

if out_of_guesses:
    print("You lose...")
else:
    print("You win")