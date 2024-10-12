import pandas

#TODO 1. Create a dictionary in this format:
phonetic_words = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in phonetic_words.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_input = input("Enter any word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, please enter letters only.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()


