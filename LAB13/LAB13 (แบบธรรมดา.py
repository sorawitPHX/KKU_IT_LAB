store_type = {1: 'Sedan', 2: 'Van', 3: 'Truck'}
file = open('vehicle.txt', 'a+')

def addVehic():
    user_id = input('Enter vehicle id: ')
    user_type = int(input('Enter vehicle type [1:Sedan, 2:Van, 3:Truck]: '))
    select_type = store_type[user_type]
    file.write(f'{user_id} {select_type}\n')

def showVehic():
    if file.tell() == 0:
        print('-- No data --')
    else:
        file.seek(0, 0)
        for line in file:
            line = line.replace('\n', '')
            v_id, v_type = line.split(' ')
            print(f'{v_id} {v_type}')
        file.seek(0, 0)
        count = len( file.readlines() )
        print(f'The number of vehicle {count}')

def showVehicByType():
    if file.tell() == 0:
        print('-- No data --')
    else:
        user_type = int(input('Enter vehicle type [1:Sedan, 2:Van, 3:Truck]: '))
        select = store_type[ user_type ]
        c = 0
        file.seek(0)
        for line in file:
            line = line.replace('\n', '')
            v_id, v_type = line.split(' ')
            if select == v_type:
                c += 1
                print(f'ID: {v_id}')
        if c > 0:
            print(f'The number of vehicle {c}')
        else:
            print('-- No data --')

def Exit():
    file.close()
    exit()
    
def mainmenu():
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
            4: Exit}
    while True:
        showMenu()
        select = int(input('Select menu number [1-4]: '))
        menu[ select ]()
        input('กด Enter เพื่อดำเนินการต่อ...')

#เรียกใช้ main
mainmenu()