# first of month
# vince ian muzerengwa

month=input("Enter the month: ")
year=eval(input("Enter the year: "))


if month =="January":
 y=1
if month == "February":
 y=2
if month =="March":
  y=3
if month=="April":
  y=4
if month =="May":
  y=5
if month =="June":
  y=6
if month =="July":
  y=7
if month =="August":
  y=8
if month =="September":
  y=9
if month =="October":
  y=10
if month =="November":
  y=11
if month =="December":
  y=12
  
import datetime
first=datetime.datetime(year,y,1)

print("The 1st of",month,year,"is a",first.strftime("%A."))