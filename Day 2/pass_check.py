external_file = open('input.txt')

text_input = list(external_file.readlines())

text_input = list(map(str.strip, text_input))

text_input = [entry.replace(' ', '') for entry in text_input]

print(text_input)

list_minimum = []

list_maximum = []

list_letter = []

list_password = []

for k in text_input:

    minimum = int(k[slice(0, (k.find("-")))])

    list_minimum.append(minimum)

    maximum = int(k[slice(k.find("-") + 1, k.find(":") - 1)])

    list_maximum.append(maximum)

    letter_to_find = k[k.find(":") - 1]

    list_letter.append(letter_to_find)

    password = k[k.find(":") + 1:]

    list_password.append(password)

counter = 0

right_pass = 0
too_many = 0
too_few = 0

for passwords in list_password:

    number = passwords.count(list_letter[counter])

    if list_maximum[counter] >= number >= list_minimum[counter]:

        right_pass += 1

    if list_maximum[counter] <= number:

        too_many += 1

    if number <= list_minimum[counter]:

        too_few += 1

    counter += 1

print(right_pass)
