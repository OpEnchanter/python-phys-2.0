import physics, pygame
pygame.init()
window = pygame.display.set_mode([500, 500])
running = True

fps=physics.calc_fps()

phys_obj = physics.object([100, 250], "square", 50, window, 2, fps)
phys_obj2 = physics.object([-100, 250], "square", 50, window, 0.1, fps)

while running:

    # Check for window close event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window
    window.fill((255, 255, 255))

    phys_obj.frame(False)
    phys_obj2.frame(False)
    

    # Apply changes to the window
    pygame.display.flip()

pygame.quit()