# Main menu
print(f"Main Menu")
print(f"---------")
print(f"A. Junior Cat")
print(f"B. Prime Cat")
print(f"C. Cat age articles")
print(f"X. Exit Program")
print(f"---------")

option = input("Enter an option(A,B,C or X):")

# Input and Output for option A
if(option == "A" or option == "a"):
    print("Option A selected")
    cat_age = input("Choose Cat's age in months: 8, 12, 18 or 24:")
    if(cat_age == "8"):
        print(f"Human age is 11 years old.")
    elif(cat_age == "12"):
        print(f"Human age is 15 years old.")
    elif(cat_age == "18"):
        print(f"Human age is 21 years old.")
    elif(cat_age == "24"):
        print(f"Human age is 27 years old.")
    else:
        print(f"Invalid Cat Age!")
    exit()
# Input and Output for option B
elif(option == "B" or option == "b"):
    print(f"Option B selected")
    cat_age = input("Choose Cat's age in years: 3, 4, 5 or 6:")
    if(cat_age == "3"):
        print(f"Human age is 28 years old.")
    elif(cat_age == "4"):
        print(f"Human age is 32 years old.")
    elif(cat_age == "5"):
        print(f"Human age is 36 years old.")
    elif(cat_age == "6"):
        print(f"Human age is 40 years old.")
    else:
        print(f"Invalid Cat Age!")
    exit()
# Output for option C:
elif(option == "C" or option == "c"):
    print(f"Option C selected")
    print()
    print(f"Cat-age calculators estimate a cat’s age in human years, accounting for their faster aging in early years. Different calculators use varying formulas, so results may differ slightly. This is because cat aging doesn’t follow a strict human-equivalent timeline.")
    print()
    print(f"International Cat Care website link: https://icatcare.org/advice/how-to-tell-your-cats-age-in-human-years/")
    print()
    print(f"Pets WebMD website link: https://pets.webmd.com/cats/how-to-calculate-your-cats-age")
    exit()
# Exiting the progam
elif(option == "X" or option == "x"):
    print(f"Thank you and goodbye...")
    exit()
