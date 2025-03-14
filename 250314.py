''''
# Python writing files (.txt,.json,.csv)
import json
import csv
txt_data = "I like pizza!"
#employees = {
#    "name" : "Spongebob",
#    "age" : 30,
#    "job" : "cook"
#}

employees = [["Name","Age","Job"],
             ["Spongebob",30,"Cook"],
             ["Patrick",37,"Unemployed"],
             ["Sandy",27,"Scientist"]]

#employees =["Eugene","Squidward","Spongebob","Patrick"]
file_path = "C:/Users/Administrator/Desktop/output.csv"
try:
    with open(file_path, "w",newline = "") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        #json.dump(employees,file,indent = 4)
        #file.write(txt_data)
        #for employee in employees:
        #    file.write(employee + " ")
        print(f"csv file '{file_path}'was created.")
except FileExistsError:
    print("That file already existis!")
'''

#Python reading files (.txt,.json,.csv)



