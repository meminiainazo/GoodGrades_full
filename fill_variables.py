import os

#Get folder -------------------------------------------------------------------------------------------------------------------
def get_folder(folder):
    folders_Name = os.listdir(folder)
    folders = [folder_Name for folder_Name in folders_Name if os.path.isdir(os.path.join(folder, folder_Name))]
    return folders
# ------------------------------------------------------------------------------------------------------------------------------------------

#Get files ------------------------------------------------------------------------------------------------------------------
def get_file(folder):
    for filename in os.listdir(folder):
        if filename.endswith(".docx") or filename.endswith(".pdf") or filename.endswith(".xlsx"):
            file = filename
    return file
# ----------------------------------------------------------------------------------------------------------------------------------------
