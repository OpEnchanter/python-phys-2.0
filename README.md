# Python Physics

### Notes

Engine uses imperial measurement system


### Constants
- Screen Ratio = 1px:1ft
- g = 32.185 ft/s

---

Example Script:
```
import physics, pygame
pygame.init()
window = pygame.display.set_mode([500, 500])
running = True

fps=120
objects = []

def spawn(object_amm, offset, scale, y, type):

    for x in range(object_amm):
        objects.append(physics.object([-250+25+(scale*x)+(offset*x), y], type, scale, window, 1, fps))

    print(objects)

spawn(5, 5, 50, 250, "square")
spawn(7, 5, 50, 350, "circle")

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

FPS Code:
```
if time.time()-self.timing >= 0.01:
            self.fps = int(self.frametiming/(time.time()-self.timing))
            if (show_fps):
                print(self.fps)
            self.frametiming = 0
            self.timing = time.time()
```