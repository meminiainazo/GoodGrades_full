import pandas as pd
import re
import openpyxl
from fill_variables import *

#Global file ------------------------------------------------------------------------------------------------------------
template = pd.read_excel("template.xlsx")
# -----------------------------------------------------------------------------------------------------------------------

#Get question grade ------------------------------------------------------------------------------------------------------
def get_question_grade(file, grade_pattern):
    target_columns = []
    for column in file.columns.tolist():
        if re.search(grade_pattern, str(file.at[0, column])):
            target_columns.append(column)
    return target_columns
# ------------------------------------------------------------------------------------------------------------------------


#Extract bareme ---------------------------------------------------------------------------------------------------------
def extract_bareme(file, grade_pattern):
    max_Grade_pattern = r"Max grade:\s*(\d+)"
    grades_column_name = get_question_grade(file, grade_pattern)
    i = 0
    for column in grades_column_name:
        if re.search(max_Grade_pattern, column):
            match = re.search(max_Grade_pattern, column)
            template.at[i, "note_sur"] = float(match.group(1))
            i += 1
# ------------------------------------------------------------------------------------------------------------------------

#Extract name and grades -------------------------------------------------------------------------------------------------
def extract_name_and_grades(file):
    file = pd.read_excel(file)
    grade_pattern = r"Grade:\s*(\d+\.?\d*)"
    target_columns = get_question_grade(file, grade_pattern)
    extract_bareme(file, grade_pattern)
    j,k = 0,0
    for name_index in range(file.shape[0]):
        for column in target_columns:
            if re.search(grade_pattern, str(file.at[name_index, column])):
                match = re.search(grade_pattern, str(file.at[name_index, column]))
                template.at[j, "note"] = float(match.group(1))
                template.at[j, "note_sur"] = template.at[k, "note_sur"]
                template.at[j, "utilisateur"] = file.iloc[name_index, 0]
                template.at[j, "note_sur_10"] = round(template.at[j, "note"]*10/template.at[j, "note_sur"], 2)
                if k>=7:
                    k = 0
                else :
                    k += 1
                j += 1
    template.to_excel("tmplt.xlsx")
#-------------------------------------------------------------------------------------------------------------------------