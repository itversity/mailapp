import os
import pymongo
import logging
from datetime import datetime as dt
from sendgrid import SendGridAPIClient
from send_mail import send_greeting


def main():
    logging.basicConfig(
        level=logging.INFO, 
        format='%(levelname)s %(asctime)s %(message)s',
        datefmt='%Y-%m-%d %I:%M:%S %p'
    )
    mongo_host = os.environ.get('MONGO_HOST')
    mongo_port = int(os.environ.get('MONGO_PORT'))
    from_email = os.environ.get('FROM_EMAIL')
    sg_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    client = pymongo.MongoClient(mongo_host, mongo_port)
    db = client['mailer']
    coll = db['mails']
    filter_date = dt.now().date()
    month = filter_date.month
    day = filter_date.day
    for rec in coll.find({'month': month, 'day': day}):
        logging.info(f'Sending email for {rec["_id"]}')
        subject = f'Happy {rec["e"]}'
        body = '''
            Dear {first_name},
            <br>
            Wish you a <strong>Happy {event}</strong>. Here is a 10$ discount coupon code <strong>CHEERS</strong>.
            <br>
            Regards,
            ITVersity Team
        '''
        body = body.format(first_name=rec['fn'], event=rec['e'])
        send_greeting(sg_client, from_email, rec['m'], subject, body)


if __name__ == '__main__':
    main()