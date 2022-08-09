"""
PROBLEM: Given two strings, write a method that decides if one is a permutation of the other

IDEAS: The brute force method would be to go through each character in the first string and check
the characters in the second string for a match, keeping track of where we've been.
This would be O(n^2). We can probably do better than this obvs.

The second thing I can think of is a hashmap. We will make a hashmap that maps to characters.
We will iterate through both arrays and add the character counts to each strings respective
hashmap, then we will compare the matches.

Actually an even better idea, we will use one hashmap and on the iteration through the second
array we will subtract those characters and be left with 0 at the end. If in the second iteration
a character isn't matched, we return false immediately.

PSEUDOCODE:
map

for all chars in s1
    add character to map
for all chars in s2
    if character not found return false    
    subtract char from map
    if count is less than 0 return false
return true

NOTES: I made a few logical mistakes here. My first implementation was only interested in whether
the chars found in s1 are all subtracted the correct amount by s2, without regard for characters in s2
that don't exist in s1. This is a major error. Make sure that ALL data checking is accounted for.
"""

def check_permutation(s1, s2):
    char_map = {}
    for c in s1:
        if c not in char_map:
            char_map[c] = 1
        else:
            char_map[c] += 1
    for c in s2:
        if c not in char_map:
            return False
        else:
            char_map[c] -= 1
            if char_map[c] < 0:
                return False
    for count in char_map.values():
        if count != 0:
            return False
    return True

def test(s1, s2):
    print("'" + s1 + "' and '" + s2 + "' returned " + str(check_permutation(s1, s2)))

test("asd", "das")
test("ddd", "dddd")
test("george", "ggeorge")
test("", "")
test("a", "")
test("", "a")
