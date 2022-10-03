def main():
    all_product = []
    try:
        with open('sales.txt', mode='r') as f:
            
            # Filter data
            count = 0
            for line in f:
                count += 1
                if count != 1:
                    try:
                        line = line.replace('\n', '')
                        receipt, product, unit, quanlity = line.split(', ')
                        unit, quanlity = int(unit), int(quanlity)
                        assert ( (unit > 0) and (quanlity > 0) ), f'Check data at line {count} [{line}]'
                    except ValueError:
                        print(f'At line {count} an invalid data is found, and it was skipped. [{line}]')
                    else:
                        all_product.append([receipt, product, unit, quanlity])
                        #print(receipt, product, unit, quanlity)
            
            # Compute Data
            product_list = {}
            for receipt, product, unit, quanlity in all_product:
                if product not in product_list:
                    product_list[ product ] = [unit, quanlity]
                else:
                    product_list[ product ][1] += quanlity
            
            # Output Data
            print(product_list)
            total_all_product_sold = 0
            total_all_product_price = 0
            output = ''
            for k, v in product_list.items():
                total_all_product_sold += v[1]
                total_all_product_price += v[0]*v[1]
                output += f'{k} x {v[1]} x {v[0]} bath = {v[0]*v[1]} bath\n'
            
            print(f'The data in file contains {len(all_product)}')
            print('='*30)
            print(f'Product were sald {total_all_product_sold} items.')
            print(output[:-1])
            print('='*30)
            print(f'Total sales {total_all_product_price} bath.')
            
    except IOError:
        print('Cannot open "sales.txt"')
    

if __name__ == '__main__':
    main()