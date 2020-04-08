import random
import string

#User details
def get_user_details(user_data):
    print("\n-----------------------------------------")
    print("\t   User Accounts")
    print("-----------------------------------------")
    for user in user_data:
        print(f"\nName:\t   {user['first_name']} {user['last_name']}\nEmail:\t   {user['email']}\nPassword:  {user['password']}")
    print("-----------------------------------------")

    return None


def generate_password(first_name, last_name):

    # generate 5 random characters

    characters = string.ascii_letters
    length = 5
    random_password = ''.join(random.choice(characters)for i in range(length))

    #add first two letters of Firstname and the last two letters of lastname
    password = str(first_name[:2] + random_password + last_name[-2:])

    return password

def get_user_password():
    while True:
        print("Enter a password of seven characters or more in length\n")
        password1 = input(": ")
        if len(password1) >= 7:
            print("Confirm password\n")
            password2 = input(": ")
            if password1 == password2:
                break
            print("Password does not match")
            continue
        print("Password must be seven characters or more in length")
        continue
    return password1


def user_registration():
    user_list = []
    while True:
        user_first_name = input("\nFirstname: ")
        user_last_name = input("Lastname: ")

        # make first letter of names uppercase and others lower

        first_name = (user_first_name[0].upper() + user_first_name[1:].lower()).strip()
        last_name = user_last_name[0].upper() + user_last_name[1:].lower()

        email = input("Email ").lower()

        temp_password = generate_password(first_name, last_name)
        user_choice = input(
            f"Do you like the generated password {temp_password} [y/N]  : "
        )
        if user_choice.lower() == "y":
            password = temp_password
        else:
            password = get_user_password()

        print(f"\nAccount for {first_name} {last_name} has been created successfully\n")
        user = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
        }
        user_list.append(user)
        add_again = input("Would you like to add another user? [y/N] : ")
        if add_again.lower() == "y":
            continue
        break
    return get_user_details(user_list)


def main():
    print("HNG Tech")
    print("Welcome, create new users")

    user_registration()


main()
			