"""
PROBLEM: Given a character array, change all spaces to %20. You can assume that the array has
sufficient space at the end to hold the extra characters, and you are given the "true" length of
the array.

HINT: It's often easier to handle strings by iterating over them from beginning to end.

Okay, so I got the idea, and needed to read the second hint to be clued in that we don't necessarily
know that the string is exactly the right number of spaces, just that it is sufficient, so the first
thing we need to do is just count up the spaces. So thats one O(n) operation at the beginning.

Then we just need to iterate backwards through the array, once we make it to a valid character 

THE FANG BLANK     " // Two spaces means offset is set to 4.
.................K // Place the character offset by 4
.............BLANK // Keep going for all the rest
..........20%BLANK // Place % and 0 while iterating the offset down
......FANG20%BLANK // Offset now at 2, we continue
...20%FANG20%BLANK // Same situation
// Now we are finished as the offset is set to 0
The string, changed in place, should be equal now to:
THE20%FANG20%BLANK

iterate and find 2 spaces. that means we need 6 indices, or 4 extra indices.
we will keep track of how many spaces there are left to go through as we iterate backwards.
when we get to a character thats not a space we will move it back the amount of spaces left * 2
when we get to a space we will skip it and subtract one of our spaces

actually lets change the approach slightly.
we will keep track of our index offset. so we will have two numbers tracked, our iteration and our
"placing" index offset. once we count the spaces we multiply that by two to get our placing offset.
when we get to a character we place that character in the offset position. 
when we get to a space we we place the characters 20%, moving the offset as we go.
when the offset is at 0, we should be finished

NOTES: My original implementation (ignoring python syntactic issues) counted all the spaces even at 
the end of the array, when it was only meant to count the spaces in the "true" length of the string.
"""

def count_spaces(string, length):
    spaces = 0
    for i in range(length):
        if string[i] == ' ':
            spaces += 1
    return spaces

# Takes a string with extra space at the end and the length of the string without the extra space
def urlify(string, length):
    string = list(string)
    offset = count_spaces(string, length) * 2 
    i = length - 1
    while(offset > 0):
        c = string[i]
        if c == ' ':
            string[i + offset] = '0'
            string[i + offset - 1] = '2'
            string[i + offset - 2] = '%'
            offset -= 2
        else:
            string[i + offset] = c 
        i -= 1
    return "".join(string)

def test(string, length):
    print(string + " CONVERTED TO " + urlify(string, length))

test("Mr Rick          ", 7)
test("d a fas          ", 7)
            

       

