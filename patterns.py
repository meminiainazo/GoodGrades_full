import pandas as pd
from fill_variables import *
import docx
import re

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
def get_patterns(subject):
    pattern_Debut = []
    pattern_End = []  
    pattern_point = ["points)","point)","pts)","pt)"]

    nb_Questions = get_nb_questions()
    pattern_numero = [[f"{num}\)",f"{num}/",f"Q{num}",f"QUESTION {num}",f"QUESTION{num}"] for num in range(nb_Questions)]

    is_inside_paragraph = False
    if subject.endswith(".docx"):
        file = docx.Document(subject)
        for paragraph in file.paragraphs:
            for i in range(nb_Questions):
                for j in range(len(pattern_numero[i])):
                    if re.match(pattern_numero[i][j], paragraph.text):
                        is_inside_paragraph = True

    return is_inside_paragraph

    #for i in range(nb_Questions):

# --------------------------------------------------------------------------------------------------------------

#doc = docx.Document("reference_answer/" + get_file("reference_answer/"))
#
##nb = get_nb_questions()
#document = ""
#for i in range(len(doc.paragraphs)):
#    document += (doc.paragraphs[i].text + "\n")
#
#print(document)

print(get_patterns("reference_answer/" + get_file("reference_answer/")))