from model.hr import hr
from view import terminal as view
from datetime import datetime

headers = ["Id", "Name", "Date of birth", "Department", "Clarence"]
UPDATE_OPTIONS = {
    "name" : 1,
    "date of birth": 2,
    "department": 3
}

def list_employees():
    list_of_lists = hr.get_employee()
    view.print_table(list_of_lists,headers)



def add_employee():
    # u_id = "Please write an Id: "
    # generate_id = view.get_input(u_id)
    
    new_line = view.get_inputs(["Please write an ID: ", "Please write a name: ", "Please write date of birth: ", "Please write a department: ", "Please write a clarence: "])
    hr.add_employee(new_line)



def update_employee():
    transaction_id = view.get_input("Please choose a employee ID you want to update")

    try:
        index, product_list = hr.show_employee(transaction_id)
        print(*product_list)
        change_info = view.get_input("Please choose what you want to change in the information").lower()
        if change_info in UPDATE_OPTIONS:
            new_info = view.get_input("Enter new information")
            hr.update_element(index, UPDATE_OPTIONS[change_info], new_info)

    except:

        view.print_error_message("Invalid ID")
        update_employee()

def delete_employee():

     delete_id = view.get_input("Please choose a transaction ID you want to delete")
     try:
    
            index, product_list = hr.show_employee(delete_id)
            print(*product_list)
            check_answer = view.get_input("Are you sure you want delete this transaction?").lower()
            if check_answer == "yes":
                hr.delete_employee(index)
            else:
                view.print_menu()
     except:

            view.print_error_message("Invalid ID")
            view.print_menu()


def get_oldest_and_youngest():
    convert_dates =[]
    list_of_employes = hr.get_employee()
    for i in range(len(list_of_employes)):
        convert_dates.append(hr.convert_date(list_of_employes[i][hr.DOB_INDEX]))

    names = (list_of_employes[convert_dates.index(min(convert_dates))][1],list_of_employes[convert_dates.index(max(convert_dates))][1])
    view.print_general_results(names, "The oldest and the youngest employes are")



def get_average_age():
    list_of_employes = hr.get_employee()
    employee_birthday = hr.date_1(list_of_employes)
    total_age= 0
    for i in range(len(employee_birthday)):
        years = int(employee_birthday[i][hr.YEARS_OLD])
        total_age+= hr.CURRENT_YEAR- years
    
    view.print_general_results(total_age/len(list_of_employes), "Employees average age is")
    

def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    list_of_employes= hr.get_employee()
    employes_with_clearance = 0
    number = int(view.get_input("Please write a clearence level: "))
    for i in range(len(list_of_employes)):
        if int(list_of_employes[i][hr.CLEARANCE_INDEX]) <= number:
            employes_with_clearance +=1
    view.print_general_results(employes_with_clearance, "Number of employeees with required clearance level")
    
    


def count_employees_per_department():
    list_of_employes = hr.get_employee()
    emp_per_dep = {}
    for i in range(len(list_of_employes)):
        if list_of_employes[i][hr.DEPARTMENT_INDEX] in emp_per_dep:
            emp_per_dep[list_of_employes[i][hr.DEPARTMENT_INDEX]]+=1
        else:
            emp_per_dep[list_of_employes[i][hr.DEPARTMENT_INDEX]] =1
    view.print_general_results(emp_per_dep, "Employees per department")
    


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
