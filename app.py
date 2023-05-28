# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for
import csv


# Initialize Flask app
app = Flask(__name__)

# Read the CSV file and create a dictionary of diseases and their symptoms
Diseases_dict = {}
symptoms_list = [] #Used when user wants list of symptoms only.
Diseases_info = {}
datasets_path = r'C:/Users/yassi/Downloads/Flask-tut-bing/Flask-Disease/datasets'
host_path = r"/home/Diagnoz/mysite/datasets"

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
    with open(rf'{host_path}/dataset.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
        
            Diseases_dict[line[0]] = line[1:]
            symptoms_list.append(line[1:])  
    

    with open(rf'{host_path}/symptom_Description.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
                
                Diseases_info[line[0].replace(' ',"")] = line[1]

sy_list = []
sy_list = " ".join([" ".join(symptoms) for symptoms in symptoms_list])
sy_list = sy_list.split(" ")
new_sy_list = []
new_sy_list = set(sy_list) 
                         

        



# Function to format the symptoms entered by the user
def format_symptoms(sy):
    # Split the symptoms into a list
    sy = sy.split(',')
    
    # Convert each symptom to lowercase and remove any leading/trailing spaces
    sy = [i.lower().strip() for i in sy]
    

    
    return sy

# Function to get a list of possible diseases based on the symptoms entered by the user
def get_diseases(symptoms_list):
    dict_count = {}
    
   
    new_symptoms_list = [i.strip("']").strip("['").replace(" ","_") for i in symptoms_list]
 
    

    for sym in new_symptoms_list:
        
        for key, value in Diseases_dict.items():
            if sym in value:
                
                try:
                    dict_count[key] += 1
                except Exception as e:
                    dict_count[key] = 1
            
    
    # Calculate the percentage of symptoms matched for each disease
    diseases_dict_percent = {i:get_percent(i,dict_count) for i in dict_count.keys()}

    
    # Sort the diseases in descending order of percentage matched
    sorted_diseases = sorted(diseases_dict_percent.items(), key=lambda x: int(dict_count[x[0]])/len(Diseases_dict[x[0]]), reverse=True)
    
    return sorted_diseases

# Function to calculate the percentage of symptoms matched for a disease
def get_percent(disease,dict):
    return f'has {dict[disease]} symptoms out of {len(Diseases_dict[disease])} '

# Route for the home page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# Route for the symptoms page
@app.route('/symptoms', methods=['GET', 'POST'])
def symptoms():
    if request.method == "POST":
        # Get the symptoms entered by the user and redirect to the diseases page
        symptoms = request.form["sy"]
        return redirect(url_for("diseases",sy=symptoms))
    else:
        # Display the symptoms page
        return render_template("symptoms.html")

# Route for the diseases page
@app.route('/diseases/<sy>')
def diseases(sy):
    # Format the symptoms entered by the user
    symptoms = format_symptoms(sy)

    #Global the variable so it can be used in the learn_more page
    global diseases_final 

    # Get a list of possible diseases based on the symptoms entered by the user
    diseases_final = get_diseases(symptoms_list=symptoms) 

    # Display the diseases page with the list of diseases
    return render_template('diseases.html',keys=diseases_final)

@app.route('/learnmore/<disease>',methods = ['GET','POST'])
def learn_more(disease):
    
    return render_template('learn_more.html',info = Diseases_info[disease],name = disease)
    
        

@app.route('/symptoms_set')
def symptoms_set():
    sy_list = list(new_sy_list)
    
    return render_template('symptoms_set.html',sys=sy_list)

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html',title = 'About')

@app.route('/contact')
def contact():
    return render_template('contact.html')


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)