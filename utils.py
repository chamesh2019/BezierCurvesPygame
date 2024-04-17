def in_circle(point: tuple, center: tuple, radius: int) -> bool:
    return (abs(point[0] - center[0])**2 + abs(point[1] - center[1])**2)**0.5 < radius


def divide_line_segment(A, B, n):
    x1, y1 = A
    x2, y2 = B
    
    dx = x2 - x1
    dy = y2 - y1
    
    dx_step = dx / n
    dy_step = dy / n
    
    points = [(x1 + i * dx_step, y1 + i * dy_step) for i in range(0, n)]
    points.append(B)
    
    return points

