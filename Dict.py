"""x = input("Enter Word: ")
y = input("Enter Letter: ")
z = 0
for i in range(len(x)):
    if y == x[i]:
        z = z + 1
print(z)

num_to_word = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven",
               "8": "eight", "9": "nine"}
a = str(int(input("Enter Number: ")))
num_list = list(a)
num_word = ""
for i in num_list:
    num_word = num_word + num_to_word[i] + " "
print(num_word)

colors = {"green", "yellow", "red", "white", "blue"}
c = int(input("How many colors would you like to add?: "))
for i in range(c):
    q=input("What color would you like to add?: ")
    colors.add(q)

for n in colors:
    print(n)"""