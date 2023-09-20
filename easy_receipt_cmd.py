import sys
from generatepdf import generate_pdf_invoice
from database_settings import get_results_from_query, get_all_ids
import datetime
from generate_excel import invoice_to_excel


item1 = ''
query_list = get_all_ids()

results = get_results_from_query(int(2))

today_date = datetime.date.today()
company_email = results[0]
address = results[1]
company_name = results[2]
zip_code = results[3]
image = str(results[4])
account_num = results[5]
routing_num = results[6]

invoice_number = sys.argv[1]
client_name = sys.argv[2]
items = input('How many items do you want to add to your receipt?')
itemdictionary = {}
total = 0
for i in range(int(items)):
    item = input('Describe your item:')
    value = int(input('Put the value here:'))
    total += int(value)

    itemdictionary[item] = value


context = {'client_name': client_name,
           'items': itemdictionary,
           'invoice_number': invoice_number,
           'today_date': today_date,
           'company_name': company_name,
           'company_email': company_email,
           'address': address,
           'zip_code': zip_code,
           'image': image,
           'account_num': account_num,
           'routing_num': routing_num,
           'total': total
           }


invoice_to_excel(context)
generate_pdf_invoice(context)