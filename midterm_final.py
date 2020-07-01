midterm1=float(input("first midterm note:"))
midterm2=float(input("second midterm note:"))
final=float(input("final note:"))
average=0.3*midterm1+0.3*midterm2+final*0.4

if (average>=90):
    print("AA")
elif (average >= 85):
    print("BA")
elif (average >= 80):
    print("BB")
elif (average >= 75):
    print("CB")
elif (average >= 70):
    print("CC")
elif (average >= 65):
    print("DC")
elif (average >= 60):
    print("DD")
elif (average >= 50):
    print("FD")
else:
    print("FF")
