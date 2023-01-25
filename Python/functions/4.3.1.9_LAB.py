def is_prime(num):
     count=0
     prime_count=0
     for n1 in range (2,num+1):
         if ( num % n1 == 0):
             count=count+1
         else:
             primt_count=prime_count+1
     
     if ( prime_count == 0) & (count == 1):
      return True
     else:
      return False
             
#
# Write your code here.
#

for i in range(1, 100):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
