#I hereby certify that this program is solely the result of my own work and is in compliance with the Academic Integrity policy of the course syllabus and the academic integrity policy of the CS department
import math
import Draw

#all upper-case variables are constant
#initialize all variables needed to compute position, velocity, and acceleration
STRING_LENGTH = 400 #m
BOB_RADIUS=30
MAX_ANGLE= math.radians(45)
GRAVITY = 9.81 #m/s^2
ANGULAR_FREQUENCY = (GRAVITY / STRING_LENGTH)**.5 #rad/s
PERIOD = (2 * (math.pi)) / ANGULAR_FREQUENCY #seconds
PHASE_CONSTANT = 0 #Because it is released from the maximum angle
    
#initialize variables needed to compute tension and weight
PENDULUM_BOB_MASS = 5 #kg
    
#initialize variables needed to compute kinetic, potential, and total mechanical energies
PENDULUM_MASS = 10 #kg   
    
#initialize all variables for animation
CANVAS_SIZE=1000 
ANIMATION_TIME= .2 #seconds
TOTAL_DURATION = 2 * PERIOD #seconds
NUM_FRAMES = int(TOTAL_DURATION/ANIMATION_TIME)  
OFFSET=.05 

#initialize all variables for arrow heads
ARROW_LENGTH= 10 #pixels
ARROW_ANGLE_RADIANS= math.radians(30)

def compute (MAX_ANGLE,ANGULAR_FREQUENCY,time,PHASE_CONSTANT,STRING_LENGTH):
    #compute position, velocity, acceleration, horizontal and vertical postions of the bob
    position = MAX_ANGLE * math.cos(ANGULAR_FREQUENCY * (time) + PHASE_CONSTANT) #rad
    velocity = (MAX_ANGLE*ANGULAR_FREQUENCY) * math.sin(ANGULAR_FREQUENCY * (time) + PHASE_CONSTANT) #rad/s
    acceleration = (MAX_ANGLE*(ANGULAR_FREQUENCY**2)) * math.cos(ANGULAR_FREQUENCY * (time) + PHASE_CONSTANT) #rad/s^2
    x = STRING_LENGTH * math.sin(position)  
    y = STRING_LENGTH * math.cos(position)       
    return position, velocity, acceleration, x, y

def drawPendulum(x,y,BOB_RADIUS,CANVAS_SIZE):
    #draw the pole
    Draw.setColor(Draw.BLACK)
    Draw.line((CANVAS_SIZE/2),0,(CANVAS_SIZE/2), CANVAS_SIZE)
    
    #draw the string 
    Draw.line((CANVAS_SIZE/2),0, (CANVAS_SIZE/2) + x, y)
    
    #draw the ball based on position
    Draw.setColor(Draw.RED)
    Draw.filledOval((CANVAS_SIZE/2) + x - (BOB_RADIUS/2), y - (BOB_RADIUS/2), BOB_RADIUS, BOB_RADIUS)
    return None

def vector (x1, y1, x2, y2, ARROW_LENGTH, ARROW_ANGLE_RADIANS):
    #draw three lines offset from one another for the line to be more visible
    Draw.line(x1 - OFFSET, y1, x2, y2)
    Draw.line(x1, y1, x2, y2)
    Draw.line(x1 + OFFSET, y1, x2, y2)

    #compute angle of the main line
    angle = math.atan2(y2 - y1, x2 - x1) #needed because line is not horizonal and constantlty changing, returns radians 
   
    #compute angles for the arrowheads
    angle1 = angle - ARROW_ANGLE_RADIANS
    angle2 = angle + ARROW_ANGLE_RADIANS
    
    # Draw arrowheads
    Draw.line(x2, y2, x2 - (ARROW_LENGTH * math.cos(angle1)), y2 - (ARROW_LENGTH * math.sin(angle1)))
    Draw.line(x2, y2, x2 - (ARROW_LENGTH * math.cos(angle2)), y2 - (ARROW_LENGTH * math.sin(angle2)))
    return None

