#Connor Houghton
#30/09/14
#telling the user whether ater is frozen, boiling or neither

water_temp = int(input("please enter the temperature of the water: "))

if water_temp >= 100:
    print ("The water is boiling.")
elif water_temp <= 0:
    print("The water is frozen.")
else:
    print("The water is neither boiling or frozen.")
