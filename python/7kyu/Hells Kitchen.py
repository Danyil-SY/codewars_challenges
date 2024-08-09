# Hells Kitchen

# Gordon Ramsay shouts. He shouts and swears. There may be something wrong with him.

# Anyway, you will be given a string of four words. Your job is to turn them in to Gordon language.

# Rules:

# Obviously the words should be Caps, Every word should end with '!!!!', Any letter 'a' or 'A' should become '@', Any other vowel should become '*'.

def gordon(a):
    a = ' '.join(list(map(lambda x: x.upper()+'!!!!', a.split(' '))))
    for letter in 'AEIOU':
        if letter == 'A':
            replacement = '@'
        else:
            replacement = '*'
        a = a.replace(letter, replacement)
    return a
