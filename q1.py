
# ******************************
# Make your Code
# ******************************
cluster_count = 0
even_count = 0

for i in range(10):
    num = int(input())

    # checks if the number is even
    if num % 2 == 0:
        even_count += 1
    else:
        even_count = 0
    
    # adding the cluster
    if even_count == 2:
        cluster_count += 1

print(cluster_count)

# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
