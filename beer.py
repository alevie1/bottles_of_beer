#Prompt for how many bottles of beer are, in fact, on the wall
bottle_number = int(input('How many bottles of beer are on the wall?\n'))
drunk = 0
#Cry if it is zero?
if bottle_number < 1:
	print("\n*incoherent sobbing at the sad lack of beer*\n")
#Make it sing every verse, make sure it doesn't say 'bottles' for one bottle
print('')
while bottle_number > 0:
	if bottle_number == 1:
		line1 = f'{bottle_number} bottle of beer on the wall'
		line2 = f'{bottle_number} bottle of beer'
		line3 = f'Take it down,\nPass it around,'
		bottle_number = bottle_number - 1
		line4 = f'{bottle_number} bottles of beer on the wall'
	else:
		line1 = f'{bottle_number} bottles of beer on the wall'
		line2 = f'{bottle_number} bottles of beer'
		line3 = f'Take one down,\nPass it around,'
		bottle_number = bottle_number - 1
		line4 = f'{bottle_number} bottles of beer on the wall'
	drunk += 1
	#if drunk > 5:
		#finish this part later
	print(f'{line1}\n{line2}\n{line3}\n{line4}')
#Add 'drunkenness' - substitute random characters into the string?