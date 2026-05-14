alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

user_choice = input("type 'decode' for decode and type 'encode' for encode :").lower()
user_message = input("Enter the secret message:").lower()
shift_position = int(input("how much you want to shift:"))
run_loop = True
while run_loop:
    user_continue = input("Do you want to continue : 'yes' or 'no'").lower()
    if user_choice == 'decode':
        def ceaser_decode(message, shift):
            decode_message_string = ""
            for i in message:
                positon = alphabets.index(i)
                decode_message_string += alphabets[(positon + shift_position) % 26]
            return decode_message_string
        print(ceaser_decode(message=user_message, shift=shift_position))
    elif user_choice == 'encode':
        def ceaser_encode(message, shift):
            encode_message_string = ""
            for i in message:
                positon = alphabets.index(i)
                encode_message_string += alphabets[(positon - shift_position) % 26]
            return encode_message_string
        print(ceaser_encode(message=user_message, shift=shift_position))
    #
    # if user_continue == "no":
    #     run_loop =False
    # elif run_loop == "yes":
    #     run_loop= True
    # else:
    #     print("Please enter a valid in put from yes or no ")
