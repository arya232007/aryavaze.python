print("1 Circle")
print("2 Rectangle")
print("3 Triangle")

c=int(input("choose:"))

if c==1:
    r=float(input("Radius"))
    print("area=",3.14*r*r)

elif c==2:
    l,b=float(input("length,breadth"))
    print("area=",l*b)

elif c==3:
    b,h=float(input("base,height"))
    print("area=",0.5*b*h)
