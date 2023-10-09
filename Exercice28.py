# asking for the number of years
n = int(input("Enter the number of years (n): "))

s = 0

for i in range(1, n + 1):
    depotAnnuel = 500 + (3 * i)
    s = s + depotAnnuel

print("The amount Amal will have on her",n,"th birthday is:",s,"dh")
