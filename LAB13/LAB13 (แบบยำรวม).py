#หัวจะปวดดด
import os

#Menu1
def addVehicle():
    store_type = {'1': 'Sedan',
                  '2': 'Van',
                  '3': 'Truck'}
    
    while True: #Input and Error Check
        try:
            user_vehic_id = input('Enter vehicle id: ').replace(' ', '')
            if user_vehic_id.isspace() or user_vehic_id == str(): raise
            user_type = input('Enter type of vehicle [1:Sedan, 2:Van, 3:Truck]: ')
            if user_type not in store_type.keys(): raise
        except:
            print('-- Invalid Try again -- ')
            continue
        else: break
    
    user_type = store_type[user_type]
    with open('vehicle.txt', mode='a') as file: #Apeend Text to File(vehicle.txt)
        car = f'{user_vehic_id} {user_type}\n'
        file.writelines(car)
    
    
#Menu2 And Menu3
def showVehicle(mode_show=0): 
    vehic_type = {'1': 'Sedan',
                  '2': 'Van',
                  '3': 'Truck'}
    
    with open('vehicle.txt', mode='r') as file: 
        file_copy = file.readlines()
        
    count = len(file_copy)
    if count != 0:
        if mode_show==0: # Menu2
            print(f'{"ID":20} {"Type"}')
            print('-'*25)
            for line in file_copy:
                line = line.replace('\n', '')
                d, t = line.split(' ')
                print(f'{d:20} {t:20}')
            print(f'The number of vehicle is: {count}') 
             
        elif mode_show==1: # Menu3
            count = 0
            while True:
                user_type = input('Enter type of vehicle [1:Sedan, 2:Van, 3:Truck]: ')
                if user_type not in vehic_type.keys() or user_type == '': 
                    print
                    continue
                else: break
            print('')
            user_type = vehic_type[user_type]
            for line in file_copy:
                line = line.replace('\n', '')
                d, t = line.split(' ')
                if t == user_type:
                    count += 1
                    print(f'ID: {d}')
            print(f'The number of vehicle is: {count}') if count != 0 else print(f'-- Not found data --')
    else:
        print(f'-- Not found data --')
              

#Menu4
def clearFile():
    with open('vehicle.txt', mode='w') as f:
        pass


#Main Menu        
def main(show_menu=1):
    def showMenu():
        print(f'''
            {' Select Menu ':#^23}
            1. Add Vehicle data
            2. Show all vehicle
            3. Show vehicle by type
            4. Clear file
            5. Exit
            ''')
        
    menu = {1: addVehicle,
            2: lambda : showVehicle(mode_show=0),
            3: lambda : showVehicle(mode_show=1),
            4: clearFile,
            5: exit}
    
    while True:
        if show_menu==1:
            showMenu()
        while True: #Input and Error Check
            try:
                user = int(input('Select menu number [1-5]: '))
                if user not in menu.keys(): raise Exception
            except ValueError:
                print('-- Please Input Number --')
                continue
            except Exception:
                print('-- Not in menu Please try again --')
                continue
            except:
                print('-- Invalid Input Try Again --')
                continue
            else: break
        print('')
        menu[user]()
        input('\nEnter to continue... ')
        os.system('cls')       
           

#ส่วน Main เรียกใช้ Function
if __name__ == '__main__':
    main()