#Prompt for how many bottles of beer are, in fact, on the wall
import random
import string

bottle_number = ''

while not bottle_number:
	try:
		bottle_number = int(input('How many bottles of beer are on the wall?\n'))
	except:
		print("That's not a number!")
drunk = 0
drunknum = ''
#Cry if it is zero?
if bottle_number == 0:
	print("\nNo beer? A tragedy, to be sure. *sniff*\n")
elif bottle_number < 0:
	print("What? Negative beer? How is that possible?")
#Make it sing every verse, make sure it doesn't say 'bottles' for one bottle


print('')
while bottle_number > 0:
	if bottle_number == 1:
		part1 = f'{bottle_number} bottle of beer on the wall,\n{bottle_number} bottle of beer.\nTake it down,\nPass it around,\n'
		bottle_number = bottle_number - 1
		part2 = f'{bottle_number} bottles of beer on the wall\n'
	else:
		part1 = f'{bottle_number} bottles of beer on the wall,\n{bottle_number} bottles of beer,\nTake one down,\nPass it around,\n'
		bottle_number = bottle_number - 1
		if bottle_number == 1:
			part2 = f'{bottle_number} bottle of beer on the wall\n'
		else:
			part2 = f'{bottle_number} bottles of beer on the wall\n'
	drunk += 1

	fullsong = part1 + part2
	songlist = list(fullsong)

	if (drunk % 7) == 0:
		if drunk >= 15:
			drunknum += 'e'
		if drunk >= 30:
			drunknum += 'e'
		if drunk >= 60:
			drunknum += 'e'
		if drunk >= 90:
			drunknum += 'e'
		drunknum += 'e'
	for i in drunknum:
		charnum1 = random.randrange(len(songlist))
		charrep = random.choice(list(string.ascii_letters))
		#print(f'{charnum1}{charrep}')
		while songlist[charnum1] in '\n':
			charnum1 = random.randrange(len(songlist))
		songlist[charnum1] = charrep
	
	fullsong = ''.join(songlist)

	print(f'{fullsong}')
	input()
if drunk >= 150:
	print('\n...zzzzzzzzz...')
#Add 'drunkenness' - substitute random characters into the string?