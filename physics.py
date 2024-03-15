import pygame, time, math, sys

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
    def __init__(self, start_position = list, start_velocity = list, object_type = str, object_scale = int, window = pygame.display, density = float, elasticity = float, roughness = float, fps = int):
        # Physics Variables

        self.position = [start_position[0], start_position[1]]
        self.velocity = start_velocity


        # Physics Constants

        self.g = 17.75
        self.scale = object_scale
        self.density = density
        self.volume = 0

        self.drag = self.g / (self.density*10)

        if object_type == "circle":
            self.volume = (((self.scale/2)**2) * 3.14)
        elif object_type == "square":
            self.volume = self.scale**2
        elif object_type == "triange":
            self.volume = (self.scale**2)/2

        self.mass = self.density * self.volume

        self.elasticity = elasticity
        self.roughness = roughness

        #print(self.mass)


        # Simulation Variables

        self.object_type = object_type
        self.elapsed_frames = 0
        self.window = window
        self.timing = time.time()
        self.frametiming = 0
        self.fps = fps

        self.drag = self.g/(self.density*10)
        

    def frame(self, show_fps = bool, collision_objects = list):
        self.frametiming += 1

        # Calculate Frame Physics
        self.velocity[1] -= (self.g - self.drag)

        self.position[1] += self.velocity[1]/self.fps
        self.position[0] += self.velocity[0]/self.fps
        self.position[1] = math.floor(self.position[1])
        
        # Check for collision with other objects
        for object in collision_objects:
            y_collision = self.position[1] < object.position[1] + object.scale/2 and self.position[1] > object.position[1] - object.scale/2
            if self.position[1] <= (object.position[1] + object.scale/2) + self.scale/2 and self.position[1] > object.position[1] and self.position[0] >= object.position[0]-object.scale/2 and self.position[0] <= object.position[0] + object.scale/2:
                self.position[1] = (object.position[1] + object.scale/2) + (self.scale/2)
                self.velocity[1] = -self.velocity[1] * self.elasticity
            elif self.position[1] >= (object.position[1] - object.scale/2) - self.scale/2 and self.position[1] < object.position[1] and self.position[0] >= object.position[0]-object.scale/2 and self.position[0] <= object.position[0] + object.scale/2 and self.density < 0.1:
                self.position[1] = (object.position[1] - object.scale/2) - (self.scale/2)
                self.velocity[1] = -self.velocity[1] * self.elasticity

            if (self.position[0]-self.scale/2 <= object.position[0]+object.scale/2 and self.position[0]-self.scale/2 >= object.position[0]-object.scale/2 and y_collision):
                self.position[0] = object.position[0] + object.scale/2 + self.scale/2
                self.velocity[0] = -self.velocity[0] * self.elasticity
            elif (self.position[0]+self.scale/2 >= object.position[0]-object.scale/2 and self.position[0]+self.scale/2 <= object.position[0]+object.scale/2 and y_collision):
                self.position[0] = object.position[0] - object.scale/2 - self.scale/2
                self.velocity[0] = -self.velocity[0] * self.elasticity

        # Hardcoded window boundary
                
        if self.position[1] <= 0 + self.scale/2: # Y axis bottom boundary
            self.position[1] = 0+(self.scale/2)
            self.velocity[0] = self.velocity[0] - self.velocity[0] * self.roughness
            self.velocity[1] = -self.velocity[1] * self.elasticity
        elif self.position[1] >= 500 - self.scale/2: # Y axis top boundary
            self.position[1] = 500-(self.scale/2)
            self.velocity[0] = self.velocity[0] - self.velocity[0] * self.roughness
            self.velocity[1] = -self.velocity[1] * self.elasticity
            

        if self.position[0] >= 250 - self.scale/2: # X axis right boundary
            self.position[0] = 250 - self.scale/2
            self.velocity[0] = -self.velocity[0] * self.elasticity
        elif self.position[0] <= -250 + self.scale/2: # X axis left boundary
            self.position[0] = -250 + self.scale/2
            self.velocity[0] = -self.velocity[0] * self.elasticity

         # Draw the object to the screen
        if self.object_type == "circle":
            pygame.draw.circle(self.window, (0, 0, 0), [self.position[0]+250, (500-self.position[1])], self.scale/2)
        elif self.object_type == "square":
            pygame.draw.rect(self.window, (0, 0, 0), (self.position[0] - self.scale/2 + 250, (500-self.position[1]) - self.scale/2, self.scale, self.scale))
        elif self.object_type == "triangle":
            pygame.draw.polygon(self.window, (0, 0, 0), ((250+self.position[0]-self.scale/2, 500-self.position[1]+self.scale/2), (250+self.position[0]-1, 500-(self.position[1]+self.scale/2)), (250+(self.scale/2)+self.position[0], 500-self.position[1]+self.scale/2)))

        self.elapsed_frames += 1