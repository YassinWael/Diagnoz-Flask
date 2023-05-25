# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for
import csv
from icecream import ic

# Initialize Flask app
app = Flask(__name__)

# Read the CSV file and create a dictionary of diseases and their symptoms
Diseases_dict = {}
with open('dataset.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        Diseases_dict[line[0]] = line[1:]

# Function to format the symptoms entered by the user
def format_symptoms(sy):
    # Split the symptoms into a list
    sy = sy.split(' ')
    # Convert each symptom to lowercase and remove any leading/trailing spaces
    sy = [i.lower().strip() for i in sy]
    return sy

# Function to get a list of possible diseases based on the symptoms entered by the user
def get_diseases(symptoms_str):
    dict_count = {}
    for key, value in Diseases_dict.items():
        count = 0
        for symptom in symptoms_str:
            symptom = symptom.strip()
            if symptom in value:
                count += 1
        if count > 0:
            dict_count[key] = count
    # Calculate the percentage of symptoms matched for each disease
    diseases_dict_percent = {i:get_percent(i,dict_count) for i in dict_count.keys()}
    # Sort the diseases in descending order of percentage matched
    sorted_diseases = sorted(diseases_dict_percent.items(), key=lambda x: x[1], reverse=True)
    return sorted_diseases

# Function to calculate the percentage of symptoms matched for a disease
def get_percent(disease,dict):
    percent = round(dict[disease] / len(Diseases_dict[disease])*100)
    if len(str(percent))==1:
        percent = f'0{percent}'
    return f'is {percent}%'

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
    ic(symptoms) # Print the formatted symptoms using the icecream module
    # Get a list of possible diseases based on the symptoms entered by the user
    diseases_final = get_diseases(symptoms_str=symptoms)
    ic(diseases_final) # Print the list of diseases and their percentage matched using the icecream module
    # Display the diseases page with the list of diseases
    return render_template('diseases.html',keys=diseases_final)

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html',title = 'About')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)