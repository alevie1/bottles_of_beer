#Prompt for how many bottles of beer are, in fact, on the wall
bottle_number = int(input('How many bottles of beer are on the wall?\n'))
drunk = 0
#Cry if it is zero?
if bottle_number < 1:
	print("\n*incoherent sobbing at the tragic lack of beer*\n")
#Make it sing every verse, make sure it doesn't say 'bottles' for one bottle
print('')
while bottle_number > 0:
	if bottle_number == 1:
		part1 = f'{bottle_number} bottle of beer on the wall,\n{bottle_number} bottle of beer.\nTake it down,\nPass it around,\n'
		bottle_number = bottle_number - 1
		part2 = f'{bottle_number} bottles of beer on the wall'
	else:
		part1 = f'{bottle_number} bottles of beer on the wall,\n{bottle_number} bottles of beer,\nTake one down,\nPass it around,\n'
		bottle_number = bottle_number - 1
		if bottle_number == 1:
			part2 = f'{bottle_number} bottle of beer on the wall'
		else:
			part2 = f'{bottle_number} bottles of beer on the wall'
	drunk += 1
	#if drunk > 5:
		#finish this part later
	print(f'{part1}{part2}')
#Add 'drunkenness' - substitute random characters into the string?