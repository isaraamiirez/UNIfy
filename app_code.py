
#CONSOLE: LOGIN INFORMATION
  
from tkinter import *
from functools import partial


def validateLogin(username, password):
	print ("User has entered the username :", username.get())
	print ("User has entered the password :", password.get())
	return


# Creating the GUI window
console = Tk () # Initialization of Tkinter
console.geometry('400x300')  # Size of the window
console.title('Login page for using python Tkinter code')


# Creating input of username
Label1 = Label (console, text="User Name"). grid (row=0, column=0) # Label to specify Username
Input1 = StringVar()
# Inputing the user’s name
usernameEntry = Entry (console, textvariable = Input1). grid (row=0, column=1)


# Creating input of Password
# Label to specify Login
Label2 = Label(console,text="Password").grid(row=1, column=0)
Input2 = StringVar()
# Inputing the Password
passwordEntry = Entry (console, textvariable = Input2, show='*'). grid (row=1, column=1)


validateLogin = partial (validateLogin, Input1, Input2)


# Creating login button
loginButton = Button (console, text="Login", command=validateLogin). grid (row=4, column=0)


console.mainloop()


#FUNCTION 1: Filtered search with variables: 

#Library required for this part: 

universities1 = {
    "ICADE Comillas": {"name": "ICADE Comillas", "location": "Madrid", "study_type": "traditional method",
                       "study_fields": "business", "annual_budget": "10-15k", "language": "spanish",
                       "public_private": "private"},
    "IE University": {"name": "IE University", "location": "Madrid", "study_type": "project based", "study_fields": "business",
                      "annual_budget": "20-25k", "language": "english", "public_private": "private"},
    "ICAI Comillas": {"name": "ICAI Comillas", "location": "Madrid", "study_type": "traditional method",
                      "study_fields": "engineering", "annual_budget": "10-15k", "language": "spanish",
                      "public_private": "private"},
    "CIHS Comillas": {"name": "CIHS Comillas", "location": "Madrid", "study_type": "traditional method",
                      "study_fields": "social sciences", "annual_budget": "10-15k", "language": "spanish",
                      "public_private": "private"},
    "Universidad Carlos III": {"name": "Universidad Carlos III", "location": "Madrid",
                             "study_type": "traditional method", "study_fields": "general",
                               "annual_budget": "0-5k", "language": "spanish", "public_private": "public"},
    "Universidad Complutense de Madrid": {"name": "Universidad Complutense de Madrid", "location": "Madrid",
                                        "study_type": "traditional method", "study_fields": "general",
                                          "annual_budget": "0-5k", "language": "spanish", "public_private": "public"},
    "Universidad Autonoma de Madrid": {"name": "Universidad Autonoma de Madrid", "location": "Madrid",
                                       "study_type": "traditional method", "study_fields": "general",
                                       "annual_budget": "0-5k", "language": "spanish",
                                       "public_private": "public"},
    "ESIC Valencia": {"name": "ESIC Valencia", "location": "Valencia", "study_type": "project based", "study_fields": "business",
                      "annual_budget": "10-15k", "language": "spanish", "public_private": "private"},
    "Universidad de Navarra": {"name": "Universidad de Navarra", "location": "Pamplona",
                             "study_type": "traditional method", "study_fields": "health sciences",
                               "annual_budget": "10-15k", "language": "spanish", "public_private": "private"},
    "Universitat Pompeu Fabra": {"name": "Universitat Pompeu Fabra", "location": "Barcelona",
                                 "study_type": "traditional method", "study_fields": "general",
                                 "annual_budget": "0-5k", "language": "catalan",
                                  "public_private": "public"},
    "ESADE Barcelona": {"name": "ESADE Barcelona", "location": "Barcelona", "study_type": "project based", "study_fields": "business",
                        "annual_budget": "15-20k", "language": "spanish",  "public_private": "private"},
    "Universidad de Salamanca": {"name": "Universidad de Salamanca", "location": "Salamanca",
                                 "study_type": "project based", "study_fields": "general", "annual_budget": "0-5k",
                                 "language": "spanish", "public_private": "public"},
    "Universidad Rey Juan Carlos": {"name": "Universidad Rey Juan Carlos", "location": "Madrid", "study_type": "traditional method", "study_fields": "general",
                                    "annual_budget": "0-5k", "language": "spanish",
                                    "public_private": "public"},
    "Univerisdad Politecnica de Valencia": {"name": "Univerisdad Politecnica de Valencia", "location": "Valencia", "study_type": "traditional method",
                                            "study_fields": "engineering",
                                            "annual_budget": "0-1k", "language": "spanish",
                                            "public_private": "public"},
}

