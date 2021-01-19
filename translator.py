def translate(phrase):
    translaton = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translaton =translaton + "G"
            else:
                translaton = translaton + "g"

        else:
            translaton = translaton + letter
    return translaton

print(translate(input("Enter a phrase: ")))