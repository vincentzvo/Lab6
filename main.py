# encode method writen by Vincent Zvolsky
def encode(password):
    # initialized variables
    password_list = []
    encoded_password = ""

    # stores password as a list of integers
    for i in range(len(password)):
        password_list.append(int(password[i]))

    # loops through password list, shifting the integer at each index up by 3
    for i in range(len(password_list)):
        if password_list[i] < 7:
            password_list[i] += 3
        elif password_list[i] == 7:
            password_list[i] = 0
        elif password_list[i] == 8:
            password_list[i] = 1
        elif password_list[i] == 9:
            password_list[i] = 2

    # stores password list back to a string
    for i in range(len(password_list)):
        encoded_password += str(password_list[i])

    return encoded_password

# decode method writen by <VALERIA RUBIO>
def decode(encoded_password):
    result=''
    for digit in encoded_password:
        newdigit=(int(digit)-3)
        if newdigit < 0:
            newdigit=newdigit+10 #to wrap around when a negative is found, ie if 2, it will return 9
        result+=str(newdigit)
    return result











# main method writen by Vincent Zvolsky
if __name__ == "__main__":

    # loops menu until user inputs 3 to quit
    loop_menu = True
    while loop_menu == True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        # prompt/store user's menu option input
        menu_option = input("Please enter an option: ")

        # encode
        if menu_option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print()

        # decode
        elif menu_option == "2":
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password},"
                  f" and the original password is {decoded_password}.")
            print()

        # quit
        elif menu_option == "3":
            loop_menu = False
