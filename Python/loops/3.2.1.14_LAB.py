blocks = int(input("Enter the number of blocks: "))
height = 0
int_layer = 1
while blocks > 0 :
    blocks = blocks - int_layer 
    int_layer = int_layer + 1

    if blocks < 0 :
        break
    height = height + 1
#
# Write your code here.
#	

print("The height of the pyramid:", height)
