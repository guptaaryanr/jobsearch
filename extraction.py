import requests
import os
import csv

year = input("Year: ")
URL = "https://www.uscis.gov/sites/default/files/document/data/h1b_datahubexport-" + year + ".csv"
filename = "h1b_" + year + ".csv"

def download():
    if(int(year) < 2009 or int(year) > 2022):
        exit("Error")
    response = requests.get(URL)
    open(filename, "wb").write(response.content)

def delete_file():
    if os.path.exists(filename):
        os.remove(filename)
    else:
        exit("Error")

def applications():
    file = open(filename)
    csvreader = csv.reader(file, delimiter = ",")
    approvals, denials = 0, 0
    employer = input("Employer: ")
    for row in csvreader:
        if employer == row[1]:
            approvals += int(row[2]) + int(row[4])
            denials += int(row[3]) + int(row[5])
    if(approvals == 0 and denials == 0):
        print("Company not available")
    print("Approvals: ", approvals)
    print("Denials: ", denials)


download()
applications()
delete_file()