options = {"location": ["Madrid", "Pamplona", "Valencia", "Salamanca", "Barcelona"],
           "public_private": ["public", "private"],
           "study_type": ["traditional method", "project based"],
           "study_fields": ["business", "engineering", "social sciences", "health sciences", "general"],
           "annual_budget": ["0-5k", "10-15k", "15-20k", "20-25k"],
           "language": ["spanish", "english", "catalan"]
           }

def printOptions(dictionary):
    print("What are your preferences?: ")
    for i in dictionary:
        print(i)


def printOptionsOptions(dictionary, what):
    print("Filtering options: ")
    for i in dictionary[what]:
        print(i)


def printResults(array):
    print("\n\nThese are the Universities you are looking for!: ")
    for i in array:
        print(i)


def filter():
    filter = input("Do you want to start your filtered search? (if so type 'yes', if not, type 'no'): ")
    if filter == "yes":
        opciones = []
        while True:
            printOptions(options)
            what = input("\nWhat do you want to filter: ").lower()
            printOptionsOptions(options, what)
            what2 = input("\nWhat do you want to filter: ")
            opciones.append((what, what2))
            otra = input("Do you want to add another option? ")
            if otra == "no":
                break
    return opciones


def compatibleUnis(universities1):
    compatible = []
    opciones = filter()
    for i in universities1:
        count = 0
        for j in opciones:
            if universities1[i][j[0]] == j[1]:
                count += 1
        if count == len(opciones):
            compatible.append(universities1[i]["name"])
    return compatible


unis = compatibleUnis(universities1)
printResults(unis)

#FUNCTION 2: Questionare to know your university preferences in terms of personality

#Library required for this part: 

universities2 = {
    "ICADE Comillas": {"name": "ICADE Comillas", "spirit": "employee", "person_type": "critical & analytical",
                       "team_work": "sets objectives & methodologies", "study_type": "learning content by heart",
                       "study_fields": "business", "annual_budget": "10-15k", "language": "spanish",
                       "contact": "admisiones@comillas.edu"},
    "IE University": {"name": "IE University", "spirit": "entrepreneur", "person_type": "innovative & creative",
                      "team_work": "has creative ideas", "study_type": "doing projects", "study_fields": "business",
                      "annual_budget": "20-25k", "language": "english", "contact": "university@ie.edu"},
    "ICAI Comillas": {"name": "ICAI Comillas", "spirit": "employee", "person_type": "critical & analytical",
                      "team_work": "sets objectives & methodologies", "study_type": "learning content by heart",
                      "study_fields": "engineering", "annual_budget": "10-15k", "language": "spanish",
                      "contact": "admisiones@comillas.edu"},
    "CIHS Comillas": {"name": "CIHS Comillas", "spirit": "creative worker", "person_type": "empathetic & social",
                      "team_work": "organises personal strengths", "study_type": "learning content by heart",
                      "study_fields": "social sciences", "annual_budget": "10-15k", "language": "spanish",
                      "contact": "admisiones@comillas.edu"},
    "Universidad Carlos III": {"name": "Universidad Carlos III", "spirit": "employee",
                               "person_type": "critical & analytical", "team_work": "sets objectives & methodologies",
                               "study_type": "learning content by heart", "study_fields": "general",
                               "annual_budget": "0-5k", "language": "spanish", "contact": "dpd@uc3m.es"},
    "Universidad Complutense de Madrid": {"name": "Universidad Complutense de Madrid", "spirit": "creative worker",
                                          "person_type": "empathetic & social",
                                          "team_work": "organises personal strengths",
                                          "study_type": "learning content by heart", "study_fields": "general",
                                          "annual_budget": "0-5k", "language": "spanish", "contact": "oipd@ucm.es"},
    "Universidad Autonoma de Madrid": {"name": "Universidad Autonoma de Madrid", "spirit": "employee",
                                       "person_type": "critical & analytical",
                                       "team_work": "organises personal strengths",
                                       "study_type": "learning content by heart", "study_fields": "general",
                                       "annual_budget": "0-5k", "language": "spanish",
                                       "contact": "informacion.general@uam.es"},
    "ESIC Valencia": {"name": "ESIC Valencia", "spirit": "entrepreneur", "person_type": "innovative & creative",
                      "team_work": "has creative ideas", "study_type": "doing projects", "study_fields": "business",
                      "annual_budget": "10-15k", "language": "spanish", "contact": "info.valencia@esic.edu"},
    "Universidad de Navarra": {"name": "Universidad de Navarra", "spirit": "entrepreneur",
                               "person_type": "critical & analytical", "team_work": "sets objectives & methodologies",
                               "study_type": "learning content by heart", "study_fields": "health sciences",
                               "annual_budget": "10-15k", "language": "spanish", "contact": "info@unav.es"},
    "Universitat Pompeu Fabra": {"name": "Universitat Pompeu Fabra", "spirit": "employee",
                                 "person_type": "critical & analytical", "team_work": "sets objectives & methodologies",
                                 "study_type": "learning content by heart", "study_fields": "general",
                                 "annual_budget": "0-5k", "language": "catalan",
                                 "contact": "carreres.professionals@upf.edu"},
    "ESADE Barcelona": {"name": "ESADE Barcelona", "spirit": "employee", "person_type": "innovative & creative",
                        "team_work": "has creative ideas", "study_type": "doing projects", "study_fields": "business",
                        "annual_budget": "15-20k", "language": "spanish", "contact": "shop@2000publimark.com"},
    "Universidad de Salamanca": {"name": "Universidad de Salamanca", "spirit": "creative worker",
                                 "person_type": "empathetic & social", "team_work": "organises personal strengths",
                                 "study_type": "doing projects", "study_fields": "general", "annual_budget": "0-5k",
                                 "language": "spanish", "contact": "protocolo@usal.es"},
    "Universidad Rey Juan Carlos": {"name": "Universidad Rey Juan Carlos", "spirit": "employee",
                                    "person_type": "empathetic & social", "team_work": "organises personal strengths",
                                    "study_type": "learning content by heart", "study_fields": "general",
                                    "annual_budget": "0-5k", "language": "spanish",
                                    "contact": "fuenlabrada.secretariadealumnos@urjc.es"},
    "Univerisdad Politecnica de Valencia": {"name": "Univerisdad Politecnica de Valencia", "spirit": "employee",
                                            "person_type": "critical & analytical",
                                            "team_work": "sets objectives & methodologies",
                                            "study_type": "learning content by heart", "study_fields": "engineering",
                                            "annual_budget": "0-1k", "language": "spanish",
                                            "contact": "informacion@upv.es"},
}


