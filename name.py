def fullname(first_name,last_name): #creating fullname function
    z=first_name + " " + last_name #joining two varaibles
    return z
def string_alternative(x): #creating another function for method printing alternate characters in the string
    return x[::2]

user_name=str(input("enter the first name:")) #taking the first name from the user
user_name2=str(input("enter the last name:")) #taking the last name from the user
user_full_name = fullname(user_name, user_name2) #passing the variables to the fullname method


print(user_full_name)

def main(): #creating the main function
    alterstring = string_alternative(user_full_name) #calling the string_alternative method
    print(alterstring)

if __name__ == '__main__': #calling the main function
    main()

