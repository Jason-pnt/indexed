from git import Repo
import os
import subprocess
import sys
import time
from shutil import copyfile
current_path=(os.path.abspath(__file__))
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
repo = Repo(os.path.abspath(father_path))
time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
commitName = ('Checking keyword whether amazon indexed ')
commitName = commitName + time_now
repo.index.add(['test.csv'])
repo.index.commit(commitName)
subprocess.check_call(['git', 'push', 'origin', 'master'])