# Various alternative text encodings (e.g. Morse, braille, etc.)

def braille_translator():
    """
    Interactive braille translator

    Launches an interactive interpreter for braille.
    """
    braille_alphabet = {
        (1,): 'A',
        (1,2): 'B',
        (1,4): 'C',
        (1,4,5): 'D',
        (1,5): 'E',
        (1,2,4): 'F',
        (1,2,4,5): 'G',
        (1,2,5): 'H',
        (2,4): 'I',
        (2,4,5): 'J',
        (1,3): 'K',
        (1,2,3): 'L',
        (1,3,4): 'M',
        (1,3,4,5): 'N',
        (1,3,5): 'O',
        (1,2,3,4): 'P',
        (1,2,3,4,5): 'Q',
        (1,2,3,5): 'R',
        (2,3,4): 'S',
        (2,3,4,5): 'T',
        (1,3,6): 'U',
        (1,2,3,6): 'V',
        (2,4,5,6): 'W',
        (1,3,4,6): 'X',
        (1,3,4,5,6): 'Y',
        (1,3,5,6): 'Z'
    }
    # Input using uijkm, (right-hand home row)
    uijk_input_str = 'ujmik,'
    erdf_input_str = 'edcrfv'

    input_history = ''

    print('Interactive Braille Translator')
    print('Use "uijkm," or "erdfcv" to input a braille character.')
    print('[Enter] to quit.')

    while True:
        usr_input = input('>>> ')
        if usr_input == '':
            break 
        
        if usr_input[0] in uijk_input_str:
            try:
                num_repr = sorted([uijk_input_str.index(i) + 1 for i in usr_input])
            except ValueError as e:
                print('\tDetected uijk input format, but received invalid input')
                continue
        elif usr_input[0] in erdf_input_str:
            try:
                num_repr = sorted([erdf_input_str.index(i) + 1 for i in usr_input])
            except ValueError as e:
                print('\tDetected erdf input format, but received invalid input')
                continue
        else:
            print('\tInvalid input character. Could not detect input format')
            continue
        try:
            letter = braille_alphabet[tuple(num_repr)]
        except KeyError:
            print('\tInvalid braille pattern.')
            continue
        input_history += letter
        print('\tLetter: ' + letter)
        print('\tHistory: ' + input_history)

if __name__ == "__main__":
    braille_translator()