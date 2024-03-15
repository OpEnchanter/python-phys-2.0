# Python Physics

### Notes

Engine uses imperial measurement system


### Constants
- Screen Ratio = 1px:1ft
- g = 32.185 ft/s

### Objects
#### Types
- Circle : ``"circle"``
- Sqaure : ``"square"``
- Triangle : ``"triangle"``
#### Code
```python
import physics, pygame
pygame.init()
window = pygame.display.set_mode([500, 500])
running = True

fps=120
objects = []

def spawn(object_amm, offset, scale, starting_pos, starting_vel, type, density, elasticity, roughness):

    for x in range(object_amm):
        objects.append(physics.object([starting_pos[0]+(scale/2)+(offset*x)+(scale*x), starting_pos[1]], starting_vel,  type, scale, window, density, elasticity, roughness, fps))

spawn(1, 10, 25, [-100, 350], [-1000, 100], "square", 1, 0.57, 0.1)




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
```