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
    def __init__(self, start_position = list, start_velocity = list, object_type = str, object_scale = int, window = pygame.display, density = float, elasticity = float, roughness = float, deltaTime = int, draggable = bool):
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

        self.can_pick_up = draggable

        self.object_type = object_type
        self.elapsed_frames = 0
        self.window = window
        self.timing = time.time()
        self.frametiming = 0
        self.deltaTime = deltaTime

        self.drag = self.g/(self.density*10)

        self.grabbing = False

        self.last_frame_pos = start_position
        self.last_frame_grabbing = False
        self.idx = 0

    def frame(self, show_fps = bool, collision_objects = list, other_grabbed = bool):
        self.frametiming += 1

        # Calculate Frame Physics
        self.velocity[1] -= (self.g - self.drag)

        self.position[1] += self.velocity[1]*self.deltaTime
        self.position[0] += self.velocity[0]*self.deltaTime
        self.position[1] = math.floor(self.position[1])

        # Check for mouse grab
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x -= 250
        mouse_y = 500-mouse_y

        if (self.grabbing and pygame.mouse.get_pressed()[0]):
            self.grabbing = True
        elif (pygame.mouse.get_pressed()[0]):
            self.grabbing = pygame.mouse.get_pressed()[0] and (mouse_x > self.position[0] - self.scale/2 and mouse_x < self.position[0] + self.scale/2) and (mouse_y > self.position[1] - self.scale/2 and mouse_y < self.position[1] + self.scale/2)
        else:
            self.grabbing = False
        
        if (other_grabbed):
            self.grabbing = False

        self.grabbing = self.grabbing and self.can_pick_up


        if (self.grabbing):
            self.position = [mouse_x, mouse_y]
            self.velocity = [0, 0]
            pygame.mouse.set_visible(False)
        elif (self.last_frame_grabbing):
            self.position = [mouse_x, mouse_y]
            x_vel = (mouse_x - self.last_frame_pos[0])*30
            y_vel = (mouse_y - self.last_frame_pos[1])*30
            self.velocity = [x_vel, y_vel]
            pygame.mouse.set_visible(True)
        else:
            pygame.mouse.set_visible(True)

        self.last_frame_grabbing = self.grabbing
        if (self.idx >= 3):
            self.last_frame_pos = self.position
            self.idx = 0
        self.idx += 1
        
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
            self.position[1] += self.velocity[1]*self.deltaTime
            self.position[0] += self.velocity[0]*self.deltaTime
        elif self.position[1] >= 500 - self.scale/2: # Y axis top boundary
            self.position[1] = 500-(self.scale/2)
            self.velocity[0] = self.velocity[0] - self.velocity[0] * self.roughness
            self.velocity[1] = -self.velocity[1] * self.elasticity
            self.position[1] += self.velocity[1]*self.deltaTime
            self.position[0] += self.velocity[0]*self.deltaTime
            

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

class rot_square:
    def __init__(self, dpf=0.1, scale=100, window=None):
        self.dpf = dpf  # degrees per frame
        self.scale = scale
        self.angles = [0, 90, 180, 270]
        self.window = window
        self.points = [(), (), (), ()]

    def frame(self):
        for x in range(len(self.points)):
            dist = self.scale / 2
            self.angles[x] += self.dpf
            self.points[x] = (250 + math.sin(math.radians(self.angles[x])) * dist,
                               250 + math.cos(math.radians(self.angles[x])) * dist)
            self.angles[x] += self.dpf
        pygame.draw.polygon(self.window, (self.angles[2]//255, self.angles[1]//255, self.angles[0]//255), self.points)

