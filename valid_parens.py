# leetcode.com/problems/valid-parentheses/

def isValid(s:str) -> bool:

    open_arr = ['(', '[', '{']
    closing_arr = [')', ']', '}']

    track = []

    for i,char in enumerate(s):
        if char in open_arr:
            track.append(f'{open_arr.index(char)}')
        elif char in closing_arr:
            if s[i-1] in open_arr and open_arr.index(s[i-1]) == closing_arr.index(char):
                track.pop()
            else:
                track.append(f'{closing_arr.index(char)}')



    return len(track) % 2 == 0 and track == track[::-1]

print(isValid('()[]{}'))