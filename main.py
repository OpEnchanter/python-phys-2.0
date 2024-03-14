import physics, pygame
pygame.init()
window = pygame.display.set_mode([500, 500])
running = True

fps=120

phys_obj = physics.object([0, 250], "square", 50, window, 1, fps)
phys_obj2 = physics.object([0, 450], "square", 50, window, 1, fps)


clock = pygame.time.Clock()
while running:
                                                                              
    # Check for window close event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window
    window.fill((255, 255, 255))

    phys_obj.frame(False, [phys_obj2])
    phys_obj2.frame(False, [phys_obj])

    # Apply changes to the window
    pygame.display.flip()

    clock.tick(fps)

pygame.quit()

