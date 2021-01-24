# writed by alimp0401 and Pavel Ukilevich
MorseCode = {'А': '.-'}
# MorseCode['B'] = '-...'
# MorseCode['C'] = '-.-.'
# MorseCode['D'] = '-..'
# MorseCode['E'] = '.'
# MorseCode['F'] = '..-.'
# MorseCode['G'] = '--.'
# MorseCode['H'] = '....'
# MorseCode['I'] = '..'
# MorseCode['J'] = '.---'
# MorseCode['K'] = '-.-'
# MorseCode['L'] = '.-..'
# MorseCode['M'] = '--'
# MorseCode['N'] = '-.'
# MorseCode['O'] = '---'
# MorseCode['P'] = '.--.'
# MorseCode['Q'] = '--.-'
# MorseCode['R'] = '.-.'
# MorseCode['S'] = '...'
# MorseCode['T'] = '-'
# MorseCode['U'] = '..-'
# MorseCode['V'] = '...-'
# MorseCode['W'] = '.--'
# MorseCode['X'] = '-..-'
# MorseCode['Y'] = '-.--'
# MorseCode['Z'] = '--..'
MorseCode['.'] = '......'
MorseCode[','] = '.-.-.-'
MorseCode[':'] = '---...'
MorseCode[';'] = '-.-.-.'
MorseCode['('] = '-.--.'
MorseCode[')'] = '-.--.-'
MorseCode["'"] = '.----.'
MorseCode['"'] = '.-..-.'
MorseCode['-'] = '-....-'
MorseCode['/'] = '-..-.'
MorseCode['_'] = '..--.-'
MorseCode['?'] = '..--..'
MorseCode['!'] = '--..--'
MorseCode['+'] = '.-.-.'
MorseCode[' '] = '-...-'
MorseCode['Error'] = '........'
MorseCode['@'] = '.--.-.'
MorseCode['\n'] = '..-.-'
# MorseCode['А'] = '.-'
MorseCode['Б'] = '-...'
MorseCode['В'] = '.--'
MorseCode['Г'] = '--.'
MorseCode['Д'] = '-..'
MorseCode['Е'] = '.'
MorseCode['Ё'] = '.'
MorseCode['Ж'] = '...-'
MorseCode['З'] = '--..'
MorseCode['И'] = '..'
MorseCode['К'] = '-.-'
MorseCode['Л'] = '.-..'
MorseCode['М'] = '--'
MorseCode['Н'] = '-.'
MorseCode['О'] = '---'
MorseCode['П'] = '.--.'
MorseCode['Р'] = '.-.'
MorseCode['С'] = '...'
MorseCode['Т'] = '-'
MorseCode['У'] = '..-'
MorseCode['Ф'] = '..-.'
MorseCode['х'] = '....'
MorseCode['Ц'] = '-.-.'
MorseCode['Ч'] = '---.'
MorseCode['Ш'] = '----'
MorseCode['Щ'] = '--.-'
MorseCode['Ы'] = '-.--'
MorseCode['Ь'] = '-..-'
MorseCode['Ъ'] = '-..-'
MorseCode['Э'] = '..-..'
MorseCode['Ю'] = '..--'
MorseCode['Я'] = '.-.-'
MorseCode['1'] = '.----'
MorseCode['2'] = '..---'
MorseCode['3'] = '...--'
MorseCode['4'] = '....-'
MorseCode['5'] = '.....'
MorseCode['6'] = '-....'
MorseCode['7'] = '--...'
MorseCode['8'] = '---..'
MorseCode['9'] = '----.'
MorseCode['0'] = '-----'


def decode_from_morse(code):
    global MorseCode
    text = ""
    for code in code.split(" "):
        text += list(MorseCode.keys())[list(MorseCode.values()).index(code)]
    return text


def encode_to_morse(text):
    global MorseCode
    code = " ".join([MorseCode[letter] for letter in text.upper()])
    return code


def main():
    while True:
        command = input("напишите З для закодировки, Р для раскодировки или С, чтобы остановиться: ")
        if command == "З":
            code = encode_to_morse(input())
            print(code)
        elif command == "Р":
            text = decode_from_morse(input())
            print(text)
        else:
            break


main()
