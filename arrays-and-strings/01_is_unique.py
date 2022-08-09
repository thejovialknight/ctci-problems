def check_all_unique(string):
    string_map = {};
    for c in string:
        if c not in string_map:
            string_map[c] = True
        else:
            return False
    return True

def test_and_print(string):
    if check_all_unique(string):
        print("All unique in '" + string + "'")
    else:
        print("Not all unique in '" + string + "'")

test_and_print("string")
test_and_print("You're my bae")
test_and_print("ABCDeFGHIJK")
