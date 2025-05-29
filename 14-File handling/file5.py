

from datetime import datetime


currt_dt=datetime.now()

#separat folder madhe file create karayachi aslyas.
file_name =r"D:/python/14-File handling/" +currt_dt.strftime('%d-%m-%Y-%H-%M-%S.txt')

with open(file_name,"a") as fp:
    print("created",file_name)
