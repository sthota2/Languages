def liters_100km_to_miles_gallon(liters):
    return (1/(1.609344/3.785411784))*100/liters
#
# Write your code here.
#
def miles_gallon_to_liters_100km(miles):
    km_per_liters=(1/1.609344)/(1/3.785411784)*100/miles
    return km_per_liters
#
# Write your code here
#

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
