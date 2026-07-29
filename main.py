import random
import string

def main():
    length = get_length()
    characters = choose_character_set()
    password = generate_password(length,characters)

    print("Password length:", length)
  
    display_password (password)


def display_password(password):
    print("\nGenerated Password:", password)


        
    
def get_length():

    while True :

         print("\n1) 4 character password")
         print("2) 8 character password")
         print("3) 12 character password")

         choice = input(">")

         if choice == "1" :
             return 4
         elif choice == "2" :
             return 8
         elif choice == "3":
             return 12
         else :
             return ("Invalid choice")


def choose_character_set():
      
    characters = string.ascii_letters

   
    number = input("Include numbers? (y/n): ").lower()

    if number == "y":
        characters += string.digits

    symbols = input("Include symbols? (y/n): ").lower()

    if symbols == "y":
        characters += string.punctuation

    return characters

def generate_password(length, characters):
    password = ""

    for i in range(length):
        password += random.choice(characters)
    return password


if __name__ == "__main__":
    main()