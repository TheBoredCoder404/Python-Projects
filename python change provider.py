from decimal import Decimal 
values = [Decimal("100"), Decimal("50"), Decimal("20"), Decimal("10"),
          Decimal("5"), Decimal("1"), Decimal("0.25"), Decimal("0.10"),
          Decimal("0.05"), Decimal("0.01")]
names = ["100 Dollar Bill(s)","50 Dollar Bill(s)","20 Dollar Bill(s)","10 Dollar Bill(s)","5 Dollar Bill(s)","1 Dollar Bill(s)","Quarter(s)","Dime(s)","Nickel(s)","Penny(s)"]
amount = Decimal(input("Amount:"))
for i in range(len(values)):
    if(amount>=values[i]):
        print(str(int((amount-amount%values[i])/values[i]))+" "+names[i])
        amount = amount%values[i]
        
    


    
  

