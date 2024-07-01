calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    global calls
    calls += 1
    txt_lower = string.lower()
    txt_upper = string.upper()
    lenght = len(string)

    return lenght, txt_lower, txt_upper


def is_contains(string, list_to_search):
    global calls
    calls += 1
    for item in list_to_search:
        if item.lower() == string.lower():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
