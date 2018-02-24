# Problem1: Receive miles and convert to kilometers
# kilometers = miles * 1.60934
# Enter Miles 5
# 5 miles equals 8.04 kilometers


miles = input('Please provide number of miles: ')
miles = float(miles)
kilometers = miles * 1.60934

print(' The provided number of miles: {} is equal to {} '
      'kilometers'.format(miles, kilometers))