def drawPlain():
    for frame in range(NUM_FRAMES):
        time = frame * ANIMATION_TIME
        
        #compute new position, velocity, acceleration
        position, velocity, acceleration, x, y = compute(MAX_ANGLE,ANGULAR_FREQUENCY,time,PHASE_CONSTANT,STRING_LENGTH)
        
        #clear the canvas
        Draw.clear()
        
        #draw the pendulum
        drawPendulum(x, y, BOB_RADIUS, CANVAS_SIZE)
        
        #draw text
        Draw.setFontFamily('American Typewriter')
        Draw.setFontSize(32)
        Draw.setFontBold(True)
        Draw.string("SIMPLE PENDULUM", 50, 50)

        #show the canvas
        Draw.show(ANIMATION_TIME)
        
def drawVelocity():
    for frame in range(NUM_FRAMES):
        time = frame * ANIMATION_TIME            
        
        #compute new position, velocity, acceleration
        position, velocity, acceleration, x, y = compute(MAX_ANGLE,ANGULAR_FREQUENCY,time,PHASE_CONSTANT,STRING_LENGTH)
        
        #clear the canvas
        Draw.clear()
        drawPendulum(x,y,BOB_RADIUS,CANVAS_SIZE)
            
        #calculate the velocity magnitude
        scaleFactor= 400 #needed in order for the vector to appear for the animation
        velocityMagnitude= (velocity * scaleFactor)
        
        #translate x and y by 90 degrees to point in the direction the bob is moving 
        tangentX = (-y / STRING_LENGTH)
        tangentY = (x / STRING_LENGTH)       
            
        #draw the velocity vector
        Draw.setColor(Draw.BLUE)
        vector((CANVAS_SIZE/2) + x , y,(CANVAS_SIZE/2) + x + (velocityMagnitude* tangentX), y+ (velocityMagnitude * tangentY),ARROW_LENGTH, ARROW_ANGLE_RADIANS)          

        #draw informational text
        Draw.string("VELOCITY VECTOR", 50, 50)

        #draw.show
        Draw.show(ANIMATION_TIME)
        
def drawAcceleration():
    for frame in range(NUM_FRAMES):
        time = frame * ANIMATION_TIME 
        
        #compute new position, velocity, acceleration
        position, velocity, acceleration, x, y = compute(MAX_ANGLE,ANGULAR_FREQUENCY,time,PHASE_CONSTANT,STRING_LENGTH)
        
        #clear the canvas
        Draw.clear()  
        
        #draw the pendulum
        drawPendulum(x, y, BOB_RADIUS, CANVAS_SIZE)
        
        #compute radial and tangential acceleration
        scaleFactorTangential = 8 #needed in order for the vector to appear for the animation
        scaleFactorRadial = 1500000 #needed in order for the vector to appear for the animation
        radialAcceleration = (velocity ** 2) / STRING_LENGTH #m/s^2  
        tangentialAcceleration = GRAVITY * math.sin(position) #m/s^2
        radialX = (-x / STRING_LENGTH) * radialAcceleration * scaleFactorRadial
        radialY = (-y / STRING_LENGTH) * radialAcceleration * scaleFactorRadial
        tangentialX = -(y / STRING_LENGTH) * tangentialAcceleration * scaleFactorTangential 
        tangentialY = (x / STRING_LENGTH) * tangentialAcceleration * scaleFactorTangential      

        #draw the two acceleration components:
        #draw the radial acceleration 
        Draw.setColor(Draw.DARK_GREEN)  
        vector ((CANVAS_SIZE/2) + x, y, (CANVAS_SIZE/2) + x + radialX, y + radialY, ARROW_LENGTH,ARROW_ANGLE_RADIANS)
        
        #draw informational text
        Draw.setFontSize(24)
        Draw.string("RADIAL ACCELERATION", 50, 50)
        
        #draw the tangental acceleration 
        Draw.setColor(Draw.BLUE)
        vector((CANVAS_SIZE/2) + x, y,(CANVAS_SIZE/2) + x + tangentialX, y+ tangentialY,ARROW_LENGTH, ARROW_ANGLE_RADIANS)
        
        #draw informational text 
        Draw.string("TANGENTIAL ACCELERATION", 575, 50)
        
        #draw.show
        Draw.show(ANIMATION_TIME)
        
