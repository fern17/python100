import string

alphabet = list(string.ascii_letters)

# of course these two could be merged in only one function with an additional parameter: operation [encode, decode]
def encode(message, shift):
    encoded_message = []
    for c in range(0, len(message)):
        i = alphabet.index(message[c])
        ce = alphabet[(i + shift) % len(alphabet)]
        encoded_message.append(ce)
    return encoded_message

def decode(message, shift):
    decoded_message = []
    for c in range(0, len(message)):
        i = alphabet.index(message[c])
        ce = alphabet[(len(alphabet) + i - shift) % len(alphabet)]
        decoded_message.append(ce)
    return decoded_message


print("Welcome to Caesar Cypher\n")
operation = input("Type \'encode\' to encrypt, type \'decode\' to decrypt: ")
if operation == "encode":
    message = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    encoded_message = "".join(encode(message, shift))
    print(f"Encoded message: {encoded_message}")
elif operation == "decode":
    message = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    decoded_message = "".join(decode(message, shift))
    print(f"Decoded message: {decoded_message}")
else:
    print("Unknown operation")