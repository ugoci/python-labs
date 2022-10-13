# Write the file counts to a `.csv` file.
import csv

#count = {"": 8, ".csv": 2, ".md": 2, ".png": 11}
#with open("filecounts.csv", "a") as csvfile:
#    countwriter = csv.writer(csvfile)
#    data = [count[""], count[".csv"], count[".md"], count[".png"]]
#    countwriter.writerow(data)
#    print(data)

#****************
#emplist = []
#for value in count.values():
#    emplist.append(value)
#print(emplist)

with open("filecounts.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=["Folder", "CSV", "MD", "PNG"])
    counts = list(reader)

print(counts)