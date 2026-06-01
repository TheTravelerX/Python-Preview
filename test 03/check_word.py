
target_word = 'mower'
target_letters = list(target_word)

word_list = ['_' for i in range(5)]

# guessing a 5-letter-word in six or few attempts
def check_word(input_word):
    if input_word == target_word:
        print('SPOT ON! You got it.')
    else:
        input_letters = list(input_word)
        for input_letter_index, input_letter in enumerate(input_letters):
            for target_letter_index, target_letter in enumerate(target_letters):
                if input_letter == target_letter:
                    if input_letter_index == target_letter_index:
                        word_list[input_letter_index] = input_letter
        
                    else:
                        print(f'Letter {input_letter} is in the target word...but not on the proper spot')
                
    print(' '.join(word_list)) # convert word_list to a string separated by spaces


check_word('boled')
