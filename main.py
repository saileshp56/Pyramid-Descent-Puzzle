output_file = "pyramid_output.txt"
input_file = "pyramid_input.txt"

target = 0
arr = []
with open(input_file, 'r') as file:
    lines = file.read().splitlines()
    target = int(lines[0].split(" ")[1])
    for line in lines[1:]:
        arr.append([int(item) for item in line.split(",")])

# All set up is now done

rows = len(arr)

def dfs(row, col, str, prod):

    val = arr[row][col]
    new_prod = prod * val
    if new_prod > target:
        return "*"
    if row == rows - 1: # DFS is at the final row
        if new_prod == target:
            return str
        else:
            return "*"
    left = dfs(row+1, col, str + "L", val * prod)
    if left == "*":
        return dfs(row + 1, col+1, str + "R" ,val * prod) # right = dfs(row + 1, col+1, str + "R" ,val * prod)
    else:
        return left

# dfs(0, 0, "", 1) is called to start the DFS

with open(output_file, 'w') as file:
    file.write(dfs(0, 0, "", 1))
