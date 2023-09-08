import pandas as pd
import os 
#from docx import Document 
import re
from fill_variables import *
from patterns import *

# Variables ----------------------------------------------------------------------------------------------------------
subject_Folder = "subject/"
reference_answer_Folder = "reference_answer/"
students_answer_Folder = "students_answer/"
grades_Folder = "grades/"

#patterns_Begin, pattern_End = get_patterns(get_patterns(subject_Folder + get_file(reference_answer_Folder)))

ecole = "EDHEC"
langue = ""
annee = ""
session = ""
competence = ""
# --------------------------------------------------------------------------------------------------------------------

#print(get_folder(students_answer_Folder))