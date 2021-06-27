

def num_to_word(word):
    text_word_dict = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
                      6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    new_word = ''
    for i in range(len(word)):
        try:
            new_word += text_word_dict[int(word[i])]
        except ValueError:
            new_word += word[i]
    return new_word



def encrypt(plain_text, key):

    plain_text = num_to_word(plain_text)
    encrypted = ""

    for c in plain_text:

        if c.isupper(): #check if it's an uppercase character

            c_index = ord(c) - ord('A')

            # shift the current character by key positions
            c_shifted = (c_index + key) % 26 + ord('A')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.islower(): #check if its a lowecase character

            # subtract the unicode of 'a' to get index in [0-25) range
            c_index = ord(c) - ord('a')

            c_shifted = (c_index + key) % 26 + ord('a')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.isdigit():

            # if it's a number,shift its actual value
            c_new = (int(c) + key) % 10

            encrypted += str(c_new)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            encrypted += c

    return encrypted



def word_to_num(phrase):
    word_text_dict = {'Zero': 0, 'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,
                      'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'OneOne': 11, 'OneTwo': 12,
                      'OneThree': 13, 'OneFour': 14, 'OneFive': 15, 'OneSix': 16, 'OneSeven': 17, 'OneEight': 18,
                      'OneNine': 19, 'TwoZero': 20, 'TwoOne': 21, 'TwoTwo': 22, 'TwoThree': 23, 'TwoFour': 24,
                      'TwoFive': 25, 'TwoSix': 26}
    try:
        split_phrase = phrase.split()
        new_word = split_phrase[0] + ' {}'.format(str(word_text_dict[split_phrase[1]]))
    except KeyError:
        return False
    return new_word

def decrypt(ciphertext, key):

    decrypted = ""

    for c in ciphertext:

        if c.isupper():

            c_index = ord(c) - ord('A')

            # shift the current character to left by key positions to get its original position
            c_og_pos = (c_index - key) % 26 + ord('A')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.islower():

            c_index = ord(c) - ord('a')

            c_og_pos = (c_index - key) % 26 + ord('a')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.isdigit():

            # if it's a number,shift its actual value
            c_og = (int(c) - key) % 10

            decrypted += str(c_og)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            decrypted += c

    new_word = word_to_num(decrypted)
    return new_word




if __name__ == '__main__':
    text = "medium 300"
    s = 5
    encrypt_text = encrypt(text, s)
    print(encrypt_text)
    # decrypt_text = decrypt(encrypt_text, s)
    # print(decrypt_text)

