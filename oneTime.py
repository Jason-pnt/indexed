from git import Repo
import os
import subprocess
import sys
import time
import datetime
import pytz
from shutil import copyfile
current_path=(os.path.abspath(__file__))
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")

repo = Repo(os.path.abspath(father_path))
pdt_timezone=pytz.timezone("America/Los_Angeles")

time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
dates = time.strftime("%Y-%m-%d", time.localtime())
flags = True
while flags:
    for i in (os.listdir(os.path.join(father_path,'keyword'))):
        pdt_times = datetime.datetime.now(pdt_timezone).strftime("%Y-%m-%d %H:%M:%S")
        if i.endswith('xlsx'):
            print(i+'\n')
            commitName = (i.split('.')[0])
            commitName = commitName + ' ' + pdt_times
            copyfile(os.path.join(father_path, 'keyword', i), os.path.join(father_path, 'test.xlsx'))
            repo.index.add(['*'])
            repo.index.commit(commitName)
            subprocess.check_call(['git', 'push', 'origin', 'master'])
            time.sleep(2)
    flags = False