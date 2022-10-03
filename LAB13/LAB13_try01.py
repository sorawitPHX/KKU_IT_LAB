store_type = {1: 'Sedan', 2: 'Van', 3: 'Truck'}

def addVehic():
    user_id = input('Enter vehicle id: ')
    user_type = int(input('Enter vehicle type [1:Sedan, 2:Van, 3:Truck]: '))
    select_type = store_type[user_type]
    file = open('vehicle.txt', 'a+')
    file.writelines(f'{user_id} - {select_type}\n')
    file.close()
        
        
def showVehic():
    file = open('vehicle.txt', 'r')
    for line in file:
        line = line.replace('\n', '')
        v_id, v_type = line.split(' - ')
        print(f'{v_id} {v_type}')
    file.close()

            
def showVehicByType():
    pass


def main():
    def showMenu():
        print('''
          #### Select Menu ####
          1. Add vehicle
          2. Show vehicle
          3. Show vehicle by type
          4. Exit
          ''')
    menu = {1: addVehic,
            2: showVehic,
            3: showVehicByType,
            4: exit}
    while True:
        showMenu()
        select = int(input('Select menu number [1-4]: '))
        menu[ select ]()

#เรียกใช้ main
main()
