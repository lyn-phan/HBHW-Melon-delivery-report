the_file = open("um-deliveries-20140519.txt")
'''day 1 sales'''
the_file = open("um-deliveries-20140520.txt")
'''day 2 sales'''
the_file = open("um-deliveries-20140521.txt")
'''day 3 sales'''

def calculate_sales_report():
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')
        melon = words[0]
        count = words[1]
        amount = words[2]
        sum()


        
print(f"Delivered {count} {melon}s for total of ${amount}.")







print("Day 1")
'''This is the sales for Day 1'''

the_file = open("um-deliveries-20140519.txt")
'''Data for sales / deliveries for one driver'''
for line in the_file:
    '''Starts a loop to go through each line in the summary'''

    line = line.rstrip()
    ''' removes white space or removes specified set of characters'''
    words = line.split('|')
    '''splits arguments into separate words'''

    melon = words[0]
    '''the first word is defined for melon type'''
    count = words[0]
    '''the first of this is the count'''
    amount = words[0]
    '''the first of this is the dollar amount'''

    print("Delivered {} {}s for total of ${}".format(count, melon, amount))

the_file.close()
'''this file is closed'''


print("Day 2")
the_file = open("um-deliveries-20140520.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
the_file.close()


print("Day 3")
the_file = open("um-deliveries-20140521.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
the_file.close()
