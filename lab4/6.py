def reverse_words(sentence: str) -> str:
    words = sentence.split()

    def reverse_list(word_list: list) -> list:
        if len(word_list) <= 1:
            return word_list
        return reverse_list(word_list[1:]) + [word_list[0]]

    return " ".join(reverse_list(words))

s = input("Введите строку ")
print(reverse_words(s))