def drawForces():
    for frame in range(NUM_FRAMES):
        time = frame * ANIMATION_TIME 
            
        #compute new position, velocity, acceleration
        position, velocity, acceleration, x, y = compute(MAX_ANGLE,ANGULAR_FREQUENCY,time,PHASE_CONSTANT,STRING_LENGTH)
            
        #clear the canvas
        Draw.clear()  
            
        #draw the pendulum
        drawPendulum(x, y, BOB_RADIUS, CANVAS_SIZE)
            
        #compute weight and tension
        weight = PENDULUM_BOB_MASS * GRAVITY #newtons
        tension = weight * math.cos (position) + (PENDULUM_BOB_MASS * (velocity **2)/ STRING_LENGTH) #newtons
        tensionX = -tension * math.sin(position) #negative tension to point in the direction of the pivot
        tensionY = -tension * math.cos(position) #negative tension to point in the direction of the pivot         

        #draw the constant weight vector
        Draw.setColor(Draw.BLUE)
        vector((CANVAS_SIZE/2) + x, y,(CANVAS_SIZE/2) + x, y + (weight),ARROW_LENGTH, ARROW_ANGLE_RADIANS)

        #draw informational text
        Draw.setFontSize(32)
        Draw.string("WEIGHT", 50, 450)

        #draw the tension vector
        Draw.setColor(Draw.VIOLET)
        vector((CANVAS_SIZE/2) + x, y,(CANVAS_SIZE/2) + x +tensionX, y + tensionY,ARROW_LENGTH, ARROW_ANGLE_RADIANS)

        #draw informational text
        Draw.string("TENSION", 50, 50)

        #draw.show
        Draw.show(ANIMATION_TIME)
        
def drawEnergy():
    for frame in range(NUM_FRAMES*2):
        time = frame * ANIMATION_TIME 

        #compute new position, velocity, acceleration
        position, velocity, acceleration, x, y = compute(MAX_ANGLE,ANGULAR_FREQUENCY,time,PHASE_CONSTANT,STRING_LENGTH)
        
        #clear the canvas
        Draw.clear()  
        
        #draw the pendulum
        drawPendulum(x, y, BOB_RADIUS, CANVAS_SIZE)
        
        #initialize variables needed to compute energies
        pendulumHeight = STRING_LENGTH * (1- math.cos(position))
        
        #calculate bob velocity by converting from angular velocity to linear velocity 
        bobVelocity = STRING_LENGTH * velocity
        
        #compute kinetic, potential, and total mechanical energies
        kinetic = .5 * PENDULUM_MASS * (bobVelocity **2) #joules
        gravitationalPotential = PENDULUM_MASS * GRAVITY * pendulumHeight #joules
        totalMechanical = (kinetic + gravitationalPotential) #joules
        graphScaleFactor = .03 #needed in order for the graphs to appear for the animation
        
        #draw informational text 
        Draw.setFontSize(32)
        Draw.setFontBold(True)
        Draw.setColor(Draw.BLUE)
        Draw.string("ENERGY", 50, 50)

        #draw the Kinetic Energy Bar
        Draw.setFontSize(12)
        Draw.setFontBold(False)
        Draw.setColor(Draw.BLUE)
        Draw.filledRect(800, 700, 8, -kinetic*graphScaleFactor)

        #draw informational text 
        Draw.string("KE", 795, 710)            

        #draw the Gavitational Potential Energy Bar
        Draw.setColor(Draw.ORANGE)
        Draw.filledRect(830, 700, 8, -gravitationalPotential*graphScaleFactor)
        
        #draw informational text 
        Draw.string("PE", 825, 710)                
        
        #draw the Total Mechanical Energy Bar
        Draw.setColor(Draw.DARK_GREEN)
        Draw.filledRect(860, 700, 8, -totalMechanical*graphScaleFactor)
    
        #draw informational text 
        Draw.string("TE", 855, 710) 
        
        #draw.show
        Draw.show(ANIMATION_TIME)

def animate (type):
    if type == "plain":
        drawPlain ()            
    elif type == "velocity":
        drawVelocity()  
    elif type == "acceleration":
        drawAcceleration()     
    elif type == "forces":
        drawForces() 
    elif type == "energy":
        drawEnergy()

def main ():
    canvasSize=1000
    Draw.setCanvasSize(canvasSize,canvasSize)
    animate ("plain")
    animate ("velocity")
    animate ("acceleration")
    animate ("forces")
    animate ("energy")
    
main ()