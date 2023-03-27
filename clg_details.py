import json
import csv

with open ("eng_clg_in_india.csv", "r") as f:
    reader = csv.DictReader(f)
    next(reader)
    data = { }
    for rows in reader:
        key = rows['College Name']
        data[key] = rows
        
with open ("college.json", "w") as f:
    json.dump(data, f, indent=4)


# wite a pogram to read the data from the json file and print the college name and address of the college based on the user input

# Path: clg_details.py
import json

with open ("college.json", "r") as f:
    data = json.load(f)
    clg_name = input("Enter the college name: ")
    print("College Name : ", data[clg_name]['College Name'])
    print("Genders Accepted : ", data[clg_name]['Genders Accepted'])
    print("Total Student Enrollments : ", data[clg_name]['Total Student Enrollments'])
    print("Total Faculty : ", data[clg_name]['Total Faculty'])
    print("Established Year : ", data[clg_name]['Established Year'])
    print("Rating : ", data[clg_name]['Rating'])
    print("University : ", data[clg_name]['University'])
    print("Courses : ", data[clg_name]['Courses'])
    print("Facilities : ", data[clg_name]['Facilities'])
    print("City : ", data[clg_name]['City'])
    print("State : ", data[clg_name]['State'])
    print("Country : ", data[clg_name]['Country'])
    print("Campus Size : ", data[clg_name]['Campus Size'])
    print("College Type : ", data[clg_name]['College Type'])
    print("Average Fees : ", data[clg_name]['Average Fees'])

       
