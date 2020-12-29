repeater = 5
while repeater < 10:
    # -*- coding: utf-8 -*-


    def encrypt(text, interval):
            encrypt_text = ''
            for char in text:
                    encrypt_char = chr(ord(char) + interval)
                    encrypt_text += encrypt_char
            return encrypt_text


    def decrypt(text, interval):
            decrypt_text = ''
            for char in text:
                    decrypt_char = chr(ord(char) - interval)
                    decrypt_text += decrypt_char
            return decrypt_text


    def main():
            print('1 - Encrypt Text\n2 - Decrypt Text')
            choose = input('Mode: ')

            if choose == '1':
                    text = input('Text: ')
                    interval = int(input('Interval: '))
                    print(encrypt(text, interval))

            elif choose == '2':
                    text = input('Text: ')
                    interval = int(input('Interval: '))
                    print(decrypt(text, interval))
		
            else:
                    print('ERROR: Wrong Mode!')


    if __name__ == '__main__':
            main()
