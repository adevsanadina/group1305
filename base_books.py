from pymongo.mongo_client import MongoClient
from pprint import pprint
from confing import USER_NAME,PASSWORD

uri = f"mongodb+srv://{USER_NAME}:{PASSWORD}@cluster1305.9j8xcrc.mongodb.net/?retryWrites=true&w=majority&appName=cluster1305"

# Create a new client and connect to the server
client = MongoClient(uri)

db = client['new_db_books']

fantasy_coll = db['fantasy_literature']
school_coll = db['school_literature']

fantasy_books = [
    {'title': 'Володар перстнів:Повернення короля',
     'cost': 425,
     'year_of_writing': 1955,
     'number_of_pages': 704
    },
    {'title': 'Доктор Сон',
     'cost': 360,
     'year_of_writing': 2013,
     'number_of_pages': 640
     },
    {'title': 'Творець заклинань',
     'cost': 550,
     'year_of_writing': 2020,
     'number_of_pages': 480
     },
    {'title': 'Учень убивці',
     'cost': 350,
     'year_of_writing': 1955,
     'number_of_pages': 448
    },
    {'title': 'Клинок королеви:Танок із тінями',
     'cost': 288,
     'year_of_writing': 2023,
     'number_of_pages': 688
     },
    {'title': 'Хребет Дракона',
     'cost': 549,
     'year_of_writing': 2023,
     'number_of_pages': 560
     }
]

fantasy_coll.insert_many(fantasy_books)
fantasy_coll.insert_one({'title': 'Гра престолів','cost': 425,'year_of_writing': 1996,'number_of_pages': 864})

school_books = [
    {'title': 'Хімія',
     'class': 11,
     'number_of_pages': 208
    },
    {'title': 'Українська мова',
     'class': 11,
     'number_of_pages': 210
     },
    {'title': 'Астрономія',
     'class': 11,
     'number_of_pages': 288
     },
    {'title': 'Англійська мова',
     'class': 11,
     'number_of_pages': 256
    },
    {'title': 'Історія України',
     'class': 11,
     'number_of_pages': 258
     },
    {'title': 'Поза межами болю',
     'class': 11,
     'number_of_pages': 176
     },
    {'title': 'Уявний друг',
     'class': 11,
     'number_of_pages': 704
     }
]

school_coll.insert_many(school_books)

result = list(school_coll.find({'title': {'$regex': 'Історія*'}}))
pprint(result)

