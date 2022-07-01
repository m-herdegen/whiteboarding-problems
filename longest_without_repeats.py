# Given a string s, find the length of the longest substring without repeating characters.

# loop through the string
# check if the char has already been used
# save to a list or dict
# find the longest one
# take the length

def find_longest(in_list):
    max_string_len = 0
    for item in in_list:
        if len(item) > max_string_len:
            max_string_len = len(item)
    return max_string_len

def find_no_repeats(in_str):
    substring_list = ['']
    num_substrings = 0
    for char in in_str:
        if char not in substring_list[num_substrings]:
            substring_list[num_substrings] += char 
        else:
            num_substrings += 1
            substring_list.append(char)
    print(substring_list)
    return find_longest(substring_list)

print(find_no_repeats('my dearest darling talulah'))
