AllowedVehiclesList =  "cars.txt"
def printAuthorisedVehicle(v):
    print("The AutoCountry sales manager has authorized the purchase and sale of the following vehicles:")
    for v in cars:
        print(v)

def searchAuthorisedVehicle(cars):
    print('\033[1m' +"Please enter the full vehicle name."+'\033[0m')
    vname=input()
    if vname in cars:
        print(f'{vname} is an authorized vehicle')
    else:
        print(f'{vname} is not an authorized vehicle, if you received this in error please check the spelling and try again')
def addAuthorisedVehicle(car):
    cars=read_list_from_file(AllowedVehiclesList)
    cars.append(car)
    write_list_to_file(AllowedVehiclesList, cars)
    print('\033[1m' +'You have added "' + car+ '" as an authorised  vehicle.'+'\0')
    
def deleteAuthorisedVehicle(car):
    cars=read_list_from_file(AllowedVehiclesList)
    print('\033[1m' +'Are you sure you want to remove "'+car+'" from the Authorized Vehicles List?'+'\033[0m')
    ans=input()
    if ans=='yes':
        cars.remove(car)
        write_list_to_file(AllowedVehiclesList, cars)
        print('\033[1m' +'You have REMOVED "'+car+'" as an authorized vehicle'+'\033[0m')

    
def menu():
    print("*" * 32)
    print("Auto Country Vehicle Finder v0.5")
    print("*" * 32)
    print("Please Enter the following number below from the following menu:")
    print()

    print("1.PRINT all Authorized Vehicles")
    print("2.SEARCH for Authorized Vehicles")
    print("3.ADD Authorized Vehicle")
    print("4.DELETE Authorized Vehicle")
    print("5.Exit")
    print("*" * 32)
def read_list_from_file(file_path):
    
    with open(file_path, 'r') as file:
        content_list = file.read().splitlines()
    return content_list

def write_list_to_file(file_path, content_list):
   
    with open(file_path, 'w') as file:
        for item in content_list:
            file.write(f"{item}\n")
menu()
choice=int(input())
cars=[]
while choice >=1 and choice !=5:
    cars=read_list_from_file(AllowedVehiclesList)
    if choice==1:
         printAuthorisedVehicle(cars)
    
        
    elif(choice==2):
        searchAuthorisedVehicle(cars)
        
           
    elif(choice==3):
         print('\033[1m' +"Please enter the full Vehicle name you would like to add:"+'\033[0m')
         car=input()
         addAuthorisedVehicle(car)
         
    elif(choice==4):
         print('\033[1m' +'Please Enter the full Vehicle name you would like to REMOVE:'+'\033[0m')
         car=input()
         deleteAuthorisedVehicle(car)
         
    print(" ")
    menu()
    choice=int(input())
    
print("Thank you for using the AutoCountry Vehicle Finder,goodbye!") 
