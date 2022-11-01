alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
            "U", "V", "W", "X", "Y", "Z"]


def char_position(p_position, p_cypher_type):
    if p_cypher_type == "E":
        while p_position > len(alphabet) - 1:
            p_position -= len(alphabet)
    else:
        while p_position < 0:
            p_position += len(alphabet)
    return p_position


def cypher(p_message, p_shift, p_cypher_type):
    result = ""
    if p_cypher_type == "D":
        p_shift *= -1
    for char in p_message:
        if char in alphabet:
            position = alphabet.index(char)
            cypher_position = position + p_shift
            cypher_position = char_position(cypher_position, p_cypher_type)
            result += alphabet[cypher_position]
        else:
            result += char
    print(f"Here is the {'decode' if p_cypher_type == 'D' else 'encode'}d result: {result}")


def encrypt_decrypt():
    restart_program = False
    while not restart_program:
        user_choice = input("Type 'E' for encrypt or 'D' for decrypt")
        message = input("Enter your message: \n").upper()
        shift = int(input("Enter the shift number: \n"))
        cypher(message, shift, user_choice)
        restart = input("Type 'Y' for continue, or 'N' for quit\n")
        if restart == "N":
            restart_program = True
            print("See ya!!!")


encrypt_decrypt()
