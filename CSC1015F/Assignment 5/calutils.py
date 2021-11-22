# functions and strings
# vince ian muzerengwa

def is_leap_year (year):
    if year%4 == 0:
        r = True
        if year==1900:
            r=False
        
    else:
        r = False
        
    return r

def month_name (number):
    
    if number ==1:
        y="January"
    if number == 2:
        y="February"
    if number ==3:
        y="March"
    if number==4:
        y="April"
    if number ==5:
        y='May'
    if number==6:
        y="June"
    if number ==7:
        y="July"
    if number ==8:
        y="August"
    if number ==9:
        y="September"
    if number ==10:
        y="October"
    if number ==11:
        y="November"
    if number ==12:
        y="December"
        
    return y 
def days_in_month (month_number,year):
    
    
    if month_number ==1:
        days=31
    if month_number == 2:
        days=28
    if month_number==2 and year%4==0:
        days=29
    if month_number ==3:
        days=31
    if month_number==4:
        days=30
    if month_number ==5:
        days=31
    if month_number ==6:
        days=30
    if month_number ==7:
        days=31
    if month_number ==8:
        days=31
    if month_number ==9:
        days=30
    if month_number ==10:
        days=31
    if month_number ==11:
        days=30
    if month_number ==12:
        days=31    
       
    return days
        

def first_day_of_year (year):
    
    a = 5*((year-1)%4)
    b = 4*((year-1)%100)
    c = 6*((year-1)%400)
    day = ((1+a+b+c)%7)
    if day ==0:
        first=0
    if day==1:
        first=1
    if day==2:
        first=2
    if day==3:
        first=3
    if day==4:
        first=4
    if day==5:
        first=5
    if day==6:
        first=6
        
    return first


    
    
def first_day_of_month (month_number,year):
    
         
    import datetime
    
    first=datetime.datetime(year,month_number,1)
    day = first.strftime("%A")
    
    if day=='Sunday':
        x=0
     
    if day=='Monday':
        x=1
    if day=='Tuesday':
        x=2
    if day=='Wednesday':
        x=3    
    if day=='Thursday':
        x=4
    if day=='Friday':
        x=5        
    if day=='Saturday':
        x=6
          
    
    return x

      
        