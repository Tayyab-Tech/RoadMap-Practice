# Keep asking for a positive integer until the user enters one.
while True:
    try:
        number = int(input("Enter a positive integer: "))

        if number > 0:
            print("Valid Number:", number)
            break
        else:
            print("Number must be positive.")

    except ValueError:
        print("Please enter a valid integer.")





# Validate that an email contains @ and .
email = input("Enter email: ")

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")






# Validate that a product price is greater than 0
price = float(input("Enter product price: "))

if price > 0:
    print("Valid Price")
else:
    print("Invalid Price")




# Validate that a student's GPA is between 0.0 and 4.0
gpa = float(input("Enter GPA: "))

if 0.0 <= gpa <= 4.0:
    print("Valid GPA")
else:
    print("Invalid GPA")




# Validate that a filename ends with .txt
filename = input("Enter filename: ")

if filename.endswith(".txt"):
    print("Valid File")
else:
    print("Invalid File")

