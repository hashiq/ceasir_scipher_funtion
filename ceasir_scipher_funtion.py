alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

user_choice = input("type 'decode' for decode and type 'encode' for encode :")
user_message = input("Enter the secret message:")
shift_position = int(input("how much you want to shift:"))
decodes=[]
if user_choice == 'decode':
    def ceaser(message, shift):
        for i in message:
            orginal_message = alphabets.index(i)
            alphabets[orginal_message + shift_position]


decode_ = ceaser(message=user_message, shift=shift_position)
print(decode_)

