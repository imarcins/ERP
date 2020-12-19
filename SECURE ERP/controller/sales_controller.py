from model.sales import sales
from view import terminal as view
from datetime import datetime
#labels są wykorzystywane w przypadku funkcji add_transaction do input
TRANSACTION_DATES = ["Please choose the date you want to start from:", "Please choose the ending date: "]

TRANSACTION_LABELS = ["Please write the customers ID: ", "Please write the product name: ", "Please write the price: "]
UPDATE_OPTIONS = {
    "customer id" : 1,
    "product name": 2,
    "price": 3
}
headers = ["Id", "Customer", "Product", "Price", "Date"]

def list_transactions():
    list_of_lists = sales.sales_to_list_of_lists()
    view.print_table(list_of_lists,headers)

#Funkcja która przyjmuję input od użytkownika w celu dodania transakcji 
def add_transaction():
    #print(write_table_to_file(sales.csv, table, separator=';')) 
   
    customer_id, product_name, price = view.get_inputs(TRANSACTION_LABELS)
    try:
        price = float(price)
    except ValueError:
        print("You can only use numbers")
        add_transaction()
    sales.add_transaction(customer_id, product_name, price)
    
#Funkcja która przyjmuję input na podstawie transaction ID w celu zmiany już istniejącej transakcji. 
def update_transaction():
    transaction_id = view.get_input("Please choose a transaction ID you want to update")

    try:
        index, product_list = sales.look_for_product_list(transaction_id)
        print(*product_list)
        change_info = view.get_input("Please choose what you want to change in the information").lower()
        if change_info in UPDATE_OPTIONS:
            new_info = view.get_input("Enter new information")
            sales.update_transaction(index, UPDATE_OPTIONS[change_info], new_info)

    except:

        view.print_error_message("Invalid ID")
        update_transaction()




def delete_transaction():
    delete_id = view.get_input("Please choose a transaction ID you want to delete")
    
    try:
        index, product_list = sales.look_for_product_list(delete_id)
        print(*product_list)
        check_answer = view.get_input("Are you sure you want delete this transaction?")
        if check_answer == "yes":
            sales.delete_transaction(index)
        else:
            delete_transaction()
    except: 
        view.print_error_message("Invalid ID")
        delete_transaction()


def get_biggest_revenue_transaction():
    print(*sales.biggest_transaction())

def get_biggest_revenue_product():
    product_name, price = sales.product_transaction()
    print(f"{product_name}: {price}")

def count_transactions_between():
    print("YYYY-MM-DD")
    starting_date, ending_date = view.get_inputs(TRANSACTION_DATES)
    starting_split = starting_date.split("-")
    ending_split = ending_date.split("-")
    int_starting_split = list(map(int, starting_split))
    int_ending_split = list(map(int, ending_split))
    starting_date_time = datetime(*int_starting_split)
    ending_date_time = datetime(*int_ending_split)
    if starting_date_time > ending_date_time:
        view.print_error_message("Invalid dates")
        count_transactions_between()
    else:
        print(sales.count_transactions(starting_date_time, ending_date_time))
    



def sum_transactions_between():
    print("YYYY-MM-DD")
    starting_date, ending_date = view.get_inputs(TRANSACTION_DATES)
    starting_split = starting_date.split("-")
    ending_split = ending_date.split("-")
    int_starting_split = list(map(int, starting_split))
    int_ending_split = list(map(int, ending_split))
    starting_date_time = datetime(*int_starting_split)
    ending_date_time = datetime(*int_ending_split)
    if starting_date_time > ending_date_time:
        view.print_error_message("Invalid dates")
        sum_transactions_between()
    else:
        print(sales.sum_transactions(starting_date_time, ending_date_time))

def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)