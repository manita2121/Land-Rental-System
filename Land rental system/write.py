#function to update rentland
def update_land(dictionary):
    file = open("land.txt", "w")
    for values in dictionary.values():
        file.write(str(values[0]) + "," + str(values[1]) + "," + str(values[2]) + "," + str(values[3]) + "," + str(values[4]) + "," + str(values[5]) + "\n")
    file.close()
#function to update return land
def update_returnland(dictionary):
    file = open("land.txt", "w")
    for values in dictionary.values():
        file.write(str(values[0]) + "," + str(values[1]) + "," + str(values[2]) + "," + str(values[3]) + "," + str(values[4]) + "," + str(values[5]) + "\n")
    file.close()