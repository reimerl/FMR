import os 
import glob
import pandas as pd
from datetime import datetime

root = os.getcwd()
 
files = glob.glob('*\*\*\*')

stats = [os.stat(file) for file in files]
ctime_list = [datetime.fromtimestamp(stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S') for stat in stats]
mtime_list = [datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S') for stat in stats]
extensions = [f.split('.')[-1] for f in files]

df = pd.DataFrame([files, extensions, ctime_list, mtime_list]).T
df.columns = ['Filename', 'File Extension', 'Time Created', 'Time Modified']

df.to_csv('FileTreeTracker.csv')