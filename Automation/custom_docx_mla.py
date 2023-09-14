import os, sys
from datetime import date
from docx import Document
from docx.shared import Pt

months = ["January", "February", "March", "April", "May", "June", "July",  "August", "September", "October", "November", "December"]
path = "C:\\Users\\dylan\\My Drive\\School\\21_TCS"

def main():
    if len(sys.argv) == 1:
        print("Error: No filename given")
        return
    
    teacher = sys.argv[1]
    if teacher.lower() == "lim":
        teacher = "Mrs. Lim"
        subject = "Humanities"
    elif teacher.lower() == "wynne":
        teacher = "Mrs. Wynne"
        subject = "Humanities"
    elif teacher.lower() == "walker":
        teacher = "Mr. Walker"
        subject = "Humanities"
    elif teacher.lower() == "finley":
        teacher = "Mr. Finley"
        subject = "Latin"
    elif teacher.lower() == "reimer":
        teacher = "Mr. Reimer"
        subject = "Chemistry"
    else:
        print("Error: Invalid teacher argument")
        return

    tmp = str(date.today()).replace("-","")
    cal = f"{months[int(tmp[4:6])-1]} {int(tmp[-2:])}, {tmp[:4]}"
    title = " ".join(x.title() for x in sys.argv[2:])
    ptitle = f"{str(date.today())[5:]}-{str(date.today())[:4]} " + title.replace(" ", "") + " " + subject
    package = ["Dylan Wynne", teacher, subject, cal, title]

    doc = Document(f"{path}\\mla.docx")
    doc._body.clear_content()

    for item in package:
        p = doc.add_paragraph(item)
        if item == title:
            p.alignment = 1
        else:
            p.paragraph_format.first_line_indent = Pt(0)
        

    try:
        doc.save(f"{path}\\{subject}\\{ptitle}.docx")
    except:
        return

    os.chdir("C:\\Program Files\\Microsoft Office\\root\\Office16")
    os.system(f"winword /t \"{path}\\{subject}\\{ptitle}.docx\"")

if __name__ == "__main__":
    main()