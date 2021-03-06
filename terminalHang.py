import sys
from random_word import RandomWords

# get a library of potential words
potential_words = RandomWords()

# Hangman game words initailisations
game_word = potential_words.get_random_word()
hidden_word = "*" * len(game_word)
incorrectly_guessed_letters = []

# Game Rules :-
# number of remaining guesses
# number of reattempts
# number of guesses added by reattempt
rem_guesses = 7
reattempts = 1
num_extra_guesses = 3

# Input: an integer
# Purpose: Print the state of the game board based on the number of guesses remaining
# Return: none, just prints direct to stdout
def get_image(guesses_left):
	switcher = {
		0:
			  "|----------|\n"
			+ "|          |\n"
			+ "|         /-\ \n"
			+ "|        /   \ \n"
			+ "|        \   / \n"
			+ "|         \_/ \n"
			+ "|          | \n"
			+ "|        --|-- \n"
			+ "|       /  |  \ \n"
			+ "|          | \n"
			+ "|        /---\ \n"
			+ "|       /     \ \n"
			+ "|       \     / \n"
			+ "|       _\   /_ \n"
			+ "|\n"
			+ "|",
		1:
			  "|----------| \n"
			+ "|          | \n"
			+ "|         /-\ \n"
			+ "|        /   \ \n"
			+ "|        \   / \n"
			+ "|         \_/ \n"
			+ "|          | \n"
			+ "|        --|-- \n"
			+ "|       /  |  \ \n"
			+ "|          | \n"
			+ "|        /---\ \n"
			+ "|       / \n"
			+ "|       \ \n"
			+ "|       _\ \n"
			+ "|\n"
			+ "|",
		2:
			  "|----------|\n"
			+ "|          |\n"
			+ "|         /-\ \n"
			+ "|        /   \ \n"
			+ "|        \   / \n"
			+ "|         \_/ \n"
			+ "|          | \n"
			+ "|        --|-- \n"
			+ "|       /  |  \ \n"
			+ "|          | \n"
			+ "|        /---\ \n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|",
		3:
			  "|----------|\n"
			+ "|          |\n"
			+ "|         /-\ \n"
			+ "|        /   \ \n"
			+ "|        \   / \n"
			+ "|         \_/ \n"
			+ "|          | \n"
			+ "|          | \n"
			+ "|          | \n"
			+ "|          | \n"
			+ "|        /---\ \n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|",
		4:
			  "|----------|\n"
			+ "|          | \n"
			+ "|         /-\ \n"
			+ "|        /   \ \n"
			+ "|        \   / \n"
			+ "|         \_/ \n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|",
		5:
			  "|----------|\n"
			+ "|          |\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|",
		6:
			  "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|\n"
			+ "|",
		7:
			""
	}
	print(switcher.get(guesses_left))

# Input: a character
# Purpose: Check if the character is a lowercase letter
# Return: boolean, true if letter, false otherwise
def check_if_letter(input):
	if input in [chr(i) for i in range(ord('a'),ord('z')+1)]:
		return True
	return False

# for each input we want to check if it is fistly an individual character
# but also if that character is in the word to guess
print("Word: " + hidden_word)
for line in sys.stdin:
	if "exit" == line.strip(): sys.exit()
	else:
		print("--------------------------------------------\n"
		    + "|           Current Game State             |\n"
		    + "--------------------------------------------")
		input_character = line.strip()
		if check_if_letter(input_character):
			if input_character in hidden_word:
				print("already correctly guessed this character")
			elif input_character in incorrectly_guessed_letters:
				print("already guessed this letter incorrectly")
			elif input_character in game_word:
				print("New letter found")
				occurances = game_word.count(input_character)
				most_recent_finding = 0
				for i in range(0, occurances):
					index_of_input = game_word.find(input_character, most_recent_finding, len(game_word))
					hidden_word = hidden_word[:index_of_input] + input_character + hidden_word[index_of_input+1:]
					most_recent_finding = index_of_input + 1
			else:
				rem_guesses = rem_guesses - 1
				print("Incorrect letter \n{} guesses remaining".format(rem_guesses))
				incorrectly_guessed_letters.append(input_character)
	if reattempts == 0 and rem_guesses == 0:
		print("Failed!!\nYou loose, the word was {}".format(game_word))
		get_image(rem_guesses)
		sys.exit()
	if rem_guesses ==  0:
		print("Failed!!, we will give you {}  more guesses, good luck".format(num_extra_guesses))
		print("...")
		print("Remaining Guesses is now {}".format(num_extra_guesses))
		rem_guesses = num_extra_guesses
		get_image(rem_guesses)
		reattempts = reattempts - 1
	if "*" not in hidden_word:
		print("Completed, you WIN!")
		print("Please play again soon")
		print("The word was {}".format(game_word))
		get_image(rem_guesses)
		sys.exit()

	print("Word: " + hidden_word)
	get_image(rem_guesses)
	print("Incorrect guesses so far: " + str(incorrectly_guessed_letters))

