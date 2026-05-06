#importing fron other .py file
import operation
import read

#display fucntion to display greeting and welcome page
def display():
    #printing welcome message
    print("_" * 148 + "\n")
    a = input("Greeting from The Techno Property Nepal,Would you mind entering your name: ")
    print("_" * 148 +"\n")
    print("Address: Kamaladi, Kathmandu\t\t\t\t\t The TechnoPropertyNepal\t\t\t        Phone: [9847730084]")
    print("                                                             System Manager:Manita Basnet      ")
    print("_" * 148 + "\n")
    print("                                                Namaskar " + a + " ji, Welcome to The Techno Property Nepal!")
    print("_" * 148 + "\n")

#press function is created  to ask user what they want in the system
def press():
    print("Press 1 to Display Land")
    print("Press 2 to  Rent Land")
    print("Press 3 to Return Land")
    print("Press 4  to Exit the system")
    
#exit message
def exit():
    print("_" * 179 + "\n")
    print("Thank you for using The Techno Property Nepal's System")
    print("_" * 179 + "\n")

display()#calling display function to show display message
while True:#condition
    press()
    option = input("Please!Press as per your choice : ")
    if option == "1":
        read.show_lands()  #calling show_lands from read.py   
    elif option == "2":
        operation.rentland()#calling rentland from operation.py
        read.show_lands() #calling show_lands from read.py  
    elif option == "3":
        operation.returnland()#calling returnland from operation.py
    elif option == "4":
        exit()#calling exit function
        break
    else:# If user inputs an invalid option, Alert message is displayed.
        print("Alert!Please press 1 or 2 or 3 or 4 only:")