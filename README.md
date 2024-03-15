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
object = physics.object(start_position = list, start_velocity = list, object_type = str, object_scale = int, window = pygame.display, density = float, elasticity = float, roughness = float, fps = int) # Package default object creation

spawn(object_amm, offset, scale, starting_pos, starting_vel, type, density, elasticity, roughness) # Create more than one object using example script built in definition (spawn())
```

---

Example Script:
``` python
import physics, pygame, time
pygame.init()
window = pygame.display.set_mode([500, 500])
running = True

fps=120
objects = []

def spawn(object_amm, offset, scale, starting_pos, starting_vel, type, density):

    for x in range(object_amm):
        objects.append(physics.object([starting_pos[0]+(scale/2)+(offset*x)+(scale*x), starting_pos[1]], starting_vel,  type, scale, window, density, fps))

    print(objects)

#spawn(1, 0, 25, [-200, 350], [100, 0], "square")
#spawn(1, 0, 25, [-100, 350], [-100, 0], "square")
spawn(1, 0, 25, [0, 350], [100, 0], "square", 1)


clock = pygame.time.Clock()
while running:

    #spawn(3, 10, 10, [-200, 350], [100, 0], "square")

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