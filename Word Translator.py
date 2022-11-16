# changes every vowel (AEIOU) to the letter "K"
def translate(word):
    ftranslate = ""
    for letter in word:
        if letter.lower() in "aeiou":
            if letter.isupper():
                ftranslate = ftranslate + "K"
            else:
                ftranslate = ftranslate + "k"
        else:
            ftranslate = ftranslate + letter

    return ftranslate

print(translate(input("Enter a phrase for translation: ")))