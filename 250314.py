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


#Python reading files (.txt,.json,.csv)
import json
import csv
file_path = "C:/Users/Administrator/Desktop/input.csv"
try:
    with open(file_path,"r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
        #content = json.load(file)
        #content = file.read()
        #print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")

import datetime

date = datetime.date(2025,1,2)
today = datetime.date.today()

time = datetime.time(12,30,0)
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %m-%d-%Y")

target_datetime = datetime.datetime(2030,1,2,12,30,1)
current_datetime = datetime.datetime.now()
print(target_datetime)
print(current_datetime)
if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has NOT passed")


print(today)
print(time)
print(now)

'''



































