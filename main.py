import pygame
import time 

from utils import in_circle, divide_line_segment

pygame.init()

# set full screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


point1X = 200
point1Y = 400

point2X = 600
point2Y = 400

controlX = 400
controlY = 400

mousedown = False
selected = None
resolution = 1
tick = pygame.time.Clock()

def draw_curve(point1: tuple, point2: tuple, center: tuple, resolution: int, screen: pygame.Surface):
    set_1 = divide_line_segment(point1, center, resolution)
    set_2 = divide_line_segment(center, point2, resolution)
    
    curve_points = []
    
    for index, (p1, p2) in enumerate(zip(set_1, set_2)):
        s = divide_line_segment(p1, p2, resolution)
        curve_points.append(s[index])
        
    for x in range(len(curve_points) - 1):
        pygame.draw.line(screen, (255, 255, 255), curve_points[x], curve_points[x + 1])
        


while True:
    tick.tick(60)
    cur_time = time.time()
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (point1X, point1Y), 5)
    pygame.draw.circle(screen, (0, 255, 0), (point2X, point2Y), 5)
    pygame.draw.circle(screen, (0, 0, 255), (controlX, controlY), 5)
    
    mouse_cordinates = pygame.mouse.get_pos()
    
    draw_curve((point1X, point1Y), (point2X, point2Y), (controlX, controlY), resolution, screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        # move point with mouse drag
        if event.type == pygame.MOUSEBUTTONDOWN:
            if in_circle(event.pos, (point1X, point1Y), 5):
                mousedown = True
                selected = 1
                
            if in_circle(event.pos, (point2X, point2Y), 5):
                mousedown = True
                selected = 2
            
            if in_circle(event.pos, (controlX, controlY), 5):
                mousedown = True
                selected = 3
            
            
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
            
        if mousedown:
            if selected == 1:
                point1X = mouse_cordinates[0]
                point1Y = mouse_cordinates[1]
                
            if selected == 2:
                point2X = mouse_cordinates[0]
                point2Y = mouse_cordinates[1]
                
            if selected == 3:
                controlX = mouse_cordinates[0]
                controlY = mouse_cordinates[1]
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                resolution += 1
            
            if event.key == pygame.K_DOWN:
                if resolution > 1:
                    resolution -= 1
            
            
    # frame counter at top left
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 30)
    string = f"{(time.time() - cur_time):.5f}"
    text = font.render(string, False, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.update()


            