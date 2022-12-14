import os
import pathlib
from datetime import date
a = date.today()

c = ""
if(len(str(a.month))<2):
    c = '0'+str(a.month)
else:
    c=str(a.month)
b = str(a.day)+"-"+c+"-"+str(a.year)
print(b)
try:
    desktop = os.path.expanduser("~/Desktop")
    mode = 0o666
    path = os.path.join(desktop,b)
    os.mkdir(path, mode)
    print("File has been created")
except:
    print("The file is already exits")