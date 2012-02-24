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

def init_probability_distribution():
    p = []
    sizey = len(colors)
    sizex = len(colors[0])
    uniform = 1. / (sizey * sizex)
    p = [[[uniform] for x in range(sizex)] for y in range(sizey)]
    return p

p = init_probability_distribution()




#Your probability array must be printed 
#with the following code.

show(p)