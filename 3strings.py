language = 'Python'

# print(len(language))

# Access each individual letter

# letter = language[3]
# letter = language[0:3] # first to third letter
# letter = language[1:]  # skip first letter and show all the remaining part
letter = language[-1]  # get reverse of string

# String Methods

languageString = 'Street of The Dead White Walkers RIP 1 EPISODE'
upper_language = languageString.upper()
lower_language = languageString.lower()
find_text = languageString.find("Dead")
replace_text = languageString.replace("White", "Black")
print(replace_text)
