begin_number_tickets = 8

number_tickets = raw_input("How many tickets do you want?")
print "You have requested for " + number_tickets;

number_tickets_left = begin_number_tickets - int(number_tickets)

if int(number_tickets) >= begin_number_tickets:
    print "There are not enough tickets for you"
else:
    print "There are " + str(number_tickets_left) + " tickets left"