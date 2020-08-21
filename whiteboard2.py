terms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if terms <= 0:
   print("Please enter a positive whole number")
elif terms == 1:
   print("Fib sequence up to",terms,":")
   print(n1)
#run the sequence
else:
   print("Fib sequence:")
   while count < terms:
       print(n1)
       nth = n1 + n2
      #update numbers
       n1 = n2
       n2 = nth
       count += 1