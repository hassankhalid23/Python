import random
import string

passwords = {}

#  Purana Data Load Karna
try:
    with open("pwd.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            passwords[website] = pwd
except:
    pass


#  Password Generator
def generate_password():
    chars = string.ascii_letters + string.digits + "@#$%^&*()"  # for random password
    password = "".join(random.choice(chars) for _ in range(8))
    return password


# { imp point------------------
# range(8): Loop ko 8 baar chalane ka order deta hai.
# for _ in range(8): Yeh loop 8 baar chalega.
# random.choice(chars): Har baar loop chalne par chars mein se 1 random character uthayega.
# "".join(...): Yeh un tamam 8 characters ko aapas mein
# bina kisi gap ("") ke jod (concatenate) kar ke ek single string bana dega.}


# ---------------------------------------------------------
# Main Loop (Dhyan dein: Baaki saara code is ke ANDAR hai)
while True:
    print("\n-------------Personal Password Manager-------------")
    print("1. Save Password")
    print("2. View Password")
    print("3. Generate Password")
    print("4. Exit")

    choice = input("\nEnter ur choice: ")

    if choice == "1":
        site = input("Enter the website url: ")
        pwd = input("Enter the password: ")
        passwords[site] = pwd

        with open("pwd.txt", "a") as file:
            file.write(f"{site}:{pwd}\n")

        print("SAVED !")

    elif choice == "2":
        if not passwords:
            print("No Data Found!")
        else:
            print("\n--- Saved Passwords ---")
            for site, pwd in passwords.items():
                print(f"{site} : {pwd}")

    elif choice == "3":
        print("Generated password is:", generate_password())

    elif choice == "4":
        print("oka ba bye...")
        break
    else:
        print("Invalid input")
