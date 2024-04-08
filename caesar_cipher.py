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
            
            print(f"Encrypted text: {caesar_cipher_encrypt(plain_text, shift)}")


        elif enc_or_dec == 1:
            cipher_text = input("Enter your text to decrypt: ")

            while True:
                shift = input("Enter your shift amount as an integer (positive for right shift and negative for left shift): ")
                if is_int(shift):
                    shift = int(shift)
                    break
                else:
                    print("Invalid input, try again.")
            
            print(f"Decrypted text: {caesar_cipher_decrypt(cipher_text, shift)}")
        else:
            print("Invalid input, try again.")

        cont = input("Enter 'y' to run the program again or any other key to quit: ")

        if cont == 'y' or cont == 'Y':
            continue
        else:
            break

    return 0



def caesar_cipher_encrypt(text: str, shift: int) -> list[int]:
    ascii_list = string_to_ascii(text)

    for i in range(len(ascii_list)):
        ascii_list[i] += shift

    return ascii_to_string(ascii_list)

def caesar_cipher_decrypt(cipher: str, shift: int) -> list[int]:
    ascii_list = string_to_ascii(cipher)

    for i in range(len(ascii_list)):
        ascii_list[i] -= shift

    return ascii_to_string(ascii_list)


def string_to_ascii(text):
    ascii_codes = []

    for char in text: 
        ascii_codes.append(ord(char))

    return ascii_codes

def ascii_to_string(ascii_list):
    text = ""

    for code in ascii_list:
        text += chr(code)
    
    return text

def is_int(int_input):
    try:
        int(int_input)
        return True
    except ValueError:
        return False



driver()









