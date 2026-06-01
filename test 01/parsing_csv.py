# Testing the .split() function and list comprehension technique


def parse_csv_line(line):
    element_list = line.split(",")
    raw_scores = element_list[1:]
    scores = [int(score) for score in raw_scores] # list comprehension
    
    return {'name': element_list[0], 'scores': scores, 'avg': sum(scores) / len(scores)}

print(parse_csv_line("Alice,85,92,78"))

# Flaws: requires specific inputs since list slicing logics are hardcoded.