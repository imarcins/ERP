import operator
from model import data_manager, util
from typing import List
# from datetime import date
# from datetime import datetime

DATAFILE = "model/hr/hr.csv"
headers = ["Id", "Name", "Date of birth", "Department", "Clearance"]

YEARS_OLD = 0
NAME_INDEX=1
DOB_INDEX=2
DEPARTMENT_INDEX=3
CLEARANCE_INDEX=4
CURRENT_YEAR=2020

def get_employee():
    read_table = data_manager.read_table_from_file("model/hr/hr.csv")
    
    return list(read_table)

def add_employee( arguments):
    list_of_employes= get_employee()
    Id = util.generate_id()
    arguments[0] = Id
    list_of_employes.append(arguments)
    
    new_list = data_manager.write_table_to_file(DATAFILE,list_of_employes)
    return new_list



def update_element(index:int, index_options:int, new_info:str):
    list_of_lists = get_employee()[1:] #bez header czyta
    list_of_lists[index][index_options] = new_info
    data_manager.write_table_to_file(DATAFILE, list_of_lists)


def show_employee(date_id:str):
    list_of_lists = get_employee()[1:] #bez header czyta
    for index, employee_list in enumerate(list_of_lists):
        if date_id in employee_list: 
            return index, list_of_lists[index]

def delete_employee(index:int):
    list_of_lists = get_employee()[1:]
    del list_of_lists[index]
    data_manager.write_table_to_file(DATAFILE, list_of_lists)

def convert_date(a):
    return a
    # return list(map(int,a.split("-")))

def date_1(list_of_employee):
    total_employee = get_employee()
    employes_birth = []
    for i in range(len(total_employee)):
        a = total_employee[i][DOB_INDEX]
        a = a.split("-")
        employes_birth.append(a)
    return employes_birth
    
        
    




