current_battery = float(input('Please enter current battery level in percentage, %:'))
travel_distance = float(input('Please enter your travel distance (km):'))
battery_required = travel_distance * 0.1
charge_or_not =''
  
if current_battery > battery_required:
  print('Battery level is sufficient.')
  left = current_battery - battery_required
  print('The remaining battery level after the journey is',left)

while current_battery < battery_required:
  print('Battery level is insufficient.')
  print('Please charge your vehicle.')
  charge_or_not = input('Have you charged your vehicle? (yes or no):').lower()
  while charge_or_not == 'no':
    print('Please charge your vehicle.')
    charge_or_not = input('Have you charged your vehicle? (yes or no):').lower()
  if charge_or_not == 'yes':
    current_battery = float(input('Please enter current battery level in percentage, %:'))
    if current_battery > battery_required:
      print('Battery level is sufficient.')
      left = current_battery - battery_required
      print('The remaining battery level after the journey is',left)
