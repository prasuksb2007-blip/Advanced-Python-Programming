"""
Create a Python script to read data from an input file. Perform count lines, extract the first two lines, and
write the extracted data into a new file.
"""
# Create input.txt before running the program

file1 = open("input.txt", "r")
lines = file1.readlines()

print("Total number of lines:", len(lines))

print("First two lines:")
print(lines[0], end="")
print(lines[1], end="")

file1.close()

file2 = open("output.txt", "w")
file2.writelines(lines[:2])
file2.close()

print("\nFirst two lines are written to output.txt")
"""
--> Output (In output.txt):
Total number of lines: 4
First two lines:
This is the first line.
This is the second line.

First two lines are written to output.txt
"""