# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count("а"))

# Вывести количество гласных букв в слове
word = 'Архангельск'
print(sum([1 for item in word.lower() if item in "аеёиоуыэю"]))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for item in sentence.split():
    print(item[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
for item in sentence.split():
    print(len(item))
