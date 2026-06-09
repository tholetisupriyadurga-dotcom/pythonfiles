num = input("Enter a number: ")
print(num[::-1])
if num == num[::-1]:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")