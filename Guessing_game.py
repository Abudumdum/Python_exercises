# This is a comment
# Dont forget that writing comments is a very essential part of writing a code
secret_number = 8
guess_try = 3
print('''You have just 3 tries to guess the secret number 
GOODLUCK!
''')
guess_count = 0
while guess_count < guess_try:
    guess = int(input("GUESS: "))
    guess_count += 1
    if guess == secret_number:
        print("Congrats you found the secret number!")
        break
else:
    print("Sorry you lost the guessing game try again later")
