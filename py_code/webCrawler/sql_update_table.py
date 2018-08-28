from sql_manage import sql_update_table			#sql_update_table(table_name,dict_item)
from parse_item import get_items_from_500		#get_items_from_500()

dict_items = get_items_from_500()

sql_update_table('table_2', dict_items)