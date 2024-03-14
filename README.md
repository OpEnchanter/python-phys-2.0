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

fps=physics.calc_fps()

phys_obj = physics.object([-100, 250], "circle", 50, window, 1, fps)
phys_obj2 = physics.object([100, 250], "square", 50, window, 1, fps)

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