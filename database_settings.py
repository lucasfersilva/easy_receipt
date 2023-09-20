from tinydb import TinyDB
from tinydb import Query
db = TinyDB('data/db.json')

#db.insert({'id': 1, 'name': 'INSERT NAME','address': 'INSERT ADDRESS.','company_email':'INSERT COMPANY EMAIL',
#           'zip_code': 000,'IMG_URL':'INSERT IMG URL HERE', "account_number": 000,"routing_number": 0000})

#db.insert({"id": 2,"name": "Lucas Fernandes", "address": "github@lucasfersilva", "company_email": "lucasfersilva", "zip_code": 27197000,"img_url":"https://i.pinimg.com/236x/2b/dd/c9/2bddc91accccb9b70178c49cf5684bed.jpg",
# "account_number": 000,"routing_number": 0000})

company_name = ''
address = ''
company_email = ''
zip_code = 0


def get_all_ids():
    results = Query()
    x = db.all()

    query_list = []
    for i in x:
        query_list.append(i['id'])

    return query_list


def get_results_from_query(id):
    results = Query()
    x = db.search(results.id == id)
    for i in x:
        company_email = i['company_email']
        address = i['address']
        company_name = i['name']
        zip_code = i['zip_code']
        img_url = i['img_url']
        account_num = i['account_number']
        routing_num = i['routing_number']
    return company_email, address , company_name, zip_code, img_url, account_num, routing_num


print(get_results_from_query(2))

