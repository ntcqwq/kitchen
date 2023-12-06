import math

def find_point(x1, y1, d1, x2, y2, d2, x3, y3, d3):
    # Solve for N_x and N_y using the formula
    N_x = x1 + math.sqrt(d1 - (y1 - y2)**2) if (d1 - (y1 - y2)**2) >= 0 else None
    N_y = y1 + math.sqrt(d1 - (x1 - x2)**2) if (d1 - (x1 - x2)**2) >= 0 else None
    
    # Check if the solution is valid for the second set of coordinates
    if (N_x is not None and N_y is not None and
            math.isclose((N_x - x2)**2 + (N_y - y2)**2, d2)):
        return f"{int(N_x)} {int(N_y)}"
    
    # Solve for N_x and N_y using the formula for the second set of coordinates
    N_x = x2 + math.sqrt(d2 - (y2 - y3)**2) if (d2 - (y2 - y3)**2) >= 0 else None
    N_y = y2 + math.sqrt(d2 - (x2 - x3)**2) if (d2 - (x2 - x3)**2) >= 0 else None
    
    # Check if the solution is valid for the third set of coordinates
    if (N_x is not None and N_y is not None and
            math.isclose((N_x - x3)**2 + (N_y - y3)**2, d3)):
        return f"{int(N_x)} {int(N_y)}"
    
    # If no valid solution is found, return None
    return None

x1, y1, d1 = map(int, input().split())
x2, y2, d2 = map(int, input().split())
x3, y3, d3 = map(int, input().split())


print(find_point(1, 1, 1, 2, 1, 2, 3, 5, 13))