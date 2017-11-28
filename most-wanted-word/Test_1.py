import collections
def checkio(text):
    text = sorted(text.lower())
    text = ''.join(x for x in text if str(x).isalpha())
    most_common = collections.Counter(text).most_common()
    most_common_sorted = sorted(most_common, key=lambda x: (-x[1], x[0]))
    return most_common_sorted[0][0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
