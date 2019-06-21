import dataset
from reports import get_reports
import os
import random

def update():
    filename = random.randint(100000000,999999999)
    os.popen('cp reports.db %s.db'%(filename)) 
    db = dataset.connect("sqlite:///%s.db"%(filename))
    reportsdb = db["reports"]
    reports = get_reports()
    for report in reports:
        reportsdb.upsert(report,["report_link"])
    return filename