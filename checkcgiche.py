#!/bin/python3


# Import modules for CGI handling
import cgi, cgitb
cgitb.enable()

# Create instance of FieldStorage
form = cgi.FieldStorage()

start_date = form.getvalue('start_date')
stop_date  = form.getvalue('stop_date')
cecid = form.getvalue('cecid')



import smartsheet
smartsheet = smartsheet.Smartsheet('5weighwlzx7doyt3zdaykoqbbe')
sheetId=564760182843268
sheet = smartsheet.Sheets.get_sheet(564760182843268)
count=0
#import smartsheet
#smartsheet = smartsheet.Smartsheet('1pqifa4phr6rou9w3fey7cx4ru')
#sheet = smartsheet.Sheets.get_sheet(5802696138614660)
#count=0
#sheetId=5802696138614660

def dateP(start_date,stop_date):
        import datetime
        myDateList=[]
        start = datetime.datetime.strptime(start_date, "%d-%m-%Y")
        stop = datetime.datetime.strptime(stop_date, "%d-%m-%Y")
        import re
        from datetime import timedelta
        def change_date_format(dt):
            return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1',dt)
        while start <= stop:
                q=str(start)
                o=q.split()[0]
                p=change_date_format(o)
                #print (p)
                myDateList.append(str(p))
                start = start + timedelta(days=1)
        return  myDateList


def countP(sheetId,rowInd):
        count = 0
        for row in sheet.rows:
                if ( rowInd == row.row_number ):
                        for c in range(1, len(sheet.columns)):
                                if ( (row.cells[c].value) == 'P' ):
                                        count +=1;
        return count

def rowIdf(date_ls,sheetId):
        rowIds=0
        r=len(sheet.rows)
        #r=r-1
        for i in range(0,r):
                if ( date_ls ==  sheet.rows[i].cells[0].value):
                        rowIds = (sheet.rows[i].id)
                        rowInd = i
        return rowIds,rowInd


def colIdf(cecid,sheetId):
        c=len(sheet.columns)
        #c=c-1
        colIds=0
        for j in range(0,c):
                if ( cecid  == sheet.columns[j].title):
                        colIds = (sheet.columns[j].id)
        return colIds

def updatess(rowIds,colIds):
        row_a = smartsheet.Sheets.get_row(sheetId, rowIds)
        cell_a = row_a.get_column(colIds)
        cell_a.value = 'P'
        row_a.set_column(cell_a.column_id, cell_a)
        smartsheet.Sheets.update_rows(sheetId, [row_a])
        print ("submitted")

#query = '10-03-2017'
#cecid = 'ambika'
#myDateList=[]


def checkfn(start_date,stop_date):
        mydl=dateP(start_date,stop_date)
        counttracker=[]
        for date_ls in mydl:
                op = rowIdf(date_ls,sheetId)
                rowInd = op[1]
                datenow=countP(sheetId,(rowInd+1))
                counttracker.append(int(datenow))
                #print (counttracker)
                if ( (countP(sheetId,(rowInd+1)))) > 1:
                        print ("<h2>%s   leaveQuotaExceeds </h2>" %(date_ls));
                        # quit();
                else:
                       ## print (date_ls + '    ' + str(datenow)+'       booked')
                        print ("<h2>%s  -- %s   booked </h2>" %(date_ls,str(datenow)));
        return counttracker

#couuntt = countP(query,sheetId,(rowInd+1))
#print (couuntt)
#updatess(rowIds,colIds)
def submitfn(start_date,stop_date,cecid):
        mydl=dateP(start_date,stop_date)
        for date_ls in mydl:
                op = rowIdf(date_ls,sheetId)
                rowIds = op[0]
                rowInd = op[1]
                colIds = colIdf(cecid,sheetId)
                updatess(rowIds,colIds)


#start_date = input("Enter your input: (format and minimum value is  28-02-2017)  ");
start_date = form.getvalue('start_date')
stop_date  = form.getvalue('stop_date')
cecid = form.getvalue('cecid')
#stop_date = input("Enter your input: format and minimum value is  28-02-2017:  ");
#stop_date = input("Enter your input: format and max value is 10-03-2017:  ");
counttr=checkfn(start_date,stop_date)


#print (all(i >= 2 for i in counttr))
##if all(i <= 1 for i in counttr ):
  ##      updateenable = True
        ##print ('dates are available to book')
    ##    updatestatus = input("Do you want to update the PTO tracker (format:yes/no):  ")
##else:
  ##      updateenable = False
   ##     updatestatus = 'no'
    ##    print ("Quota exceeded, please select different date range")
     ##   exit()
#print (updatestatus)
#print (updateenable)
##if (updatestatus == 'yes' and updateenable == True):
#       print (counttr)
#       print (len(counttr)-1)
  ##      for i in range(0,(len(counttr))):
    ##            cecid = input("enter your cecid:  ")
     ##           submitfn(start_date,stop_date,cecid)
      ##          print ("process  completed. exiting....")
       ##         exit()
 
print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
tryitg = mul(start_date,stop_date)
tryi = tryitg[0]
tryit = tryitg[1]
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2>Hello %s %s %s %s</h2>" % (start_date, stop_date, tryit, tryi))
print ("</body>")
print ("</html>")
