
def get_words():
    with open('words.txt') as f:
        return f.read().split()


class Letter:
    def __init__(self, character, is_present, index=-1, is_at_index=False):
        self.character = character
        self.index = index
        self.is_present = is_present
        self.is_at_index = is_at_index


class MissingLetter(Letter):
    def __init__(self, character):
        super().__init__(character, is_present=False)


class GreenLetter(Letter):
    def __init__(self, character, index):
        super().__init__(character, True, index, True)


class YellowLetter(Letter):
    def __init__(self, character, index):
        super().__init__(character, True, index, False)


def check_letter_for_word(letter, word):
    if letter.is_present:
        if letter.is_at_index:
            return word[letter.index] == letter.character
        else:
            return letter.character in word and word[letter.index] != letter.character
    else:
        return letter.character not in word


def check_word(letters, word):
    return all(check_letter_for_word(letter, word) for letter in letters)


def filter_letters(letters, words):
    return [word for word in words if check_word(letters, word)]


def interact(letters, words):
    response = input('Tell me what you know. -h for help: ')
    if response == '-f':
        print(filter_letters(letters, words))
    elif response == '-h':
        print("""Here is how this works:
        Type in -f to filter words based on the input.
        Type in -h for help (obviously, that's how you got here.
        Type in -q to quite.
        Otherwise you will enter a comma delimited list of instructions. 
            An instruction for a Green letter looks like this: 'G[the letter][the index you found it]
            An instruction for a Yellow letter looks like this: 'Y[the letter][the index you found it] 
            An instruction for a Grey, or missing letter, just type in the letter: [the letter]
        for example, instructions might look like this: Ya1,Gt2,Ge3,Gr4,b,o,u,w""")
    elif response == '-q':
        print('Goodbye!')
    else:
        for tr in response.split(','):
            r = tr.replace(' ', '')
            try:
                if r[0] == 'G':
                    letters.append(GreenLetter(r[1].lower(), int(r[2])))
                elif r[0] == 'Y':
                    letters.append(YellowLetter(r[1].lower(), int(r[2])))
                else:
                    letters.append(MissingLetter(r[0].lower()))
            except:
                print('misconfigured input. -h for instructions')
    if response != '-q':
        interact(letters, words)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    words = get_words()
    interact([], words)

    #test input: Ga1,Gt2,Ge3,Gr4,b,o,u,w
