import string

class Alphabet:

    def __init__(self, language, letters_str):
        self.lang = language
        self.letters = list(letters_str)


    def print(self):
        print(self.letters)


    def letters_num(self):
        len(self.letters)



class EngAlphabet(Alphabet):

    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)


    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return True
        return False


    def letters_num(self):
        return EngAlphabet.__letters_num


    @staticmethod
    def example():
        print(" Пример:\n they meet you by your clothes and see you off by your mind")


if __name__ == '__main__':
    eng_alphabet = EngAlphabet()
    eng_alphabet.print()
    print(eng_alphabet.letters_num())
    print(eng_alphabet.is_en_letter('F'))
    print(eng_alphabet.is_en_letter('Щ'))
    EngAlphabet.example()
