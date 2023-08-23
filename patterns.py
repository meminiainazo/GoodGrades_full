import pandas as pd
from fill_variables import *
import docx

#Get number of questions ----------------------------------------------------------------------------------------
def get_nb_questions():
    not_Check = True
    while not_Check:
        nb_Questions = input("Entrez le nombre de questions : ")
        try:
            nb_Questions = int(nb_Questions)
            not_Check = False
        except ValueError:
            print("Veuillez entrer un nombre entier !")
    return nb_Questions
# --------------------------------------------------------------------------------------------------------------

#Get patterns --------------------------------------------------------------------------------------------------
def get_patterns():
    pattern_Debut = []
    pattern_End = []
    nb_Questions = get_nb_questions()

    #for i in range(nb_Questions):

# --------------------------------------------------------------------------------------------------------------

doc = docx.Document("reference_answer/" + get_file("reference_answer/"))

#nb = get_nb_questions()
document = ""
for i in range(len(doc.paragraphs)):
    document += (doc.paragraphs[i].text + "\n")

print(document)