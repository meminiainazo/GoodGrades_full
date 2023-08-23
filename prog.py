import pandas as pd
import os 
#from docx import Document 
import re
from fill_variables import *

# Variables ----------------------------------------------------------------------------------------------------------
subject_Folder = "subject/"
reference_answer_Folder = "reference_answer/"
students_answer_Folder = "students_answer/"
grades_Folder = "grades/"
patterns_debut = []
patterns_end = []
# --------------------------------------------------------------------------------------------------------------------

print(get_folder(students_answer_Folder))