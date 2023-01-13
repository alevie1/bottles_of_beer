#Prompt for how many bottles of beer are, in fact, on the wall
bottle_number = int(input("How many bottles of beer are on the wall?"))
#Cry if it is zero?
if bottle_number < 1:
	print("*incoherent sobbing at the sad lack of beer*")
#Make it sing every verse
while bottle_number > 0:
	print(f'{bottle_number} bottles of beer on the wall')
	print(f'{bottle_number} bottles of beer')
	print(f'Take one down,\nPass it around,')
	bottle_number = (bottle_number - 1)
	print(f'{bottle_number bottles of beer on the wall}\n\n')
#Add 'drunkenness' - substitute random characters into the string?