# twttr.py
def main():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    shortened_words = [shorten(word) for word in words]
    print(' '.join(shortened_words))

def shorten(word):
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in word if char not in vowels])

if __name__ == "__main__":
    main()
