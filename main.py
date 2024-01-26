def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    report(text, book_path)


def report(text, book_path):
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    letters = []
    for char in chars_dict:
        if char.isalpha():
            letters.append(char)
    letters.sort()
    print(letters)
    for letter in letters:
        print(f"The '{letter}' character was found {chars_dict[letter]} times")
    print(f"--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
