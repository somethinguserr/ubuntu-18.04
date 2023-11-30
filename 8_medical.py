# Program 1

class ExpertSystem:
    def __init__(self):
        self.symptoms = []
        self.rules = {}

    def add_rule(self, disease, symptom_list):
        self.rules[disease] = symptom_list

    def add_symptom(self, symptom):
        self.symptoms.append(symptom)

    def disp_symptoms(self):
        print("\nList of symptoms: ")
        for symptom in self.symptoms:
            print(symptom)
        print()

    def diagnose(self, patient_symptoms):
        possible_diseases = []

        for disease, symptoms in self.rules.items():
            if all(symptom in patient_symptoms for symptom in symptoms):
                possible_diseases.append(disease)

        return possible_diseases


# Create an instance of the expert system
expert_system = ExpertSystem()

# Define symptoms
expert_system.add_symptom("Fever")
expert_system.add_symptom("Cough")
expert_system.add_symptom("Headache")
expert_system.add_symptom("Fatigue")
expert_system.add_symptom("Sore Throat")
expert_system.add_symptom("Runny Nose")
expert_system.add_symptom("Difficulty Breathing")
expert_system.add_symptom("Body Aches")
expert_system.add_symptom("Chills")
expert_system.add_symptom("Nausea")

# Define rules for diseases based on symptoms
expert_system.add_rule("Flu", ["Fever", "Cough", "Fatigue"])
expert_system.add_rule("Common Cold", ["Cough", "Headache", "Runny Nose"])
expert_system.add_rule("Strep Throat", ["Sore Throat", "Fever", "Headache"])
expert_system.add_rule("COVID-19", ["Fever", "Cough", "Difficulty Breathing", "Fatigue"])
expert_system.add_rule("Influenza", ["Fever", "Cough", "Body Aches", "Chills"])
expert_system.add_rule("Allergy", ["Runny Nose", "Sore Throat"])

expert_system.disp_symptoms()

# Get input from the user
patient_symptoms = input("Enter symptoms from the above list (comma-separated): ").split(", ")

# Diagnose the possible diseases
possible_diseases = expert_system.diagnose(patient_symptoms)

# Display the diagnosis
if possible_diseases:
    print("Possible diseases: ", ", ".join(possible_diseases))
else:
    print("No matching diseases found.")




# Program 2:

# from pyknow import *

# diseases_list = []
# diseases_symptoms = []
# symptom_map = {}
# d_desc_map = {}
# d_treatment_map = {}

# def preprocess():
#     global diseases_list, diseases_symptoms, symptom_map, d_desc_map, d_treatment_map
#     diseases = open("diseases.txt")
#     diseases_t = diseases.read()
#     diseases_list = diseases_t.split("\n")
#     diseases.close()
    
#     for disease in diseases_list:
#         disease_s_file = open("Disease symptoms/" + disease + ".txt")
#         disease_s_data = disease_s_file.read()
#         s_list = disease_s_data.split("\n")
#         diseases_symptoms.append(s_list)
#         symptom_map[str(s_list)] = disease
#         disease_s_file.close()
        
#         disease_s_file = open("Disease descriptions/" + disease + ".txt")
#         disease_s_data = disease_s_file.read()
#         d_desc_map[disease] = disease_s_data
#         disease_s_file.close()
        
#         disease_s_file = open("Disease treatments/" + disease + ".txt")
#         disease_s_data = disease_s_file.read()
#         d_treatment_map[disease] = disease_s_data
#         disease_s_file.close()

# def identify_disease(*arguments):
#     symptom_list = []
#     for symptom in arguments:
#         symptom_list.append(symptom)
#     return symptom_map[str(symptom_list)]

# def get_details(disease):
#     return d_desc_map[disease]

# def get_treatments(disease):
#     return d_treatment_map[disease]

# def if_not_matched(disease):
#     print("")
#     id_disease = disease
#     disease_details = get_details(id_disease)
#     treatments = get_treatments(id_disease)
#     print("")
#     print("The most probable disease that you have is %s\n" % (id_disease))
#     print("A short description of the disease is given below :\n")
#     print(disease_details + "\n")
#     print("The common medications and procedures suggested by other real doctors are: \n")
#     print(treatments + "\n")

# class Greetings(KnowledgeEngine):
#     @DefFacts()
#     def _initial_action(self):
#         print("")
#         print("Hi! I am Dr. Yar, I am here to help you make your health better.")
#         print("For that, you'll have to answer a few questions about your conditions")
#         print("Do you feel any of the following symptoms:")
#         print("")
#         yield Fact(action="find_disease")

#     @Rule(Fact(action='find_disease'), NOT(Fact(headache=W())), salience=1)
#     def symptom_0(self):
#         self.declare(Fact(headache=input("headache: ")))

#     # ... (Repeat similar Rule blocks for other symptoms)

#     @Rule(Fact(action='find_disease'), Fact(disease=MATCH.disease), salience=-998)
#     def disease(self, disease):
#         print("")
#         id_disease = disease
#         disease_details = get_details(id_disease)
#         treatments = get_treatments(id_disease)
#         print("")
#         print("The most probable disease that you have is %s\n" % (id_disease))
#         print("A short description of the disease is given below :\n")
#         print(disease_details + "\n")
#         print("The common medications and procedures suggested by other real doctors are: \n")
#         print(treatments + "\n")

#     @Rule(Fact(action='find_disease'),
#           Fact(headache=MATCH.headache),
#           Fact(back_pain=MATCH.back_pain),
#           # ... (Repeat similar Facts for other symptoms)
#           NOT(Fact(disease=MATCH.disease)), salience=-999)
#     def not_matched(self, headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,
#                     low_body_temp, fever, sunken_eyes, nausea, blurred_vision):
#         print("\nDid not find any disease that matches your exact symptoms")
#         lis = [headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness, low_body_temp,
#                fever, sunken_eyes, nausea, blurred_vision]
#         max_count = 0
#         max_disease = ""
        
#         for key, val in symptom_map.items():
#             count = 0
#             temp_list = eval(key)
            
#             for j in range(0, len(lis)):
#                 if temp_list[j] == lis[j] and lis[j] == "yes":
#                     count = count + 1
            
#             if count > max_count:
#                 max_count = count
#                 max_disease = val
        
#         if_not_matched(max_disease)

# if __name__ == "__main__":
#     preprocess()
#     engine = Greetings()
    
#     while True:
#         engine.reset()  # Prepare the engine for execution.
#         engine.run()    # Run it!
#         print("Would you like to diagnose some other symptoms?")
        
#         if input() == "no":
#             exit()
