def practice() :
	w = int(input( "50元:" ))
	x = int(input( "10元:" ))
	y = int(input( "5元:" ))
	z = int(input( "1元:" ))

	result = w * 50 + x * 10 + y * 5 + z * 1
	print(result)

def quiz() :
	total = int(input( "多少錢:" ))
	remaining = 1000 - total
	num_of_500_dollar = remaining // 500
	remaining = remaining % 500
	num_of_100_dollar = remaining // 100
	remaining = remaining % 100
	num_of_50_dollar = remaining // 50
	remaining = remaining % 50
	num_of_10_dollar = remaining // 10
	remaining = remaining % 10
	num_of_5_dollar = remaining // 5
	remaining = remaining % 5
	num_of_1_dollar = remaining // 1

	print(num_of_500_dollar, end=" ")
	print(num_of_100_dollar, end=" ")
	print(num_of_50_dollar, end=" ")
	print(num_of_10_dollar, end=" ")
	print(num_of_5_dollar, end=" ")
	print(num_of_1_dollar)

def more() :
	total = int(input( "多少錢:" ))
	remaining = 1000 - total

	denominations = [500, 100, 50, 10, 5, 1]
	num_of_notes = []

	for denomination in denominations:
		num_of_notes.append(remaining // denomination)
		remaining = remaining % denomination

	print(num_of_notes, end="")
	print()

command = -1
while command != 0 :
	print( "\n0: 結束" )
	print( "1: 總共多少錢" )
	print( "2: 該怎麼找錢" )
	print( "3: 該怎麼找錢 V2" )
	command = int( input( "輸入指令:" ) )
	if command == 1 :
		practice()
	elif command == 2 :
		quiz()
	elif command == 3 :
		more()
	elif command != 0 :
		print( "no command" )