import pygame, sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('TEST')

pos = pygame.mouse.get_pos()
clock = pygame.time.Clock()

while True:
    pos_x, pos_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            rel_x, rel_y = event.rel
            rel_x1 = rel_x %2
            rel_y1 = rel_y %2
            #print(f"Chuột di chuyển: x: {rel_x}, y: {rel_y}")
            if rel_x > 0 :
                print(f"Chuột di chuyển sang bên phải x:{rel_x}, y: {rel_y}")
            elif rel_x < 0:
                print(f"Chuột di chuyển sang bên trái x:{rel_x}, y: {rel_y}")
            if rel_y > 0:
                print(f"Chuột di chuyển xuống dưới x:{rel_x}, y: {rel_y}")
            elif rel_y < 0:
                print(f"Chuột di chuyển lên trên x:{rel_x}, y: {rel_y}")
                               
    clock.tick(1.5)          
           
    rel_x, rel_y = pygame.mouse.get_rel()
    #print({rel_x}, {rel_y})
    #print({pos_x}, {pos_y})
    # In ra hướng di chuyển của chuột

        
    
    pygame.display.update()
            