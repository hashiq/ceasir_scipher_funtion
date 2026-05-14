alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
run_loop = True
while run_loop:
    user_choice = input("type 'decode' for decode and type 'encode' for encode :").lower()
    user_message = input("Enter the secret message:").lower()
    shift_position = int(input("how much you want to shift:"))
    if user_choice == 'decode':
        def ceaser_decode(message,shift):
            decode_message_string = ""
            for i in message:
                positon = alphabets.index(i)
                decode_message_string += alphabets[(positon + shift_position) % 26]
            return decode_message_string
        print(ceaser_decode(message=user_message, shift=shift_position))
    elif user_choice == 'encode':
        def ceaser_encode(message,shift):
            encode_message_string = ""
            for i in message:
                positon = alphabets.index(i)
                encode_message_string += alphabets[(positon - shift_position) % 26]
            return encode_message_string
        print(ceaser_encode(message=user_message, shift=shift_position))
    user_continue = input("Do you want to continue : 'yes' or 'no':").lower()
    if user_continue == "no":
        run_loop =False
    elif user_continue == "yes":
        run_loop= True
    else:
        print("#404")
