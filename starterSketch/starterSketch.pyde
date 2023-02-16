def settings():
    size(500,500)
    
def setup():
    colorMode(HSB)
    
SQUARE_MAX = 50
    
def recSquare(depth):
    fill(map(depth, 0, SQUARE_MAX,0, 255),255,255)
    rotate(TAU/SQUARE_MAX * frameCount/1000)
    if depth == 0:
        return
    gapX = width/SQUARE_MAX
    gapY = height/SQUARE_MAX
    pX = -(gapX * depth)/2
    pY = -(gapY * depth)/2
    square(pX, pY, depth * max(gapX, gapY))
    recSquare(depth -1)
    
TREE_MAX = 10

def recTree(x, y, ang, depth):
    colorMode(RGB)
    strokeWeight(depth)
    stroke(255,map(depth, 0, TREE_MAX, 0, 255), 255)
    if depth == 0:
        return
    pX = x + (depth * 5 * cos(ang - PI/2))
    pY = y + (depth * 5 * sin(ang - PI/2))
    line(x,y, pX, pY)
    recTree(pX, pY, ang + PI/6, depth -1)
    recTree(pX, pY, ang - PI/6, depth -1)

count = 0

def draw():
    colorMode(HSB)
    global count
    background(0)
    translate(width/2, height/2)
    if frameCount % 120 == 0:
        count += 1
    if count % 2 == 0:
        recSquare(SQUARE_MAX)
    if count % 2 == 1:
        recTree(0,height/3,0,TREE_MAX)
