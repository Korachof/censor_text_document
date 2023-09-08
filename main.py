

def main():
    print("Hello. This program takes a text document and checks it for swear words. The options are below: \n"
          "1) Replace each swear word with the same number of asterisks (\"**** you, Bob!\") \n"
          "2) Replace each swear word with its less offensive version (\"I'm freaking tired\") \n"
          "3) Replace each swear word with a funny, less offensive version (\"You're a poop head\")")

    def choose_option():
        censor_option = input("Please type the corresponding number to your preferred option above. \n")

        if censor_option != "1" or censor_option != "2" or censor_option != "3":
            choose_option()

        correct_option = input("You selected" + censor_option + ". " + "Is that correct? Type Y for yes, and N for No")

        if correct_option.upper() == "N" or (correct_option.upper() != "Y" and correct_option.upper() != "N"):
            choose_option()

        return censor_option

    user_choice = choose_option()

    if user_choice == "1":
        print("You chose 1!")

    elif user_choice == "2":
        print("You chose 2!")

    else:
        print("You chose 3!")


main()