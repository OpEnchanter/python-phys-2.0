import pygame, time, math

def calc_fps():
    frametiming = 0
    timing = time.time()
    checking_fps = True
    while(checking_fps):
        frametiming += 1
        if time.time()-timing >= 1:
            fps = int(frametiming/(time.time()-timing))
            checking_fps=False
            return(fps)


class object():
    def __init__(self, start_position = list, object_type = str, object_scale = int, window = pygame.display, density = int, fps = int):
        # Physics Variables

        self.position = [start_position[0], start_position[1]]
        self.velocity = [0,0]


        # Physics Constants

        self.g = 315.09
        self.scale = object_scale
        self.density = density
        self.volume = 0

        if object_type == "circle":
            self.volume = (((self.scale/2)**2) * 3.14)
        elif object_type == "square":
            self.volume = self.scale**2

        self.mass = self.density * self.volume

        print(self.mass)


        # Simulation Variables

        self.object_type = object_type
        self.elapsed_frames = 0
        self.window = window
        self.timing = time.time()
        self.frametiming = 0
        self.fps = fps

        self.drag = 0
        

    def frame(self, show_fps = bool):
        self.frametiming += 1
        
        # Draw the object to the screen
        if self.object_type == "circle":
            pygame.draw.circle(self.window, (0, 0, 0), [self.position[0]+250, (500-self.position[1])], self.scale/2)
        elif self.object_type == "square":
            pygame.draw.rect(self.window, (0, 0, 0), (self.position[0] - self.scale/2 + 250, (500-self.position[1]) - self.scale/2, self.scale, self.scale))

        # Calculate Frame Physics
        if self.position[1] <= 0 + self.scale/2 and abs(self.velocity[1]) > 0.01:
            self.position[1] = 0+self.scale/2
            self.velocity[1] = 0
        elif self.position[1] >= 500 - self.scale/2 and abs(self.velocity[1]) > 0.01:
            self.position[1] = 500-self.scale/2
            self.velocity[1] = 0
        elif abs(self.velocity[1]) > 0:
            self.drag = self.g / (self.density*10)
        self.velocity[1] -= (self.g - self.drag) / self.fps

        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        # Calulate Simulation fps
        if time.time()-self.timing >= 1:
            self.fps = int(self.frametiming/(time.time()-self.timing))
            if (show_fps):
                print(self.fps)
            self.frametiming = 0
            self.timing = time.time()


        self.elapsed_frames += 1