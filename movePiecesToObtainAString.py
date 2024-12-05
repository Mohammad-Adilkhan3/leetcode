def canTransform(start: str, target: str) -> bool:
    n = len(start)
    
    # Remove blanks and compare character sequences
    start_pieces = [(c, i) for i, c in enumerate(start) if c != '_']
    target_pieces = [(c, i) for i, c in enumerate(target) if c != '_']
    
    if len(start_pieces) != len(target_pieces):
        return False  # Mismatch in number of pieces
    
    for (sc, si), (tc, ti) in zip(start_pieces, target_pieces):
        if sc != tc:  # Pieces don't match
            return False
        if sc == 'L' and si < ti:  # 'L' moved right
            return False
        if sc == 'R' and si > ti:  # 'R' moved left
            return False
    
    return True

# Example Test Cases
print(canTransform("_L__R__R_", "L______RR"))  # Output: True
print(canTransform("R_L_", "__LR"))           # Output: False
print(canTransform("_R", "R_"))               # Output: False
