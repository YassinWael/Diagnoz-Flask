import csv
lang = "English" #Default language.
Diseases_dict = {}

# Define a list to store symptoms when user wants list of symptoms only
symptoms_list = []

# Define a dictionary to store information on each disease
Diseases_info = {}

# Define paths to datasets
datasets_path = r'C:/Users/yassi/Downloads/Flask-tut-bing/Flask-Disease/datasets'
host_path = r"/home/Diagnoz/mysite/datasets"

# Variable for location where code is running 

code_running = "Local" # Local code running


# Define an empty list to store chosen symptoms
chosen_symptoms = []
try:
    with open(rf'{datasets_path}/dataset.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
        
            Diseases_dict[line[0]] = line[1:]
            symptoms_list.append(line[1:])  

    

    with open(rf'{datasets_path}/symptom_Description.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
                
                Diseases_info[line[0].replace(' ',"")] = line[1]



except FileNotFoundError: 
    # code is running from host

    code_running = "Host"
    with open(rf'{host_path}/dataset.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
        
            Diseases_dict[line[0]] = line[1:]
            symptoms_list.append(line[1:])  
    

    with open(rf'{host_path}/symptom_Description.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
                
                Diseases_info[line[0].replace(' ',"")] = line[1]


# Join all symptoms in symptoms_list into a single string
sy_list = " ".join([" ".join(symptoms) for symptoms in symptoms_list])

# Split the string into a list of individual symptoms
sy_list = sy_list.split(" ")

# Remove any symptoms that contain the word "Symptom"
sy_list = [i for i in sy_list if 'Symptom' not in i.split('_')]

# Create a new set to store unique symptoms
new_sy_list = set(sy_list) 


print("------------------------------------------------------------------------------------------------")

