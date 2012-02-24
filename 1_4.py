colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

def init_probability_distribution(colors):
    sizey = len(colors)
    sizex = len(colors[0])
    uniform = 1. / (sizey * sizex)
    p = [[uniform for x in range(sizex)] for y in range(sizey)]
    return p

def sense(p, colors, color):
    for y in range(len(p)):
        for x in range(len(p[0])):
            if color == colors[y][x]:
                p[y][x] *= sensor_right
            else:
                p[y][x] *= (1 - sensor_right)
    return normalize(p)

def move(p, direction):
    dy = direction[0]
    dx = direction[1]
    q = [[0 for x in range(len(p[0]))] for y in range(len(p))]
    for y in range(len(p)):
        for x in range(len(p[0])):
            s = p[y][x] * (1 - p_move)
            s += p[(y - dy) % len(p)][(x - dx) % len(p[0])] * p_move
            q[y][x] = s
    return normalize(q)           

def normalize(p):
    total = sum(sum(n) for n in p)
    return [map(lambda x: float(x) / total, n) for n in p]

    
p = init_probability_distribution(colors)
for movement, color in zip(motions, measurements):
    p = move(p, movement)
    p = sense(p, colors, color)

#Your probability array must be printed 
#with the following code.

show(p)