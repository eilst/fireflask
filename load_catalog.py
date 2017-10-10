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
 i = 1
    for row in data:
        """remove any character  []#/.$ in key ==> firebase requirement """
        item = {re.sub('[#/.$]', '', row[2]) : row[2]}
        """update() will not duplicate any item"""
        db.child(row[0]).child(row[1]).update(item)
        """lines in my test file is 881"""
        sys.stdout.write("Upload progress: %d%%   \r" % (int((i/881)*100)))
        sys.stdout.flush()
        i=i+1


populate("catalogo.csv")

