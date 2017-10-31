dtb = datetime.datetime.strptime('10/30/2017 11:15 PM', '%m/%d/%Y %I:%M %p')
format = "%m/%d/%Y %H:%M:%S"
fordate = dtb.strftime(format)
date = datetime.datetime.strptime(fordate, format)


rdate = '10/30/2017 11:15 PM'
format = "%m/%d/%Y %H:%M:%S"
datetime.datetime.strptime(rdate, '%m/%d/%Y %I:%M %p').strftime(format)
