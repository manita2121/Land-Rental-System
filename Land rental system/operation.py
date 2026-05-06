#iimporting datetime for current date and time
import datetime
#imporinf read and write also
import read
import write

#to validate the land ID 
def validation_of_LandID(dictionary):
    while True:
        try:
            land_id = int(input("Enter the ID of the land: "))
            if land_id < 1 or land_id > len(dictionary):
                print(" Invalid land ID.")
            else:
                return land_id
        except ValueError:
            print("Please input the Land ID available in table.” ")
#To check land availablity Status
def checkingStatus(landland, landID):
    if landland[landID][5].lower() == "available":
        print("The land is available for rent")
        return True
    else:
        print(" Land is not available for rent at the moment.Please, Choose another land.")
        return False
#to generate bill of rentnd land
def bill_of_Rentedland(name, rented_lands):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = "Land's Rent Bill " + name + " " + current_time + ".txt"
    with open(file_name, "w") as file:
        file.write("_" * 90 + "\n")
        file.write("Address: Kamaladi, Kathmandu      The TechnoPropertyNepal        Phone: [9847730084]"+"\n")
        file.write("                               System Manager:Manita Basnet   "+"\n"   )
        file.write("_" * 90 + "\n")
        file.write("\n                                     Rented Land Bill\n")
        file.write("_" * 90 + "\n")
        file.write("Name of the Customer: " + name + "\n")
        file.write("Date and Time of Renting: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        total_rent = 0
        for land_id, duration, rent in rented_lands:
            details = read.return_land_details()[land_id]
            file.write("Land ID: " + str(land_id) + "\n")
            file.write("Kitta Number: " + details[0] + "\n")
            file.write("District: " + details[1] + "\n")
            file.write("Direction: " + details[2] + "\n")
            file.write("Aana: " + details[3] + "\n")
            file.write("Actual Rent Price: " + details[4] + "\n")
            file.write("Duration of Renting: " + str(duration) + " months\n")
            file.write("Rent for " + str(duration) + " months: " + str(rent) + "\n")
            total_rent += rent
            file.write("_" * 90 + "\n")
           
            print("_" * 148 + "\n")
            print("Address: Kamaladi, Kathmandu\t\t\t\t\t The TechnoPropertyNepal\t\t\t        Phone: [9847730084]")
            print("                                                             System Manager:Manita Basnet      ")
            print("_" * 148 + "\n")
            print("\n                  Rented Land Bill\n")
            print("\nRented Land ID:", land_id)
            print("Kitta Number:", details[0])
            print("District:", details[1])
            print("Direction:", details[2])
            print("Aana:", details[3])
            print("Actual Rent Price:", details[4])
            print("Duration of Renting:", duration, "months")
            print("Rent for", duration, "months:", rent)
            print("\n")
        file.write("\nTotal Rent: " + str(total_rent) + "\n")
        # Print total rent to console
        print("\nTotal Rent:", total_rent)
    print("\nThe bill is printed in the file:", file_name)
 
 #to generate bill of returnelands
def bill_of_returnlands(name, returned_lands):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = "Land Return Bill_" + name + "_" + current_time + ".txt"
    with open(file_name, "w") as file:
        file.write("_" * 90 + "\n")
        file.write("Address: Kamaladi, Kathmandu      The TechnoPropertyNepal        Phone: [9847730084]" + "\n")
        file.write("                               System Manager:Manita Basnet   " + "\n")
        file.write("_" * 90 + "\n")
        file.write("\n                                     Returned Land Bill\n")
        file.write("_" * 90 + "\n")
        file.write("Name of the Customer: " + name + "\n")
        file.write("Date and Time of Return: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        file.write("\nReturned Land Details:\n")
        total_fine = 0
        for land_details in returned_lands:
            file.write("_" * 90 + "\n")
            file.write("Kitta Number: " + land_details[0] + "\n")
            file.write("District: " + land_details[1] + "\n")
            file.write("Direction: " + land_details[2] + "\n")
            file.write("Aana: " + land_details[3] + "\n")
            file.write("Availability: " + land_details[5] + "\n")
            file.write("Fine: " + str(land_details[6]) + "\n")
            total_fine += land_details[6]
        file.write("_" * 90 + "\n")
        file.write("Total Fine: " + str(total_fine) + "\n")
        #to print in console
    print("_" * 148 + "\n")
    print("Address: Kamaladi, Kathmandu\t\t\t\t\t The TechnoPropertyNepal\t\t\t        Phone: [9847730084]")
    print("                                                             System Manager:Manita Basnet      ")
    print("_" * 148 + "\n")

    print("\n                  Returned Land Bill\n")
    print("_" * 180)
    print("Name of the Customer:", name)
    print("Date and Time of Return:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("\nReturned Land Details:")
    for land_details in returned_lands:
        print("Kitta Number:", land_details[0])
        print("District:", land_details[1])
        print("Direction:", land_details[2])
        print("Aana:", land_details[3])
        print("Availability:", land_details[5])
        print("Fine:", land_details[6])
        print("\n")
    print("\nTotal Fine:", total_fine)
    print("\nThe return bill is printed in the file:", file_name)

#to rent land
def rentland():
    while True:
        rented_lands = []  
        while True:
            landland = read.return_land_details()
            landID = validation_of_LandID(landland)

            if checkingStatus(landland, landID):
                while True:
                    ask = input("Would you like to rent the land? (yes/no): ").lower()
                    if ask == "yes":
                        name = input("Enter your Name: ")
                        address = input("Enter your Address: ")
                        email = input("Enter your Email: ")
                        while True:
                            try:
                                landland[landID][5] = "Not Available"
                                write.update_land(landland)
                                duration = int(input("Enter the duration you want to rent the land (in months): "))
                                if duration <= 0:
                                    print("Duration must be greater than 0 Months.")
                                else:
                                   
                                    price = int(landland[landID][-2])
                                    rent = price * duration
                                    print("Rent for", duration, "months:", rent)
                                    rent_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                    print("Date and Time of Renting:", rent_date_time)

                                    
                                    rented_lands.append((landID, duration, rent))
                                    break
                            except ValueError:
                                print("Invalid input. Please enter a valid integer for duration.")
                        break
                    elif ask == "no":
                        break
                    else:
                        print("Please answer with 'yes' or 'no'.")

                while True:
                    rent_another = input("Would you like to rent more land? (yes/no): ").lower()
                    if rent_another == "yes":
                        break
                    elif rent_another == "no":
                        bill_of_Rentedland(name, rented_lands) 
                        return  
                    else:
                        print("Please answer with 'yes' or 'no'.")
#to return land
def returnland():
    while True:
        returned_lands = []  
        while True:
            read.show_lands()
            landland = read.return_land_details()
            landID = validation_of_LandID(landland)  
            if landland[landID][5].lower() == "not available":
                while True:
                    ask = input("Would you like to return the land? (yes/no): ").lower()
                    if ask == "yes":
                        name = input("Enter your Name: ")
                        address = input("Enter your Address: ")
                        email = input("Enter your Email: ")

                        return_time = datetime.datetime.now()

                        rent_starttime_str = landland[landID][-1]
                        if rent_starttime_str != "Not Available":
                            rent_start_time = datetime.datetime.strptime(rent_starttime_str, "%Y-%m-%d %H:%M:%S")
                            rented_duration = (return_time - rent_start_time).days 
                            if rented_duration > int(landland[landID][-3]):
                                extra_duration = rented_duration - int(landland[landID][-3])
                                fine_percentage = 0.10
                                fine = extra_duration * int(landland[landID][-2]) * fine_percentage
                                print("Fine for exceeding rental duration:", fine)
                            else:
                                fine = 0
                        else:
                            fine = 0
                        landland[landID][5] = "Available"
                        write.update_returnland(landland)  
                        print("The land has been returned successfully.")
                        returned_land_details = [landland[landID][0], landland[landID][1], landland[landID][2], landland[landID][3], landland[landID][4], landland[landID][5], fine]
                        returned_lands.append(returned_land_details)

                        break 
                    elif ask == "no":
                        break
                    else:
                        print("Please answer with 'yes' or 'no'.")

                while True:
                    return_more = input("Would you like to return more lands? (yes/no): ").lower()
                    if return_more == "yes":
                        break
                    elif return_more == "no":
                        if returned_lands:
                            bill_of_returnlands(name, returned_lands)  # Generate return bill for all returned lands
                        return
                    else:
                        print("Please answer with 'yes' or 'no'.")
            else:
                print("This land is not currently rented. Please choose another land.")
