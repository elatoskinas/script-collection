# Input names of the files
file1 = input()
file2 = input()

# Open the first file, and split lines
f1 = open(file1, "r")
f1_contents = f1.read().split("\n")

# Open the second file, and split lines
f2 = open(file2, "r")
f2_contents = f2.read().split("\n")

# Iterate through contents of the files
for i in range(len(f1_contents)):
    # If index bigger than file2 size, then stop comparison
    if i > len(f2_contents):
        break
    
    # Get the i-th line from both file lines
    l1 = f1_contents[i]
    l2 = f2_contents[i]

    # Compare the lines
    equal = l1 == l2

    # Lines not equal: Print differences
    if not equal:
        print("Line", i)
        print(l1)
        print("\n\n\n")
        print(l2)
        print("--------------------")