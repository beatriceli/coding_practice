import string

def rows(letter):
    alphabet = string.ascii_uppercase
    idx = alphabet.index(letter)
    n = 2*idx+1
    letters = list(alphabet[:idx+1])

    grid = [[" "] * n for _ in range(n)]
    left, right = idx, idx

    for i in range(idx+1):
        char = letters[i]
        left = idx - i
        right = idx + i
        grid[i][left] = char
        grid[i][right] = char

    for i in range(idx+1,n):
        grid[i] = grid[n-i-1]
    
    return ["".join(row) for row in grid]

if __name__ == '__main__':
    print(rows('C'))