text = input("Введите текст: ")
words = text.split()

def analysis(word_list):

    print(f"Кол-во слов: {len(word_list)}")

    word_counts = {}
    for word in word_list:
        w = word.lower()
        if w in word_counts:
            word_counts[w] += 1
        else:
            word_counts[w] = 1

    for word, count in word_counts.items():
        print(f"Частота каждого слова:  {word}: {count}")

    max_count = 0
    max_word = ""
    for word, count in word_counts.items():
        if count > max_count:
            max_count = count
            max_word = word
    print(f"Самое частое слово: {max_word} ")

    shortest = word_list[0]
    longest = word_list[0]
    for word in word_list:
        if len(word) < len(shortest):
            shortest = word
        if len(word) > len(longest):
            longest = word
    print(f"Самое короткое слово: '{shortest}' (длина: {len(shortest)})")
    print(f"Самое длинное слово: '{longest}' (длина: {len(longest)})")
print("Анализ полного текста")
analysis(words)
filtered_words = [word for word in words if len(word) >= 3]
print("Анализ текста со словами не больше трех букв")
analysis(filtered_words)






