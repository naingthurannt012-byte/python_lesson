# Function to convert cat age to human years
def cat_age_to_human(cat_age):
    if cat_age <= 0:
        return 0
    elif cat_age == 1:
        return 15
    elif cat_age == 2:
        return 15 + 9
    else:
        return 15 + 9 + (cat_age - 2) * 4


# Function to insert spaces between capital words
def capital_words_spaces(text):
    result = ""
    for i, char in enumerate(text):
        if i > 0 and char.isupper():
            result += " " + char
        else:
            result += char
    return result


# Function to reverse each string in a list
def reverse_string_list(strings):
    return [s[::-1] for s in strings]


# Examples
print(cat_age_to_human(1))   # Output: 15
print(cat_age_to_human(2))   # Output: 24
print(cat_age_to_human(3))   # Output: 28
print(cat_age_to_human(10))  # Output: 56

print(capital_words_spaces("Python"))                     # Output: "Python"
print(capital_words_spaces("PythonProgrammingExamples"))  # Output: "Python Programming Examples"
print(capital_words_spaces("GetReadyToBeCodingFreak"))    # Output: "Get Ready To Be Coding Freak"

print(reverse_string_list(['Red','Green','Blue','White','Black']))
# Output: ['deR','neerG','eulB','ethiW','kcalB']

def capital_words_spaces(text):
    result = ""

    for ch in text:
        if ch.isupper() and result != "":
            result += " "
        result += ch

    return result