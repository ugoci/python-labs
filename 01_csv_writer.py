# Add your file counter code here.
# Then add more code that writes the file counts to a `.csv` file.
import pathlib
import csv

mydesktop = pathlib.Path("C:/Users/Ugo/Desktop")

#dictionary list below:
dict1 = {"ppt": ""}
dict2 = {"docs": ""}
dict3 = {"pdfs": ""}
dict4 = {"other docs": ""}

dict_list = []

#file counters below:
ppt_counter = 0 
doc_counter = 0 
pdf_counter = 0
other_counter = 0

#code block below:
for filepath in mydesktop.iterdir():
    #print(filepath)
    if filepath.suffix == ".pptx":
        ppt_counter = ppt_counter + 1
        dict1["ppt"] = ppt_counter
        dict_list.append(dict1)
    elif filepath.suffix == ".docx":
        doc_counter = doc_counter + 1
        dict2["docs"] = doc_counter
        dict_list.append(dict2)
    elif filepath.suffix == ".pdf":
        pdf_counter = pdf_counter + 1
        dict3["pdfs"] = pdf_counter
        dict_list.append(dict3)
    else:
        other_counter = other_counter + 1
        dict4["other docs"] = other_counter
        dict_list.append(dict4)

#print(dict_list)

#code to save information to a file 

with open("filecounter_csvfile", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(dict_list)
#    print(data)

#code to read the contents of the file

with open("filecounter_csvfile", "r") as csvfile:
    content = csv.reader(csvfile)
    for i in content:
        #print(content)
        print(i)