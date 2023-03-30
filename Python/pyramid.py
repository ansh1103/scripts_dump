# n = 5

# for i in range(n + 1):
#     # print(" "*(n-i) + ("*"*(2*i-1)).center(n) + " "*(n-i))
#     # print(("*"*(2*i-1)).center(n))
#     print(" "*(n//2) + ("*"*(i+1)).center(n) + " "*(n//2))

n = int(input("Enter no of rows:"))
for i in range(n):
    print((" "*(n-i-1))+("* "*(i+1)))

print("Inverted pyramid")
for i in range(n):
    print((' '*(i)+"* "*(n-i)))

print("Diamond pattern")
for i in range(n):
    print((" "*(n-i-1))+("* "*(i+1)))
for i in range(n-1):
    print((" "*(i+1)+"* "*(n-i-1)))
