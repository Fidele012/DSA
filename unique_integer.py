import os

# Constants defining the integer limits
LOWER_BOUND = -1023
UPPER_BOUND = 1023
TOTAL_RANGE = UPPER_BOUND - LOWER_BOUND + 1

# Function to process the input file and write unique, sorted integers to the output file
def process_file(input_file, output_file):
    # Array to track whether an integer has been encountered
    seen_values = [False] * TOTAL_RANGE

    try:
        with open(input_file, 'r') as reader:
            for entry in reader:
                num = extract_number(entry.strip())
                if num is not None:
                    seen_values[num - LOWER_BOUND] = True

        with open(output_file, 'w') as writer:
            # Write unique integers in sorted order
            for index in range(TOTAL_RANGE):
                if seen_values[index]:
                    writer.write(f"{index + LOWER_BOUND}\n")

    except (FileNotFoundError, IOError) as err:
        print(f"Error during file operations: {err}")

# Function to parse a line and extract a valid integer within range
def extract_number(entry):
    parts = entry.split()

    # Return None if more than one part or invalid integer
    if len(parts) != 1:
        return None

    try:
        num = int(parts[0])
        if LOWER_BOUND <= num <= UPPER_BOUND:
            return num
    except ValueError:
        pass

    return None

if __name__ == "__main__":
    input_path = 'DSA/input.txt'
    output_path = 'DSA/result.txt'

    if os.path.exists(input_path):
        process_file(input_path, output_path)
        print(f"Processing complete. Output saved to {output_path}")
    else:
        print(f"Input file {input_path} does not exist")
