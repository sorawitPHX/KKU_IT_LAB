###############################################
# ถ้าหาก Run ไม่ได้ให้ไปลองรันที่ Python IDLE นะครับ #
###############################################

all_product = []
try:
    # คำสั่งที่สุ่มเสี่ยงจะเกิด Error
    f = open('sales.txt', mode='r')
except FileNotFoundError:
    # ถ้าเกิด Error จะทำการรันคำสั่งในนี้
    # ปล. (FileNotFoundError) คือ ข้อผิดพลาดเกี่ยวกับการหาไฟล์ไม่เจอ
    print('Cannot open "sales.txt"')
else:
    # ถ้าไม่เกิด Error โปรแกรมจะมาทำในนี้ต่อ
    
    # ส่วนที่ 1
    # คัดกรองข้อมูล
    count = 0
    for line in f:
        count += 1
        # โปรแกรมจะเริ่มทำงานใน loop ครั้งที่ 2 
        # เพราะใน loop ครั้งแรกเป็นการดึงข้อความในไฟล์ที่เป็นแค่ column ไม่ได้ข้อมูลที่จะเอามาคำนวณแต่อย่างใด
        # ดังนั้นจึงใช้ count เช็คว่าโปรแกรม loop ไปกี่รอบแล้ว 
        if count != 1: # จึงได้ว่าาา ถ้า loop รอบแรกไม่ต้องทำงานคำสั่งในนี้
            try:
                line = line.replace('\n', '')
                receipt, product, unit, quanlity = line.split(', ')
                unit, quanlity = int(unit), int(quanlity)
                assert ( (unit > 0) and (quanlity > 0) ), f'Check data at line {count} [{line}]'
            except ValueError:
                print(f'At line {count} an invalid data is found, and it was skipped. [{line}]')
            else:
                all_product.append([receipt, product, unit, quanlity])
    
    # ส่วนที่ 2
    # คำนวณข้อมูล
    product_dict = {}
    for receipt, product, unit, quanlity in all_product:
        if product not in product_dict:
            product_dict[ product ] = [unit, quanlity]
        else:
            product_dict[ product ][1] += quanlity
    total_all_product_sold = 0
    total_all_product_price = 0
    output = ''
    for k, v in product_dict.items():
        total_all_product_sold += v[1]
        total_all_product_price += v[0]*v[1]
        output += f'{k} x {v[1]} x {v[0]} bath = {v[0]*v[1]} bath\n'
    
    # ส่วนที่ 3
    # แสดงผลข้อมูลออกทางหน้าจอ
    print(f'The data in file contains {len(all_product)} orders.')
    print('='*30)
    print(f'Product were sold {total_all_product_sold} items.')
    print(output[:-1])
    print('='*30)
    print(f'Total sales {total_all_product_price} bath.')