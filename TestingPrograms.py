###1.Function Call to take the list and return theri sums of even numbers only
def ListSum(myList):
	sum=0
	for i in range(0,len(myList)):
		if myList[i] % 2 == 0:
			sum += myList[i]
	return sum

myList=[1,2,3,4,5,6]
result=ListSum(myList)
print(f"The sum of the even numbers in the list is:{result}")

###2.Program that to take user input
name=input("Enter the name of the Candidate:")
while True:
	try:	
		age=int(input(f"Hello {name},Please enter you're age:"))
		break
	except ValueError:
		print(f"{name} Please Enter the integer value only")
if age >= 18:
	print(f"{name},eligible to Vote \n Thanks for expressing you're Right")
else:
	print(f"{name}, is not eligible to vote Please wait {18-age} years to become Eligible")

###3.Python program to remove
vowels='aeiou'
while True:
	try:
		variable=input("Enter the String:")
		break
	except ValueError:
		print("Please enter the String value only")
def removeVowels(s):
	return ''.join([c for c in s if c.lower() not in 'aeiou'])

result=removeVowels(variable)
print(f"The result after removing is:{result}")
