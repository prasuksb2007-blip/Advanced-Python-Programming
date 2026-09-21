"""
Create a Python script to read data from an input file. Perform count lines, extract the first two lines, and
write the extracted data into a new file.
"""
def process_file(input_filename, output_filename):
    try:
        # Step 1: Open and read the input file
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()
        
        # Step 2: Count the total number of lines
        total_lines = len(lines)
        print(f"Total lines in '{input_filename}': {total_lines}")
        
        # Step 3: Extract the first two lines
        first_two_lines = lines[:2]
        
        # Step 4: Write the extracted lines to the output file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(first_two_lines)
            
        print(f"Successfully extracted first 2 lines to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Define file names
    input_file = "input.txt"
    output_file = "output.txt"
    
    # Optional: Create a dummy input file for demonstration/testing
    with open(input_file, "w") as f:
        f.write("Line 1: Welcome to File Handling Experiment.\n")
        f.write("Line 2: This is the second line.\n")
        f.write("Line 3: This line will not be copied to output.\n")
        f.write("Line 4: This is the fourth line.\n")

    # Run the function
    process_file(input_file, output_file)

"""
--> Output
Total lines in 'input.txt': 4
Successfully extracted first 2 lines to 'output.txt'.
"""