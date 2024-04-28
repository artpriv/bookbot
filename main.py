def main():
    report_book("frankenstein.txt")


def count_words(text: str) -> int:
    split = text.split()
    return len(split)


def count_letters(text: str) -> dict[str, int]:
    letter_count: dict[str, int] = {}
    for char in text.lower():
        if not ('a' <= char <= 'z'):
            continue
    
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

    return letter_count


def report_book(bookname: str) -> None:
    with open(f"./books/{bookname}", encoding="utf-8") as f:
        contents = f.read()

    word_count = count_words(contents)
    letter_dict = count_letters(contents)

    letter_count = [(letter, count) for letter, count in letter_dict.items()]
    letter_count.sort(key=lambda x: x[1], reverse=True)

    print(f" --- Begin report of books/{bookname} ---")
    print(f"{word_count} words found in the document")
    print()
    for letter, count in letter_count:
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")


main()