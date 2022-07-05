def encode(value, cipher_secret):
    value = list(map(ord, list(value)))
    for i in range(len(value)):
        value[i] = chr(value[i]+cipher_secret)
    
    print(f"Your encoded message is {''.join(value)}")

def decode(value, cipher_secret):
    value = list(map(ord, list(value)))
    for i in range(len(value)):
        value[i] = chr(value[i]-cipher_secret)
    
    print(f"Your dencoded message is {''.join(value)}")



while True:
    user_input = input("Type encode to 'encode' or 'decode' to decode:\n")
    value = input(f"Enter the message you want to {user_input}:\n")
    cipher_secret = int(input("Enter the cipher secret number:\n"))

    if user_input == 'encode':
        encode(value, cipher_secret)
    else:
        decode(value, cipher_secret)
    
    choice = input("Would you like to perform another operation? y/n: \n")
    if choice == 'n':
        break
    else:
        continue
