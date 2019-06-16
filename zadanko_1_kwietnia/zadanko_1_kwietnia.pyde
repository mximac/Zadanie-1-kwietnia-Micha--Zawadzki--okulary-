add_library('pdf')
global test #wyszło dużo zmiennych xD : te od kooru możnaby ująć w listę i byłoby mniej
global zapis
global r1
global r2
global r3
global a
global b
global c
test=0
zapis=0
r1=0
r2=0
r3=0
a=0
b=0
c=0
def setup():
    global img
    img = loadImage("dowod.jpg") #TU DAJEMY FOTO
    size(198,255)
def draw():
    global zapis
    if keyPressed:
        if key == 'S' or key == 's':
            beginRecord(PDF, "out_img.pdf")
            zapis=1
    global test
    global a
    global b
    global c
    r1=a
    r2=b
    r3=c
    if mousePressed:
        test=1
        r1 = int(random(255))
        r2 = int(random(255))
        r3 = int(random(255))
        a=r1
        b=r2
        c=r3
    image(img, 0, 0)
    s = createShape()
    s.beginShape()
    s.fill(0, 0, 0)
    if test==1:
        s.fill(r1,r2,r3)
    s.noStroke()
    s.vertex(width/10, height/2.8)
    s.vertex(width/10, height/2)
    s.vertex(width/3.3, height/2)
    s.vertex(width/3.3, height/2.8)
    s.endShape(CLOSE)
    shape(s, 25, 25)
    s = createShape()
    s.beginShape()
    s.fill(0, 0, 0)
    if test==1:
        s.fill(r1,r2,r3)
    s.noStroke()
    s.vertex(width/2.3, height/2.8)
    s.vertex(width/2.3, height/2)
    s.vertex(width/1.55, height/2)
    s.vertex(width/1.55, height/2.8)
    s.endShape(CLOSE)
    shape(s, 25, 25)
    s = createShape()
    s.beginShape()
    s.fill(0, 0, 0)
    if test==1:
        s.fill(r1,r2,r3)
    s.noStroke()
    s.vertex(width/15, height/2.5)
    s.vertex(width/15, height/2.3)
    s.vertex(width/1.45, height/2.3)
    s.vertex(width/1.45, height/2.5)
    s.endShape(CLOSE)
    shape(s, 25, 25)
    if zapis==1:
        endRecord()
        exit()
    
