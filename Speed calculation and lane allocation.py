# Speed calculation and lane allocation
max_speed = 120

print('===== Speed Calculation and Lane Allocation System =====')
try:
  distance = eval(input('Enter your travel distance (km): '))
  duration = eval(input('Enter expected  travel duration (hours): '))

  if distance <= 0 or duration <= 0:
    print('Error: distance and duration must be greater than 0.')
  else:
    speed = distance / duration
    print(f'\nRequired Speed: {speed:.2f}km/h')
    if speed > max_speed:
      print('Safety Status: Unsafe')
      print('Warning!! Required speed exceed the maximum limit(120km/h).')
      print('Please adjust the travel duration.')
    else:
      print('Safety Status: Safe')
      if speed > 60:
        lane = 'Fast Lane'
      else:
        lane = 'Slow Lane'

      print(f'Assigned Flight Lane: {lane}')
      print('Flight Status: Ready for flight')
      print('Have a safe journey!')
      
except ValueError:
  print('Error! Please enter numeric values.')