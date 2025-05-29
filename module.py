from projectile import Projectile

# Set the angle, velocity, and initial height
angle = 45  # Launch angle in degrees
velocity = 50  # Initial velocity in m/s
height = 10  # Launch height in meters

# Create a projectile instance
proj = Projectile(angle, velocity, height)

# Simulate the flight for a specified time interval
time_interval = 0.1  # Time step in seconds
while proj.getY() > 0:  # Stop when the projectile hits the ground 
    proj.update(time_interval)
    print(f"Position: ({proj.getX():.2f}, {proj.getY():.2f})")

print("The projectile has landed.")