import pygame, time


class object():
    def __init__(self, start_position = list, object_type = str, object_scale = int, window = pygame.display):
        self.position = [start_position[0] + 250, -start_position[1] + 250]
        self.velocity = [0,0]
        self.elapsed_frames = 0
        self.object_type = object_type
        self.window = window
        self.scale = object_scale
        self.timing = time.time()
        self.frametiming = 0

    def frame(self, show_frame_elapsed = bool):
        
        
        # Draw the object to the screen
        if self.object_type == "circle":
            pygame.draw.circle(self.window, (0, 0, 0), (self.position[0], self.position[1]), self.scale/2)
        elif self.object_type == "square":
            pygame.draw.rect(self.window, (0, 0, 0), (self.position[0] - self.scale/2, self.position[1] - self.scale/2, self.scale, self.scale))

        # Calculate Frame Physics
        
        if time.time()-self.timing >= 1:
            self.timing = time.time()
            print(self.timing/self.frametiming)
            self.frametiming=0

        self.elapsed_frames += 1
        self.frametiming += 1