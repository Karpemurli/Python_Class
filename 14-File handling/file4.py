
# Q. how to create a file with datetime as a filename?

from datetime import datetime


# currt_dt=datetime.now()
# # print("current_Date & Time=",currt_dt)


# #datetime file save & convert string in using strftime() function . 


# file_name =currt_dt.strftime('%d-%m-%Y-%H-%M-%S.txt')
# with open(file_name,"a") as fp:
#     print("created",file_name)


curr=datetime.now()

filenm=r'D:/python/14-File handling/'+curr.strftime('%d-%m-%Y-%H-%S-%M.txt')
with open(filenm,'a') as mm:
    print("created",filenm)