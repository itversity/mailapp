from datetime import datetime as dt
import random
import os
from faker import Faker
import logging
import pymongo


def gen_test_data():
    logging.info('Generating test data')
    recs = []
    faker = Faker()
    events = ['Birth Day', 'Marriage Anniversary']
    for i in range(1, 366):
        for year in [2001, 2002, 2003]:
            fn = faker.first_name()
            ln = faker.last_name()
            m = f'dgadiraju+{fn.lower()}{i}{year}@gmail.com'
            d = dt.strptime(f'{year}{i}', '%Y%j')
            e = random.choice(events)
            recs.append({
                'fn': fn,
                'ln': ln,
                'm': m,
                'month': d.month,
                'day': d.day,
                'e': e
            })
    return recs


def load_mongo_coll(recs):
    logging.info('Populating Mongo Collection with test data')
    mongo_host = os.environ.get('MONGO_HOST')
    mongo_port = int(os.environ.get('MONGO_PORT'))
    client = pymongo.MongoClient(mongo_host, mongo_port)
    db = client['mailer']
    coll = db['mails']
    coll.insert_many(recs)


def validate_mongo_coll(filter_date=None):
    logging.info('Validate Mongo Collection')
    if not filter_date:
        filter_date = dt.now().date()
    month = filter_date.month
    day = filter_date.day
    mongo_host = os.environ.get('MONGO_HOST')
    mongo_port = int(os.environ.get('MONGO_PORT'))
    client = pymongo.MongoClient(mongo_host, mongo_port)
    db = client['mailer']
    coll = db['mails']
    for doc in coll.find({'month': month, 'day': day}):
        print(doc)


def cleanup_mongo_coll():
    logging.info('Cleanup Mongo Collection')
    mongo_host = os.environ.get('MONGO_HOST')
    mongo_port = int(os.environ.get('MONGO_PORT'))
    client = pymongo.MongoClient(mongo_host, mongo_port)
    db = client['mailer']
    coll = db['mails']
    coll.delete_many({})        


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO, 
        format='%(levelname)s %(asctime)s %(message)s',
        datefmt='%Y-%m-%d %I:%M:%S %p'
    )
    recs = gen_test_data()
    cleanup_mongo_coll()
    load_mongo_coll(recs)
    validate_mongo_coll()
