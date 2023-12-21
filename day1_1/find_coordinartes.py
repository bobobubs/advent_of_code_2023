# Replace 'yourfile.txt' with the path to the actual file you want to read
file_path = 'coordinates.txt'
def calc_coordinates():
    # Open the file in read mode ('r')
    with open(file_path, 'r') as file:
        # Read and print each line
        coordinate_total = 0 
        nums = ['1', '2', '3', '4','5', '6', '7', '8', '9', '0']
        for line in file:
            #Find the first digit on the left side
            left_index = 0
            while(line[left_index] not in nums):
                left_index+=1

            right_index = -2   
            while(line[right_index] not in nums):
                right_index -= 1
                
            coordinate = int(line[left_index] + line[right_index])
            print(coordinate)
            coordinate_total += coordinate
       
    return coordinate_total

print(calc_coordinates()) 