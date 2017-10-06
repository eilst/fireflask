#!/usr/bin/env python
import csv
import os
import re
import pyrebase

config = {
    "apiKey": os.environ['API_KEY'],
    "authDomain": os.environ['AUTHDOMAIN'],
    "databaseURL": os.environ['DBUTL'],
    "storageBucket": os.environ['SBUCKET']
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
def populate(csvfile):
    data = csv.reader(open(csvfile, encoding="latin-1"))
    fields = next(data)
    for row in data:
        """remove any character  []#/.$ in key ==> firebase requirement """
        item = {re.sub('[#/.$]', '', row[2]) : row[2]}
        """update() will not duplicate any item"""
        db.child(row[0]).child(row[1]).update(item)
        print(data)


populate("catalogo.csv")

