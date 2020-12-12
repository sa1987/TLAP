#!/bin/python3

import smartsheet
smartsheet = smartsheet.Smartsheet('1pqifa4phr6rou9w3fey7cx4ru')
sheet = smartsheet.Sheets.get_sheet(5802696138614660)
count=0
sheetId=5802696138614660
def dateP(start_date,stop_date):
        import datetime
        myDateList=[]
#start_date = "28-02-2017"
#stop_date = "05-03-2017"
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

	


#query = '05-03-2017'
def countP(query,sheetId):
        result = smartsheet.Search.search_sheet(sheetId, query)
        s=str(result)
        start = s.find('Row ') + 4
        end = s.find(': "' )
        rowId = s[start:end]
        rowId=int(rowId)
        count=0
        for row in sheet.rows:
                if ( rowId == row.row_number ):
                        for c in range(0, len(sheet.columns)):
                                if ( (row.cells[c].value) == 'P' ):
                                        count +=1;
        return count
#countt=countP('05-03-2017',sheetId)
#print (countt)


myDateList=[]

#start_date = "28-02-2017"
#stop_date = "07-03-2017"
start_date = raw_input("Enter your input: format and minimum value is  28-02-2017:  ");
stop_date = raw_input("Enter your input: format and max value is 10-03-2017:  ");


mydl=dateP(start_date,stop_date)
#print (mydl)
#for query in mydl:
#       if ( countP(query,sheetId) >= 2 ):
#                       return 'excess'
for query in mydl:
         datenow=countP(query,sheetId)
         if ( (countP(query,sheetId)))> 1:
                 print (query +'    leaveQuotaExceeds');
                # quit();
         else:
                print (query + '  has ' + str(datenow)+'       booked')

