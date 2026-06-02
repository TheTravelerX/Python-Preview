# The Count of Monte Cristo is a novel by Alexandre Dumas that is considered a classic. Nevertheless, in the introduction of an English translation of the book, the writer Umberto Eco confesses that he found the book to be “one of the most badly written novels of all time”.

# In particular, he says it is “shameless in its repetition of the same adjective,” and mentions in particular the number of times “its characters either shudder or turn pale.”

# To see whether his objection is valid, let’s count the number number of lines that contain the word pale in fany form, including pale, pales, paled, and paleness, as well as the related word pallor. Use a single regular expression that matches any of these words. As an additional challenge, make sure that it doesn’t match any other words, like impale – you might want to ask a virtual assistant for help.

import os
import re

# get the a file path that is irrelevant with OS and current terminal directory
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'sample_paragraph.txt')

pattern = ' pale| pallor'

with open(file_path) as test_file:
    str_content = test_file.read() # convert the content of test_file to a string, since re.search(pattern, [string])
    overall_result = re.search(pattern, str_content)

count = 0
with open(file_path) as test_file:
    for line in test_file:
        result = re.search(pattern, line)
        if result:
            count += 1
            print(line.strip())
    
print("\n", overall_result)

print(f"Match Lines: {count}")

