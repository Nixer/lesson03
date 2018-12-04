# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

# Вывести количество букв а в слове
word = 'Архангельск'
print(len(word))

# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = 'аоиеёэыуюя'
i = 0
for letter in word:
    if letter.lower() in vowels:
        i += 1
print(f'В слове {word} {i} гласных буквы')

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split(" ")))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split(" "):
    print(word[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
length_sum = 0
sentence_list = sentence.split(" ")
for word in sentence_list:
    length_sum += len(word)
print(length_sum/len(sentence_list))
