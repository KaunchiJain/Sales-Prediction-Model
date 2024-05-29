import os
import webbrowser
choice = input("Choose the category for sales forecasting: \n1. Location \n2. Store \n3. Region\n ")
location=['L1','L2','L3','L4','L5']
region=['R1','R2','R3']
store=['S1','S2','S3','S4']   
locdict = {"L1": [10242.473622960486 , 13520.53723990161 , 182804927.25556624],
           "L2":[15433.59878593115 , 20642.76291054448 , 426123660.58095074],
           "L3":[8158.019792302034 , 10720.330010626263 , 114925475.53673409],
           "L4": [7016.536928487199 , 9176.00817467835 , 84199126.0217639],
           "L5":[6916.977443440596 , 8989.7767048963 , 80816085.20389618]} 
storedict = {"S4": [15485.596894601007,20750.002114982184, 430562587.77176505],
             "S3":[11235.522173634065 , 14907.164575749493 , 222223555.68848056], 
             "S1": [9293.13329077292 , 12303.08177750587 , 151365821.22399697],
             "S2":[6993.575434728554 , 9168.68074146217 , 84064706.53885931]}
regdict = {"R1":[16174.836187763278 , 21285.929101593338 , 453090777.7180582],
           "R2":[12389.862692369281 , 16468.46754720104 , 271210423.35321385],
           "R3":[12617.572095062265 , 16615.543092039592 , 276076272.2434246]
           "R4":[11999.81163508174 , 15930.185662734784 , 253770815.24920088]}
def show_graph(ch):
    temp=ch+"_Rolling.png"
    temp2=ch+"_Expo.png"
    os.startfile(temp)
    os.startfile(temp2)
    webbrowser.open('Gyaan.html') 
if choice == "Location":
    print("Choose from",location)
    subchoice = input()
    print("MAD:", locdict[subchoice][0], "\nVariance: ", locdict[subchoice][1],
          "\nStandard Deviation",locdict[subchoice][2])
    show_graph(subchoice)
elif choice == "Store":
    print("Choose from",store)
    subchoice = input()
    print("MAD:", storedict[subchoice][0], "\nVariance: ", storedict[subchoice][1],
          "\nStandard Deviation",storedict[subchoice][2])
    show_graph(subchoice)
elif choice == "Region":
    print("Choose from",region)
    subchoice = input()
    print("MAD:", regdict[subchoice][0], "\nVariance: ", regdict[subchoice][1],
          "\nStandard Deviation",regdict[subchoice][2])
    show_graph(subchoice)
else:
    print("Invalid Choice")

    