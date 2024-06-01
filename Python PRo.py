# Shipping Modes
F_Mode="1--By Air"
R_Mode="2--By Car"
S_Mode="3--By Ship"
F_Price=30
R_Price=20
S_Price=10
print("Shipping Prices: " , F_Mode ," ", F_Price ," ", R_Mode,R_Price , S_Mode,' ',S_Price )
Wieght=float(input("Enter Cargo wieght: "))
Shipping_Mode=int(input("Enter shipping Mode: "))

if Shipping_Mode==1 or Shipping_Mode==2  or Shipping_Mode==3:
    if Shipping_Mode==1:
       Coast=F_Price*Wieght
       print("Your shipping coast is= " + str(Coast))
    elif Shipping_Mode==2:
         Coast=R_Price*Wieght
         print("Your shipping coast is= " + str(Coast))
    elif Shipping_Mode==3:
         Coast=S_Price*Wieght
         print("Your shipping coast is= " + str(Coast))
else:print(" please Correct your input value")
