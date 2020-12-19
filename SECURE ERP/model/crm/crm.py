""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]


def crmcsv_to_list_of_lists():
    read_table = data_manager.read_table_from_file(DATAFILE)
    return list(read_table)


def add_customer(customer_data:list):
    list_of_crm = crmcsv_to_list_of_lists()
    list_of_crm.append(customer_data)
    data_manager.write_table_to_file(DATAFILE, list_of_crm)


def update_customer(update_info:list):
    customer_index = int(update_info[0])
    data_index = int(update_info[1])
    new_info = update_info(2)
    list_of_crm = crmcsv_to_list_of_lists()
    list_of_crm[customer_index][data_index] = new_info
    data_manager.write_table_to_file(DATAFILE, list_of_crm)


def delete_customer(customer_index):
    customer_index = int(customer_index)
    list_of_crm = crmcsv_to_list_of_lists()
    del list_of_crm[customer_index]
    data_manager.write_table_to_file(DATAFILE, list_of_crm)


def get_subscribed_emails():
    subs_mails = []
    list_of_crm = crmcsv_to_list_of_lists()
    for customer in list_of_crm:
        if customer[3] == "1":
            subs_mails.append(customer[2])
    return subs_mails
    
