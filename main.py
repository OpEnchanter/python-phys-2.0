import physics, pygame
pygame.init()
window = pygame.display.set_mode([500, 500])
running = True

fps=120
objects = []

def spawn(object_amm, offset, scale, starting_pos, type):

    for x in range(object_amm):
        objects.append(physics.object([starting_pos[0]+(scale/2)+(offset*x)+(scale*x), starting_pos[1]], type, scale, window, 1, fps))

    print(objects)

spawn(1, 0, 250, [-25, 750], "triangle")

clock = pygame.time.Clock()
while running:
                                                                              
    # Check for window close event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window
    window.fill((255, 255, 255))

    for object in objects:
        other_obj = [obj for obj in objects if obj != object]
        object.frame(False, other_obj)

    # Apply changes to the window
    pygame.display.flip()

    clock.tick(fps)

pygame.quit()

