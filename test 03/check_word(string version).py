target_word = 'lower'

def check_word_str(input_word):
    word_string = ''
    for i in range(len(target_word)):
        if input_word[i] in target_word:
            if input_word[i] == target_word[i]:
                word_string += (input_word[i] + ' ')
            else:
                word_string += '_ '
                print(f"Letter {input_word[i]} on index {i} is in the target word...but not in the proper spot")
        else:
            word_string += '_'

    print(word_string)


check_word_str('boler')