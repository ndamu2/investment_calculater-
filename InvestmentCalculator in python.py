P=float(input("Enter the amount you want to deposite"))
r=float(input("enter the interest "))
t=float(input("ente the years of the investment"))

print(P)
print(r)
print(t)

interest=input("Do you want (simple or compound) interest?")
if interest == "simple":
    A=P*(1+r*t)
    print("This is the amount of simple interest")
    print(A)

else:
    A=P*(1+r)**t
    print("This is the amount of compound interest")
    print(A)
