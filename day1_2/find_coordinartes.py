def calc_coordinates():
    file_path = './day1_2/coordinates.txt'
    coordinate_total = 0

    # Mapping of spelled-out numbers to their numerical equivalents
    numbers_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }

    # Open the file in read mode ('r')
    with open(file_path, 'r') as file:
        for line in file:
            # Initialize variables to hold the positions of the first and last digits
            first_digit_pos = len(line)
            last_digit_pos = -1
            first_digit = None
            last_digit = None

            # Check each spelled-out number and numerical digit in the line
            for word, number in numbers_map.items():
                pos = line.find(word)
                while pos != -1:  # While the spelled-out number is found in the line
                    if pos < first_digit_pos:
                        first_digit_pos = pos
                        first_digit = number
                    if pos > last_digit_pos:
                        last_digit_pos = pos
                        last_digit = number
                    # Search for next occurrence
                    pos = line.find(word, pos + 1)

            # Check for numerical digits
            for num in range(10):
                pos = line.find(str(num))
                while pos != -1:  # While the digit is found in the line
                    if pos < first_digit_pos:
                        first_digit_pos = pos
                        first_digit = num
                    if pos > last_digit_pos:
                        last_digit_pos = pos
                        last_digit = num
                    # Search for next occurrence
                    pos = line.find(str(num), pos + 1)

            # Calculate the coordinate if both digits are found
            if first_digit is not None and last_digit is not None:
                coordinate = int(f"{first_digit}{last_digit}")
                coordinate_total += coordinate

    return coordinate_total

# Print the total calibration value
print(calc_coordinates())