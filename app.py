# Prompt user for the value of n
n = int(input("Enter the value of n (an odd integer): "))

# Create an n x n matrix filled with zeros
magic_square = [[0 for i in range(n)] for j in range(n)]

# Set the starting position of the number 1
row = n // 2
col = n - 1

# Define a function to determine the next position in the magic square
def next_position(row, col, n):
    row = (row - 1) % n
    col = (col + 1) % n
    return row, col

# Iterate through the numbers 1 to n^2 and place them in the magic square
for num in range(1, n**2 + 1):
    # Place the current number in the current position
    magic_square[row][col] = num
    
    # Determine the next position in the magic square
    next_row, next_col = next_position(row, col, n)
    
    # If the next position is already filled, move down one row instead
    if magic_square[next_row][next_col]:
        row = (row + 1) % n
    else:
        row, col = next_row, next_col

# Print the completed magic square
print("Magic Square of size", n)
for i in range(n):
    for j in range(n):
        print(magic_square[i][j], end='\t')
    print()
