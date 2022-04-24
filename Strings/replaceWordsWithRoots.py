# Given a sentence and a list of roots, replace all words the cotain the roots with the roots

def replace_words(sentence, roots):
    # Remove duplicates roots
    rootset = set(roots)

    def replace(word):
        # iterates through the length of the word, checking after each letter to see if it is in the rootset
        # If it is in the rootset, return the root (word[:i]), if it gets through the length of the word, just return the word.
        for i in range(len(word)):
            if word[:i] in rootset:
                return word[:i]
        return word
# This line below takes a list (an iterable), maps a function to it, then makes it into a string seperated by a space (" ")
    return " ".join(list(map(replace, sentence.split())))

print(replace_words('I really wanted to go back to the land of running because I never enjoyed it here',['want', 'run', 'enjoy']))


