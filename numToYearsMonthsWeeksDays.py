import sys
while True:
    
    print("press q to quit")
    print("Please enter days you intend to convert to years, months, weeks and days:: ")

    number = input()
    
    if number == 'q':    
        sys.exit()
    else:
      

        year,y_remainder = divmod(int(number), 365)
    
        month,m_remainder = divmod(y_remainder, 30)
    
        week,day = divmod(m_remainder, 7)
        print("equals",year,"year",month,"months",week,"weeks",day,"days")

   
  



