
def openbarcodes():

    bland = ['Bland-22', 'Bland-28', 'Bland-51', 'Bland-70', 'Bland-90', 'Bland-82']

    f = open('Cornales.barcodes', 'r')
    lines = f.readlines()
    f2 = open("Cornales2.barcodes", "w")
    
    for line in lines:
        if  line.startswith(tuple(bland)):
            line = ''
            f2.write(line)
        else:
            f2.write(line.strip())
            f2.write('\n')
    
            
            

def main():
    openbarcodes()



if __name__ == "__main__":
    
    main()