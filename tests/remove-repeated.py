import csv
from icecream import ic
import pickle
## This removes all the repeated diseases from a csv file

used_diseases = []
lines = []

with open(r'C:\Users\yassi\Downloads\Flask-tut-bing\Flask-Disease\datasets\symptom_Description.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    for line in csv_reader:
        try:
            if line[0] not in used_diseases:
                lines.append(line)
                used_diseases.append(line[0])
                ic(line[0])
        except IndexError:
            ic(used_diseases)
            break
            
        






with open(r'C:\Users\yassi\Downloads\Flask-tut-bing\Flask-Disease\datasets\symptom_Description.csv',mode = 'w',newline='') as csv_file:
    
    writer = csv.writer(csv_file)
    
    writer.writerows(lines)


with open('used_diseases.pkl', 'wb') as f:
    pickle.dump(used_diseases, f)