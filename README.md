# Python Physics

### Notes

Engine uses imperial measurement system


### Constants
- Screen Ratio = 1px:1ft
- g = 32.185 ft/s

---

Example Script:
```
import main, pygame
pygame.init()
window = pygame.display.set_mode([500, 500])
running = True

print(window)

phys_obj = main.object([0, 0], "square", 50, window)
phys_obj2 = main.object([55, 0], "square", 50, window)

while running:

    # Check for window close event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window
    window.fill((255, 255, 255))

    phys_obj.frame()
    phys_obj2.frame()
    

    # Apply changes to the window
    pygame.display.flip()

pygame.quit()
```
