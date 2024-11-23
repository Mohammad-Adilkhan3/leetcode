def rotateTheBox(box):
    m, n = len(box), len(box[0])
    
    # Apply gravity row by row
    for row in box:
        empty = n - 1  # Position of the last empty space
        for j in range(n - 1, -1, -1):
            if row[j] == '#':
                row[j], row[empty] = row[empty], row[j]
                empty -= 1
            elif row[j] == '*':
                empty = j - 1
    
    # Rotate the matrix 90 degrees clockwise
    rotated_box = [[None] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            rotated_box[j][m - i - 1] = box[i][j]
    
    return rotated_box
