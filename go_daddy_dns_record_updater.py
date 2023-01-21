#!/usr/bin/env python3

# Full package imports
import sys
import logging
import schedule
import time
from datetime import datetime
import os
import logging
from logging.handlers import RotatingFileHandler

log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')

os.system('mkdir -p ./log')
logFile = './log/dns_scheduler.log'

my_handler = RotatingFileHandler(logFile, mode='a', maxBytes=5*1024*1024,
                                 backupCount=2, encoding=None, delay=0)
my_handler.setFormatter(log_formatter)
my_handler.setLevel(logging.INFO)

log = logging.getLogger('root')
log.setLevel(logging.INFO)

log.addHandler(my_handler)

import pif
# Partial imports
from godaddypy import Client, Account

myDomain = '<DOMAIN>'
myRecord = '<SUB DOMAIN>'

PUB_KEY = ''
SEC_KEY = ''

recordType = 'A'

userAccount = Account(api_key=PUB_KEY, api_secret=SEC_KEY)
userClient = Client(userAccount)
publicIP = 'IP ADDR'

def update_dns_record():
    log.info('Current ipv4: ' + publicIP)
    try:
        records = userClient.get_records(myDomain, name=myRecord, record_type=recordType)
        log.info(records)
        # us = userClient.delete_records(myDomain, name=myRecord)
        # log.info(us)
        if len(records):
            for record in records:
                if publicIP != record["data"]:
                    updateResult = userClient.update_record_ip(publicIP, myDomain, myRecord, recordType)
                    if updateResult is True:
                        log.info('Update ended with no Exception.')
                else:
                    log.info('No DNS update needed.')
        else:
            userClient.add_record(myDomain, {'data':publicIP,'name':myRecord,'ttl': 600, 'type':recordType})
            log.info('DNS created with no Exception ' + myRecord + '.' + myDomain)
    except:
        log.error(sys.exc_info()[1])
        sys.exit()

def job():
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %h:%M:%S")
    log.info("Schedule started")
    update_dns_record()


schedule.every(5).seconds.do(job)
log.info("Main service started")
while True:
    schedule.run_pending()
    # time.sleep(0)