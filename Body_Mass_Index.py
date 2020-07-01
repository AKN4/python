print ("""
******************************
Body   Mass   Index
******************************
""")


height = float(input("height (m):"))
weight= int(input("weight :"))
BMA=weight/(height**2) #Body_Mass_Index
if (BMA <18.5):
    print ("underweight")
elif (BMA >=18.5) and BMA<25:
    print ("normal")
elif (BMA >=25) and BMA<30:
    print ("overweight")
else:
    print ("obese")