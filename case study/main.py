from service import task
from dao import taskdao
from table import table

while(1):
    x=task dao.takeinput()
    if(x):
        task dao.run(x)
    else:
        break
print("Exiting.....\n all changes are commmitted successfully..")