#Prompt for how many bottles of beer are, in fact, on the wall
bottle_number = int(input('How many bottles of beer are on the wall?\n'))
#Cry if it is zero?
if bottle_number < 1:
	print("\n*incoherent sobbing at the sad lack of beer*\n")
#Make it sing every verse, make sure it doesn't say 'bottles' for one bottle
print('')
while bottle_number > 0:
	if bottle_number == 1:
		print(f'{bottle_number} bottle of beer on the wall')
		print(f'{bottle_number} bottle of beer')
		print(f'Take it down,\nPass it around,')
		bottle_number = (bottle_number - 1)
		print(f'{bottle_number} bottles of beer on the wall\n')
	else:
		print(f'{bottle_number} bottles of beer on the wall')
		print(f'{bottle_number} bottles of beer')
		print(f'Take one down,\nPass it around,')
		bottle_number = (bottle_number - 1)
		print(f'{bottle_number} bottles of beer on the wall\n')
#Add 'drunkenness' - substitute random characters into the string?