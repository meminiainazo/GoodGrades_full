from docx import Document
from docx.oxml.ns import qn

def has_tables_or_images(doc):
    has_tables = False
    has_images = False

    for element in doc.element.body:
        if element.tag.endswith('tbl'):
            has_tables = True
        elif element.tag.endswith('p'):
            for run in element.findall('.//' + qn('w:drawing')):
                has_images = True

    return has_tables, has_images

def main():
    docx_file_path = 'Etude de cas 2023 - processus commercial Siham hannouda .docx'
    doc = Document(docx_file_path)
    
    has_tables, has_images = has_tables_or_images(doc)
    
    if has_tables:
        print("The document contains tables.")
    else:
        print("The document does not contain any tables.")
    
    if has_images:
        print("The document contains images.")
    else:
        print("The document does not contain any images.")
