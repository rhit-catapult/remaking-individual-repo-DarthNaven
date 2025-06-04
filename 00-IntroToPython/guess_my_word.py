print("Guess my word")
import random
def update_display_word(dw, sw, g):
    new_display_word = ""

    for k in range(len(sw)):
        if g == sw[k]:
            new_display_word += g
        else:
            new_display_word += dw[k]


    return new_display_word

def main():
    word_options = ["gore", "slime", "death", "eldritch", "god", "jazz", "melt", "run", "puke", "runners", "destruct"]
    secret_word = random.choice(word_options)
    word_length = len(secret_word)
    display_word = "*" * word_length
    print(display_word)
    guessed_letters = []
    guesses = 0
    while True:
        guess = input("guess a letter:")
        if guess in guessed_letters:
            print("you already guessed that letter")
            continue
        if len(guess) != 1:
            print("I asked for only one letter")
            continue
        if display_word == secret_word:
            print("YOU WIN!")
            print("I took you",guesses,"guesses")
            break
        guesses += 1
        guessed_letters.append(guess)
        display_word = update_display_word(display_word, secret_word, guess)
        print(display_word)

main()















