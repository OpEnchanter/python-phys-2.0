import physics, pygame
pygame.init()
window = pygame.display.set_mode([500, 500])
running = True

fps=120
clock = pygame.time.Clock()
deltaTime = clock.tick(fps)/1000
objects = []

def spawn(object_amm, offset, scale, starting_pos, starting_vel, type, density, elasticity, roughness, draggable):

    for x in range(object_amm):
        objects.append(physics.object([starting_pos[0]+(scale/2)+(offset*x)+(scale*x), starting_pos[1]], starting_vel,  type, scale, window, density, elasticity, roughness, deltaTime, draggable))

spawn(5, 10, 25, [-100, 350], [0, 0], "square", 1, 0.57, 0.1, True)


while running:

    # Check for window close event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window
    window.fill((255, 255, 255))

    for object in objects:
        other_obj = [obj for obj in objects if obj != object]

        any_grabbed = False
        for obj in other_obj:
            if obj.grabbing:
                any_grabbed = True

        object.frame(False, other_obj, any_grabbed)

    # Apply changes to the window
    pygame.display.flip()

    clock.tick(fps)

pygame.quit()

