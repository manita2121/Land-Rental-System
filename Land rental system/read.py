import datetime
#to return_land_details
def return_land_details():
    file = open("land.txt", "r")
    key = 1
    landland = {}
    for sth in file:
        sth= sth.replace("\n", "")
        final = sth.replace("\t", "")
        newList = final.split(",")
        landland[key] = newList
        key += 1
    file.close()
    return landland

#to show land
def show_lands():
    
    print("\n")
    print("-" * 122)
    print("|    ID  |" ," kitta_number |"  ,  "   District   |"  ,  "   Direction  |" ,  " Anna number  |"  ,"    Price     |","           Status             |")
    print("-" *122)
    landland = return_land_details()
    for kitta,details in landland.items():
        print ("|" ,kitta,"\t","|","\t",details[0],"\t","|",details[1],"\t","|","\t",details[2],"\t","|","\t",details[3],"\t","|",details[4],"\t","|","\t",details[5],"\t\t","|")
    print("-" * 122)