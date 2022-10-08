#Loop through a data frame

#for (key, value) in student_data_frame.items():
#   print(value)


import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_letter_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#print(nato_letter_dict)
game_on = True

def generate_phonetic():
    word = input('Enter a word: ').upper()
    try:
        word_phonetic_code = [nato_letter_dict[letter] for letter in word]
    except KeyError:
        print('Sorry, only letters in the alphabet, please.')
        generate_phonetic()
    else:
        print(word_phonetic_code)
generate_phonetic()


