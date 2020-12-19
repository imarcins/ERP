from model.crm import crm
from view import terminal as view

CRM_LABELS = ["id", "name", "email", "subscribed"]

def list_customers():
    list_of_lists = crm.crmcsv_to_list_of_lists()
    view.print_table(list_of_lists, CRM_LABELS)

def add_customer():
    customer_data = view.get_inputs(CRM_LABELS)
    crm.add_customer(customer_data)

def update_customer():
    update_labels = ["customer index", "data index", "new info"]
    update_info = view.get_inputs(update_labels)
    crm.update_customer(update_info)

def delete_customer():
    customer_index = view.get_input("customer index")
    crm.delete_customer(customer_index)


def get_subscribed_emails():
     subs_mails = crm.get_subscribed_emails()
     view.print_general_results(subs_mails, "subscribers mails")


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
