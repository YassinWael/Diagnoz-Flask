# Import the Flask class from the flask module
from flask import Flask, render_template, request, redirect, url_for,flash,session,send_file
from flask_babel import Babel
from ini_database import Diseases_dict,Diseases_info,new_sy_list,chosen_symptoms,code_running


# Create a new Flask app instance
app = Flask(__name__)
app.secret_key = 'iugegiujegehgdtijoie'

babel = Babel(app)
def get_locale():
    return session.get('language', 'en')
babel.init_app(app, locale_selector=get_locale)


# Define a route for setting the language
@app.route('/set_language')
def set_language():
    if 'language' not in session:
        session['language'] = 'en'
    # sets the opposite of the old language then return to the page
    if session['language'] == 'en':

        session['language'] = 'ar'
    else:
        session['language'] = 'en'
    return redirect(request.referrer)


# Function to format the symptoms entered by the user
def format_symptoms(sy):
    # Split the symptoms into a list
    sy = sy.split(',')
   
    # Convert all symptoms to lowercase and remove any leading/trailing whitespace
    sy = [i.lower().strip() for i in sy]
    
    return sy

# Function to determine possible diagnoses based on entered symptoms
def get_diseases(symptoms_list):
    # Create a dictionary to count the number of times each disease appears
    dict_count = {}
    
    # Convert all symptoms to a format that matches the keys in Diseases_dict
    new_symptoms_list = [i.strip("']").strip("['").replace(" ","_") for i in symptoms_list]
    
    # Loop through all symptoms and diseases to count the number of matches
    for sym in new_symptoms_list:
        for key, value in Diseases_dict.items():
            if sym in value:
                try:
                    dict_count[key] += 1
                except Exception as e:
                    dict_count[key] = 1
            
    # Create a dictionary that maps diseases to the percentage of symptoms matched
    diseases_dict_percent = {i:get_percent(i,dict_count) for i in dict_count.keys()}

    # Sort the diseases by the percentage of symptoms matched
    sorted_diseases = sorted(diseases_dict_percent.items(), key=lambda x: int(dict_count[x[0]])/len(Diseases_dict[x[0]]), reverse=True)
    
    return sorted_diseases

# Function to calculate the percentage of symptoms matched for a given disease
def get_percent(disease,dict):
    return f'Has {dict[disease]} {"symptom" if int(dict[disease])==1 else "symptoms" } out of {len(Diseases_dict[disease])} '

# Define a route for the home page
@app.route('/')
@app.route('/home')
@app.route('/None')
def home():
    return render_template('home.html')



# Define a route for the symptoms page
@app.route('/symptoms', methods=['GET', 'POST'])
def symptoms():
    if request.method == "POST":
        # Get the symptoms entered by the user and redirect to the diseases page
        symptoms = request.form["sy"]
        if len(symptoms)<1: # Used Inputted Empty List
            flash("Cannot Be Empty!")
            return render_template('symptoms.html')
        else:
            print(len(symptoms),symptoms)
            return redirect(url_for("diseases",sy=symptoms))
    else:
        # Display the symptoms page
        return render_template("symptoms.html")

# Define a route for the diseases page
@app.route('/diseases/<sy>')
def diseases(sy):
    # Format the symptoms entered by the user
    symptoms = format_symptoms(sy)
    print(symptoms)
    for i in symptoms:
        if len(i)<4:
            flash("List Can't Be Empty :)")
            print(i)
            return redirect(url_for('choose',letter="all"))
        else:
            print(len(i))
            print("Else")
            continue
    
    # Get possible diagnoses based on the entered symptoms
    global diseases_final 
    diseases_final = get_diseases(symptoms_list=symptoms) 

    #remove squared brackets 
    symptoms = [i.strip("['").strip("']") for i in symptoms]

    # Render the diseases page with the list of possible diagnoses
   
    
    return render_template('diseases.html',keys=diseases_final,sys=symptoms)

# Define a route for the learn more page
@app.route('/learnmore/<disease>',methods = ['GET','POST'])
def learn_more(disease):
    # Render the learn more page with information on the selected disease
    return render_template('learn_more.html',info = Diseases_info[disease],name = disease)

# Define a route for the symptoms set page
@app.route('/symptoms_set')
def symptoms_set():
    # Convert the set of unique symptoms to a list and render the symptoms set page
    sy_list = list(new_sy_list)
    return render_template('symptoms_set.html',sys=sy_list)

# Define a route for the about page
@app.route('/about')
def about():
    return render_template('about.html',title = 'About')

# Define a route for the choose page
@app.route('/choose/<letter>',methods=['GET','POST'])
def choose(letter=""):
   
    sy_list = sorted(new_sy_list)
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'Y']
    if letter == 'all':
        return render_template('choose.html',chosen_list = chosen_symptoms,sys_list=sy_list,letters=letters)
    else:
       
        sy_list = [i for i in sy_list if not i.startswith(' ')]
        sy_list = [i for i in sy_list if i[0]==letter.lower()]
       
        return render_template('choose.html',chosen_list = chosen_symptoms,sys_list=sorted(sy_list),letters=letters,letter_chosen=letter)

    # Sort the list of unique symptoms and render the choose page
    


@app.route('/add_symptom/<symptom>')
def add_symptom(symptom):
    
    chosen_symptoms.append(symptom)
    return redirect(url_for('choose',letter="all"))

@app.route('/call_diseases') 
def call_diseases():
    """Called Only from the choose.html page , to call the diseases function."""
    global chosen_symptoms
    return_value = redirect(url_for('diseases',sy=chosen_symptoms))
    
    chosen_symptoms = []
    
    return return_value

# Define a route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/download')
def download():
    return render_template('download.html')

# Google verification
@app.route('/googlecb2bae94ee95880b.html')
def google_verification():
    return app.send_static_file('googlecb2bae94ee95880b.html')

@app.route('/sw.js')
def service_worker():
    return send_file('sw.js')


@app.route('/app.js')
def app_worker():
    return app.send_static_file('app.js')

@app.route('/offline.html')
def offline_worker():
    return send_file('offline.html')

# For offline caching
@app.route('/home.html')
def home_cache():
    return send_file('templates/home.html')

@app.route('/layout.html')
def layout_cache():
    return send_file('templates/layout.html')
# Run the Flask app
if __name__ == '__main__':

        app.run(host='0.0.0.0',debug=True,port=5000)
