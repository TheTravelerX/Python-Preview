import os

# getting the directory path of the script -> __file__
script_dir = os.path.dirname(__file__)

# checks the current operating system and combines the file path and file name
# Windows use '\' while Mac use '/', so can't just use script_dir + '/sample_test.txt'
test_file = os.path.join(script_dir, 'sample_test.txt')


def headclone(input_f, line_num, output_f):
    index = 0
    with open(input_f) as file:
        for line in file:
            index += 1
            if index <= line_num:
                # if user choose to print lines to terminal
                if output_f == None: 
                    print(line.strip()) # .strip() clears the spaces at both the head and tail of a line

                # otherwise user writes to a specified new file
                else: 
                    with open(output_f, 'w') as new_file: # using 'w' instead of 'a' to prevent adding lines to the same new_file and an empty line on the top of it
                        new_file.write(f"\n{line.strip()}")
            else:
                break

    return output_f


# headclone(test_file, 3, None)

# headclone(test_file, 5, 'my_new_file.txt')

