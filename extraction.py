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
def extract_bareme(grade, grade_pattern):
    max_Grade_pattern = r"Max grade:\s*(\d+)"
    grades_column_name = get_question_grade(grade, grade_pattern)
    i = 0
    for column in grades_column_name:
        if re.search(max_Grade_pattern, column):
            match = re.search(max_Grade_pattern, column)
            template.at[i, "note_sur"] = float(match.group(1))
            i += 1
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
def extraction(grade, subject_Folder, subject):
    file = pd.read_excel(grade)
    grade_pattern = r"Grade:\s*(\d+\.?\d*)"
    extract_bareme(file, grade_pattern)
    target_columns = get_question_grade(file, grade_pattern)
    start_pattern, end_pattern = get_patterns(subject_Folder + subject)
    j,k = 0,0
    for name_index in range(file.shape[0]):
        for column in target_columns:
            extract_name_and_grades(file, template.at[k, "note_sur"], name_index, column, grade_pattern, j)
            template.at[j, "enonce"] = extract_between(subject_Folder + subject, start_pattern[k], end_pattern[k])
            #extract_questions()
            if k>len(target_columns)-2:
                k = 0
            else :
                k += 1
            j += 1
    template.to_excel("tmplt.xlsx")
# ------------------------------------------------------------------------------------------------------------------------