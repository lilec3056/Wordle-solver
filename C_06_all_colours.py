import csv
import re

with open('words_old.txt', newline='') as f:
    reader = csv.reader(f)
    raw_list = list(reader)

word_list = []
for item in raw_list:
    # takes first item of mini-list and adds it to new single_word list.
    word_list.append(item[0])


# list to store words to remove.
to_remove = []


def letter_and_dashes(question):
    while True:

        # Collect the input
        pattern = re.compile(r'^[a-zA-Z-]+$')
        while True:
            feed_in = input(question)
            if not len(feed_in) == 5:
                print("Invalid input. Please enter 5 characters.")

            elif pattern.match(feed_in):

                return feed_in

            else:
                print("Invalid input. Please enter only letters or dashes.")


def yellow_letter_solver(yellow):
    print(yellow)
    if yellow == "-----":
        print("No yellow letters")
        pass

    for word in word_list:

        count = 0
        for character in yellow:

            # ignore dashes
            if character == "-":
                pass

            # remove where the letter is green not yellow
            elif character[count] == word[count]:
                print(f"{character} is not green")
                to_remove.append(word)

            # remove words which don't contain the letter
            elif character not in word:
                print(f"{character} is not in word")
                to_remove.append(word)

        count += 1


def green_letter_solver(green):
    print(green)
    if green == "-----":
        print("No green letters")
        pass

    for word in word_list:

        count = 0
        for character in green:

            # ignore dashes
            if character == "-":
                pass

            # remove where the letter is green not yellow
            elif character[count] != word[count]:
                print(f"{character} is in the incorrect place")
                to_remove.append(word)

            # remove words which don't contain the letter
            elif character not in word:
                print(f"{character} is not in word")
                to_remove.append(word)

        count += 1


def grey_letter_solver(grey):

    # iterate through the word list.
    for word in word_list:

        # for each word, if the word contains a letter,
        # that is not in the word, add it to our list of words to be removed.
        for character in grey:
            if character in word:
                print(f"remove {word}")
                to_remove.append(word)


# Main routine goes here

grey_letters = letter_and_dashes("What are the grey letters? ")
yellow_letters = letter_and_dashes("What are the yellow letters? ")
green_letters = letter_and_dashes("What are the green letters? ")

grey_letter_solver(grey_letters)
yellow_letter_solver(yellow_letters)
green_letter_solver(green_letters)

# remove the words identified above from our wordlist
for item in to_remove:
    if item in word_list:
        word_list.remove(item)
    else:
        pass
print(to_remove)
print()
print(word_list)

keep_going = input("press <enter> to continue or any key to end: ")

    # if keep_going != '':
    #     break

