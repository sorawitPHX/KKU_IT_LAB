def main():
    all_product = []
    try:
        with open('sales.txt', mode='r') as f:
            
            # Filter data
            for index, line in enumerate(f):
                if index != 0:
                    try:
                        line = line.replace('\n', '')
                        receipt, product, unit, quanlity = line.split(', ')
                        unit, quanlity = int(unit), int(quanlity)
                        assert ( (unit > 0) and (quanlity > 0) ), f'Check data at line {index+1} [{line}]'
                    except ValueError:
                        print(f'At line {index+1} an invalid data is found, and it was skipped. [{line}]')
                    else:
                        all_product.append([receipt, product, unit, quanlity])
                        #print(receipt, product, unit, quanlity)
            
            # Compute Data
            product_list = {}
            for receipt, product, unit, quanlity in all_product:
                if product not in product_list:
                    product_list[ product ] = quanlity
                else:
                    product_list[ product ] += quanlity
            
            # Output Data
           # print(all_product)
            #print(product_list)
            
            
    except IOError:
        print('Cannot open "sales.txt"')
    

if __name__ == '__main__':
    main()