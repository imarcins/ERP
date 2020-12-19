import operator
from model import data_manager, util
from typing import List
from datetime import datetime

#plik który przekształca  plik sales.csv w list of lists
FILE_NAME = "model/sales/sales.csv"
def sales_to_list_of_lists() -> List[List[str]]:
    read_table = data_manager.read_table_from_file(FILE_NAME)
    
    return read_table
#Funkcja która nadpisuje naszą liste w listach z nową transakcją 
def add_transaction(customer:str, product:str, price:float) -> List[List[str]]:
    list_of_lists = sales_to_list_of_lists()[1:]
    date,_ = datetime.now().isoformat().split("T")
    new_transaction = [util.generate_id(), customer, product, str(price), date]
    list_of_lists.append(new_transaction)
    data_manager.write_table_to_file(FILE_NAME, list_of_lists)
    return list_of_lists


def look_for_product_list(product_id:str) -> str:
    list_of_lists = sales_to_list_of_lists()[1:]
    for index, sales_list in enumerate(list_of_lists):
        if product_id in sales_list: 
            return index, list_of_lists[index]
        

def update_transaction(index:int, index_options:int, new_info:str):
    list_of_lists = sales_to_list_of_lists()[1:]
    list_of_lists[index][index_options] = new_info
    data_manager.write_table_to_file(FILE_NAME, list_of_lists)

def delete_transaction(index:int):
    list_of_lists = sales_to_list_of_lists()[1:]
    del list_of_lists[index]
    data_manager.write_table_to_file(FILE_NAME, list_of_lists)

def biggest_transaction():
    list_of_lists = sales_to_list_of_lists()[1:]
    biggest_price = 0 
    for index,item in enumerate(list_of_lists): 
        current_price = float(item[3])
        if biggest_price < current_price:
            index_of_biggest_price = index
            biggest_price = current_price
    return list_of_lists[index_of_biggest_price]

def product_transaction():
    list_of_lists = sales_to_list_of_lists()[1:]
    product_price = {}
    for item in list_of_lists:

        product_name = item[2]
        price = item[3]
        if product_name in product_price:
            product_price[product_name] = float(product_price[product_name]) + float(price)

        else:
            product_price[product_name] = float(price)
    
    biggest_key = max(product_price.items(), key=operator.itemgetter(1))[0]
    return biggest_key, product_price[biggest_key]

def count_transactions(starting_date_time, ending_date_time):
    list_of_lists = sales_to_list_of_lists()[1:]
    count_transaction = 0 
    for item in list_of_lists:
        date = item[-1]
        date_split = date.split("-")
        int_date_split = list(map(int, date_split))
        date_time = datetime(*int_date_split)
        if date_time >= starting_date_time and date_time <= ending_date_time:
            count_transaction += 1
    return count_transaction


def sum_transactions(starting_date_time, ending_date_time):
    list_of_lists = sales_to_list_of_lists()[1:]
    sum_transaction = 0 
    for item in list_of_lists:
        price = float(item[3])
        date = item[-1]
        date_split = date.split("-")
        int_date_split = list(map(int, date_split))
        date_time = datetime(*int_date_split)
        if date_time >= starting_date_time and date_time <= ending_date_time:
            sum_transaction += price
    return sum_transaction

