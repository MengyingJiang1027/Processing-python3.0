# 作为拓展内容参考：散射开的线条状烟花

class Particle():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = random(0, 360)
        self.Llength = random(1, 50)
        self.process = 0
        self.color = color(random(1, 255), random(1, 255), random(1, 255))
        self.weight = random(5, 10)
        self.speed = random(1, 10)
        
    def display(self):    
        pushMatrix()
        translate(self.x, self.y)
        rotate(self.angle)
        stroke(self.color)
        strokeWeight(self.weight)
        line(0, self.process - self.Llength, 0, self.process)
        popMatrix()
 
    
    def update(self):
        self.process += self.speed
    
    def run(self):
        self.display()
        self.update()
    
    def isDead(self):
        if self.process > 100:
            return True

# 先不使用particleSystem管理粒子系统类

def setup():
    global particles, particle
    size(800, 800)
    particles = []
    #blendMode(ADD)
    #colorMode(HSB)
   

def draw():
    global particles, particle
    background(0, 0, 0)

    
    for particle in particles:
        particle.run()
        if particle.isDead():
            particles.remove(particle)
            print(1)

def mousePressed():
    global particles, particle
    for i in range(15):
        particle = Particle()
        particle.x = mouseX
        particle.y = mouseY
        particles.append(particle)

    
    
            
    
    
    
    
    

        
