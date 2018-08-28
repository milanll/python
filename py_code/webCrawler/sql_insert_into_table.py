
from parse_item import get_items_from_500			#get_items_from_500()
from sql_manage import sql_insert_into_table		#sql_insert_into_table(table_name,dict_item)

dict_items = get_items_from_500()

sql_insert_into_table('table_4',dict_items)