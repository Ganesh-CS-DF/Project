import re

def simp(funct,power):
    return (str(power)+ "*" + "(" + str(funct) + ")" + "^" + str(power-1))

def exp(funct,power):
    if re.search(r'^[0-9]',power):
        z=""
        for sep in range(9):
            z=z+str(sep)
        return simp(power,"1") + "*" + "e" + "^" + power
    else:
        return (funct + "^" + power)

def main(f,p):
    if "x" in f or "x" in p:
        if f=="x":
            p=int(p)
            return simp(f,p)
        if "e" in f:
            return exp(f,p)

    else:
            return 0

print("NOTE: ALL OPERTAIONS HERE ARE WITH RESPECT TO x")
f=input("Enter function:")
p=input("Enter power:")
print(main(f,p))
    
