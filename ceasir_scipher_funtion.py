alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')','-', '_',
                      '=', '+', '[', ']', '{', '}', '|',';', ':', "'", '"', ',', '<', '.', '>', '/', '?','`', '~']
numbers_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def ceaser_encode(message, shift):
    encode_message_string = ""
    for i in message:
        if i == " ":
            encode_message_string += " "
        elif i in numbers_characters:
            position_character = numbers_characters.index(i)
            encode_message_string += numbers_characters[(position_character + shift) % len(numbers_characters)]

        elif i in special_characters:
            position_special = special_characters.index(i)
            encode_message_string += special_characters[(position_special + shift) % len(special_characters)]
        else:
            positon = alphabets.index(i)
            encode_message_string += alphabets[(positon + shift) %len(alphabets)]
    return encode_message_string


def ceaser_decode(message, shift):
    decode_message_string = ""
    for i in message:
        if i == " ":
            decode_message_string += " "
        elif i in numbers_characters:
            position_character = numbers_characters.index(i)
            decode_message_string += numbers_characters[(position_character - shift) % len(numbers_characters)]
        elif i in special_characters:
            position_special = special_characters.index(i)
            decode_message_string += special_characters[(position_special - shift) % len(special_characters)]
        else:
            positon = alphabets.index(i)
            decode_message_string += alphabets[(positon - shift) % len(alphabets)]
    return decode_message_string



while True:
    user_choice = input("type 'encode' for encode and type 'decode' for decode  :").lower()
    if user_choice =='decode' or user_choice == 'encode':
        user_message = input("Enter the message:").lower()
        shift_position = int(input("how much you want to shift:"))
    else:
        print("Please choose decode or encode")

    if user_choice == 'encode':
        print(ceaser_encode(message=user_message, shift=shift_position))
    elif user_choice == 'decode':
        print(ceaser_decode(message=user_message, shift=shift_position))
    user_continue = input("Do you want to continue : 'yes' or 'no':").lower()
    if user_continue == "no":
        print("Game stopped")
        break
    elif user_continue =="yes":
        pass
    else:
        print("#404 due to the non valid input ")
