'''         Online method
file = open("char_count.txt", "r")

number_of_lines = 0
number_of_words = 0
number_of_characters = 0

for line in file:
    line = line.strip("\n")
    print(line)

    words = line.split()
    print(words)
    number_of_lines += 1
    number_of_words += len(words)
    number_of_characters += len(line)

file.close()

print("lines:", number_of_lines, "words:", number_of_words, "characters:", number_of_characters)
'''

# My method

number_of_lines = 0
number_of_words = 0
number_of_characters = 0

with open('.\char_count.txt', "r") as fp:
    file = [line.strip("\n") for line in fp.readlines()]
    number_of_lines = len(file)
    print(file)
    for line in file:
        line = line.split()
        for temp in line:
            number_of_characters += len(temp)
        number_of_words += len(line)

print("lines:", number_of_lines, "words:", number_of_words, "characters:", number_of_characters)