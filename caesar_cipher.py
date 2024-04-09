# Written by Adam Gill 4/8/24
# This program encrypts and decrypts text with a caesar shift, the shift amount which the user chooses (positive for right, negative for left)
# Just run the program, the instructions should be pretty clear and self explanatory
# I also tried to handle all the possible input errors that could occur
# This program only shifts letters of the alphabet, all other characters are left the same

def driver():
    intro = input("This is a simple caesar cipher program to encrypt and decrypt text. Press enter to continue ")
    
    while True:
        while True:
            enc_or_dec = input("Enter a '0' to encrypt text and a '1' to decrypt text: ")
            if is_int(enc_or_dec) and (enc_or_dec == '0' or enc_or_dec == '1'):
                break
            else:
                print("Invalid input, try again.")

        enc_or_dec = int(enc_or_dec)
        if enc_or_dec == 0:
            plain_text = input("Enter your text to encrypt: ")

            while True:
                shift = input("Enter your shift amount as an integer (positive for right shift and negative for left shift): ")
                if is_int(shift):
                    shift = int(shift)
                    break
                else:
                    print("Invalid input, try again.")
            
            print(f"Encrypted text: {caesar_cipher(plain_text, shift)}")


        elif enc_or_dec == 1:
            cipher_text = input("Enter your text to decrypt (simply enter the opposite of the shift used for encryption): ")

            while True:
                shift = input("Enter your shift amount as an integer (positive for right shift and negative for left shift): ")
                if is_int(shift):
                    shift = int(shift)
                    break
                else:
                    print("Invalid input, try again.")
            
            print(f"Decrypted text: {caesar_cipher(cipher_text, shift)}")
        else:
            print("Invalid input, try again.")

        cont = input("Enter 'y' to run the program again or any other key to quit: ")

        if cont == 'y' or cont == 'Y':
            continue
        else:
            break

    return 0



def caesar_cipher(text: str, shift: int) -> list[int]:
    res = ""

    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - offset + shift) % 26 + offset)
            res += shifted_char
        else:
            res += char
    return res


def is_int(int_input):
    try:
        int(int_input)
        return True
    except ValueError:
        return False



driver()









