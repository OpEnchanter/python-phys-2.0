import main, pygame
pygame.init()
window = pygame.display.set_mode([500, 500])
running = True

print(window)

phys_obj = main.object([100, 250], "square", 50, window, 1)
phys_obj2 = main.object([-100, 250], "square", 50, window, 1)

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