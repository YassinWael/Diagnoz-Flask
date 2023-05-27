import csv
from icecream import ic

lines = []

   



with open(r'C:\Users\yassi\Downloads\Flask-tut-bing\cleaned_data.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    for line in csv_reader:
        try:
                line = [i.replace(" ","") for i in line]
                lines.append(line)




                ic(line[0])
               
                
        except IndexError:
            ic('broken')
            break
            
with open(r'C:\Users\yassi\Downloads\Flask-tut-bing\cleaned_data.csv',mode = 'w',newline='') as csv_file:
    
    writer = csv.writer(csv_file)
    
    writer.writerows(lines)

