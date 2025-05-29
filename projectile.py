from math import pi, sin, cos

class Projectile:
    def __init__(self, angle, velocity, height):
        self.xpos = 0.0
        self.ypos = height
        theta = pi * angle / 180.0
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1

    def getY(self):
        return self.ypos

    def getX(self):
        return self.xpos

def main():
    print("Projectile Simulation")
    angle = float(input("Enter launch angle (degrees): "))
    velocity = float(input("Enter initial velocity (m/s): "))
    height = float(input("Enter initial height (meters): "))
    time_step = float(input("Enter time interval for simulation (seconds): "))
    p = Projectile(angle, velocity, height)
    while p.getY() >= 0:
        p.update(time_step)
    print(f"\nThe projectile hit the ground at {p.getX():.2f} meters.")

if __name__ == '__main__':
    main()