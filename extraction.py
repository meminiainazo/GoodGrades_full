import pandas as pd
import re
import openpyxl
from fill_variables import *
from patterns import *
from docx import Document

#Global file ------------------------------------------------------------------------------------------------------------
template = pd.read_excel("template.xlsx")
# -----------------------------------------------------------------------------------------------------------------------


#Get question grade ------------------------------------------------------------------------------------------------------
def get_question_grade(grade, grade_pattern):
    target_columns = []
    for column in grade.columns.tolist():
        if re.search(grade_pattern, str(grade.at[0, column])):
            target_columns.append(column)
    return target_columns
# ------------------------------------------------------------------------------------------------------------------------


#Extract bareme ---------------------------------------------------------------------------------------------------------
def extract_bareme(column, j):
    max_Grade_pattern = r"Max grade:\s*(\d+)"
    if re.search(max_Grade_pattern, column):
        match = re.search(max_Grade_pattern, column)
        template.at[j, "note_sur"] = float(match.group(1))
# ------------------------------------------------------------------------------------------------------------------------


#Extract name and grades -------------------------------------------------------------------------------------------------
def extract_name_and_grades(grade, bareme, name_index, column, grade_pattern, j):
    if re.search(grade_pattern, str(grade.at[name_index, column])):
        match = re.search(grade_pattern, str(grade.at[name_index, column]))
        template.at[j, "note"] = float(match.group(1))
        template.at[j, "note_sur"] = bareme
        template.at[j, "utilisateur"] = grade.iloc[name_index, 0]
        template.at[j, "note_sur_10"] = round(template.at[j, "note"]*10/template.at[j, "note_sur"], 2)
    else :
        template.at[j, "note"] = grade.at[name_index, column]
        template.at[j, "note_sur"] = bareme
        template.at[j, "utilisateur"] = grade.iloc[name_index, 0]
        template.at[j, "note_sur_10"] = round(template.at[j, "note"]*10/template.at[j, "note_sur"], 2)
#-------------------------------------------------------------------------------------------------------------------------


#Extract questions -------------------------------------------------------------------------------------------------------
def extract_between(file, start_pattern, end_pattern):
    extracted_paragraphs = ""
    file = Document(file)
    is_inside_paragraph = False
    for paragraph in file.paragraphs:
        if re.search(end_pattern, paragraph.text):
            break
        if re.search(start_pattern, paragraph.text):
            is_inside_paragraph = True
        if is_inside_paragraph:
            extracted_paragraphs += ("\n" + paragraph.text)

    return extracted_paragraphs
# ------------------------------------------------------------------------------------------------------------------------


#Extraction --------------------------------------------------------------------------------------------------------------
def extraction(grade, subject_Folder, subject, students_answer_Folder):
    file = pd.read_excel(grade)
    grade_pattern = r"Grade:\s*(\d+\.?\d*)"
    target_columns = get_question_grade(file, grade_pattern) #Take the list of cells who contains the grades 
    start_pattern, end_pattern = get_patterns(subject_Folder + subject) #Take the patterns
    j,k = 0,0 #For looping the row and filling baremes
    for name_index in range(file.shape[0]):
        for column in target_columns:
            extract_bareme(column, j) #Take baremes and fill these into the file
            extract_name_and_grades(file, template.at[k, "note_sur"], name_index, column, grade_pattern, j) #Extract name and grades
            template.at[j, "enonce"] = extract_between(subject_Folder + subject, start_pattern[k], end_pattern[k]) #Extract questions
            answer_Folder = students_answer_Folder + file.iloc[name_index][0] + "/"
            template.at[j, "reponse_apprenant"] = extract_between(answer_Folder + get_file(answer_Folder), start_pattern[k], end_pattern[k])
            if k>len(target_columns)-2:
                k = 0
            else :
                k += 1
            j += 1
    template.to_excel("tmplt.xlsx")
# ------------------------------------------------------------------------------------------------------------------------