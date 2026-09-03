Name=input("Enter Name:")
s1=float(input("Enter DSA:"))
s2=float(input("Enter AI:"))
s3=float(input("Enter FDSA:"))
s4=float(input("Enter Maths:"))
s5=float(input("Enter DBMS:"))
s6=float(input("Enter OOPS:"))
total=s1+s2+s3+s4+s5+s6
avg=total/6
grade=avg
print("Grade:",grade)
if 90 < grade <=100:
    print('Grade A')
elif 80 <grade <=90:
    print("Grade B")
elif 70< grade <=80:
    print("Grade C")
elif 60<grade<=70:
    print("Grade D")
elif 50<grade<=60:
    print("pass")
else:
    print("Fail")
    