from heapq_max import heappop_max, heappush_max, heapify_max

def clean_console():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


def asking_user(universities2):
    print(
        'Hi! If you are here you are probably searching \nfor universities without being very certain of which one suits you best.')
    print('\nUNIfy is here to help you. Please answer the following questions to check it out!')

    spirit = input(
        "\nHow do you see yourself in 20 years, choose one: \n\t1) employee \n\t2) entrepreneur \n\t3) creative worker\n\n>>> Answer: ")
    while spirit not in ["1", "2", "3"]:
        spirit = input(
            "How do you see yourself in 20 years, choose one: \n\t1) employee \n\t2) entrepreneur \n\t3) creative worker\n\n>>> Answer: ")

    spirit_dict = {
        "1": "employee",
        "2": "entrepreneur",
        "3": "creative worker"
    }
    print(spirit_dict[spirit])

    clean_console()
    print("Your answers:", spirit_dict[spirit])
    person_type = input(
        "What sort of person do you identify with the most, choose from: \n\t1)innovative & creative \n\t2)critical & analytical \n\t3)empathetic & social\n\n>>> Answer: ")
    while person_type not in ["1", "2", "3"]:
        person_type = input(
            "What sort of person do you identify with the most, choose from: \n\t1)innovative & creative \n\t2)critical & analytical \n\t3)empathetic & social\n\n>>> Answer: ")

    person_type_dict = {
        "1": "innovative & creative",
        "2": "critical & analytical",
        "3": "empathetic & social"
    }
    clean_console()
    print("Your answers:", spirit_dict[spirit], "_", person_type_dict[person_type])
    team_work = input(
        "When working in teams, which of the following do you identify with the most?: \n\t1)has creative ideas \n\t2)sets objectives & methodology \n\t3)organises personal strengths\n\n>>> Answer: ")
    while team_work not in ["1", "2", "3"]:
        team_work = input(
            "When working in teams, which of the following do you identify with the most?: \n\t1)has creative ideas \n\t2)sets objectives & methodology \n\t3)organises personal strengths\n\n>>> Answer: ")

    team_work_dict = {
        "1": "has creative ideas",
        "2": "sets objectives & methodology",
        "3": "organises personal strengths"
    }

    clean_console()
    print("Your answers:", spirit_dict[spirit], "_", person_type_dict[person_type], "_", team_work_dict[team_work])
    study_type = input(
        "What helps you study the most? choose between: \n\t1)doing projects \n\t2)learning content by heart\n\n>>>Answer: ")
    while study_type not in ["1", "2"]:
        study_type = input(
            "What helps you study the most? choose between: \n\t1)doing projects \n\t2)learning content by heart\n\n>>>Answer: ")

    study_type_dict = {
        "1": "doing projects",
        "2": "learning content by heart"
    }

    clean_console()
    print("Your answers:", spirit_dict[spirit], "_", person_type_dict[person_type], "_", team_work_dict[team_work], "_",
          study_type_dict[study_type])
    study_fields = input(
        "What study field are you looking to enter?: \n\t1)business \n\t2)engineering \n\t3)social sciences \n\t4)health sciences \n\t5)general\n\n>>>Answer: ")
    while study_fields not in ["1", "2", "3", "4", "5"]:
        study_fields = input(
            "What study field are you looking to enter?: \n\t1)business \n\t2)engineering \n\t3)social sciences \n\t4)health sciences \n\t5)general\n\n>>>Answer: ")

    study_fields_dict = {
        "1": "business",
        "2": "engineering",
        "3": "social sciences",
        "4": "health sciences",
        "5": "general"
    }

    clean_console()
    print("Your answers:", spirit_dict[spirit], "_", person_type_dict[person_type], "_", team_work_dict[team_work], "_",
          study_type_dict[study_type], "_", study_fields_dict[study_fields])
    annual_budget = input(
        "What is your approximated annual budget, choose one: \n\t1)0-5k \n\t2)10-15k \n\t3)15-20k \n\t4)20-25k\n\n>>> Answer: ")
    while annual_budget not in ["1", "2", "3", "4"]:
        annual_budget = input(
            "What is your approximated annual budget, choose one: \n\t1)0-5k \n\t2)10-15k \n\t3)15-20k \n\t4)20-25k\n\n>>> Answer: ")

    annual_budget_dict = {
        "1": "0-5k",
        "2": "10-15k",
        "3": "15-20k",
        "4": "20-25k"
    }

    clean_console()
    print("Your answers:", spirit_dict[spirit], "_", person_type_dict[person_type], "_", team_work_dict[team_work], "_",
          study_type_dict[study_type], "_", study_fields_dict[study_fields], "_", annual_budget_dict[annual_budget])
    language = input(
        "What is your language preference? choose from: \n\t1)spanish \n\t2)english \n\t3)catalan\n\n>>> Answer: ")
    while language not in ["1", "2", "3"]:
        language = input(
            "What is your language preference? choose from: \n\t1)spanish \n\t2)english \n\t3)catalan\n\n>>> Answer: ")

    language_dict = {
        "1": "spanish",
        "2": "english",
        "3": "catalan"
    }

    print("Your answers:", spirit_dict[spirit], "_", person_type_dict[person_type], "_", team_work_dict[team_work], "_",
          study_type_dict[study_type], "_", study_fields_dict[study_fields], "_", annual_budget_dict[annual_budget],
          "_", language_dict[language])

    map_u = []
    heapify_max(map_u)
    for university in universities2:
        score = 0
        if universities2[university]["spirit"] == spirit_dict[spirit]:
            score += 1
        if universities2[university]["person_type"] == person_type_dict[person_type]:
            score += 1
        if universities2[university]["team_work"] == team_work_dict[team_work]:
            score += 1
        if universities2[university]["study_type"] == study_type_dict[study_type]:
            score += 1
        if universities2[university]["study_fields"] == study_fields_dict[study_fields]:
            score += 1
        if universities2[university]["annual_budget"] == annual_budget_dict[annual_budget]:
            score += 1
        if universities2[university]["language"] == language_dict[language]:
            score += 1

        heappush_max(map_u, (score, universities2[university]["name"]))
    return heappop_max(map_u)


def result(universities2, uni):
    print(f"\nCongratulations! You have been matched with {universities2[uni[1]]['name']}")
    apply = input("\nDo you want to apply now? (if so, type 'yes', else click ENTER) ")
    if apply == "yes":
        print("\nHere's the university's contact information: ", universities2[uni[1]]["contact"])


def main(universities2):
    uni = asking_user(universities2)
    result(universities2, uni)


main(universities2)
