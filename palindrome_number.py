num = int(input("Enter the number:"))
original = num
reverse = 0
while num != 0:
 reverse = reverse * 10 + num % 10
 num //= 10
if original == reverse:
 print(f"{original}is the paindrome")
else:
 print(f"{original}is not a palindrome")
