
import random, math, matplotlib.pyplot as plt

SITE_WIDTH, SITE_HEIGHT = 200, 140
TOWER_A, TOWER_B = (30,20), (20,20)
MIN_BUILDING_GAP, MIN_BOUNDARY_GAP = 15, 10
PLAZA_SIZE = 40
PLAZA_X, PLAZA_Y = (SITE_WIDTH-PLAZA_SIZE)/2, (SITE_HEIGHT-PLAZA_SIZE)/2

plaza = {"x":PLAZA_X,"y":PLAZA_Y,"width":PLAZA_SIZE,"height":PLAZA_SIZE}

def overlaps(a,b):
    return not (a["x"]+a["width"]<=b["x"] or b["x"]+b["width"]<=a["x"] or
                a["y"]+a["height"]<=b["y"] or b["y"]+b["height"]<=a["y"])

def within(b):
    return b["x"]>=MIN_BOUNDARY_GAP and b["y"]>=MIN_BOUNDARY_GAP and            b["x"]+b["width"]<=SITE_WIDTH-MIN_BOUNDARY_GAP and            b["y"]+b["height"]<=SITE_HEIGHT-MIN_BOUNDARY_GAP

def dist(a,b):
    return math.hypot(a["x"]-b["x"], a["y"]-b["y"])

def gen(t):
    w,h=TOWER_A if t=="A" else TOWER_B
    return {"type":t,"x":random.uniform(0,SITE_WIDTH-w),"y":random.uniform(0,SITE_HEIGHT-h),"width":w,"height":h}

def valid(bs):
    for b in bs:
        if not within(b) or overlaps(b,plaza): return False
    for i in range(len(bs)):
        for j in range(i+1,len(bs)):
            if dist(bs[i],bs[j])<MIN_BUILDING_GAP: return False
    for a in [b for b in bs if b["type"]=="A"]:
        if not any(dist(a,b)<=60 for b in bs if b["type"]=="B"): return False
    return True

def draw(bs,i):
    fig,ax=plt.subplots()
    ax.add_patch(plt.Rectangle((0,0),SITE_WIDTH,SITE_HEIGHT,fill=False))
    ax.add_patch(plt.Rectangle((PLAZA_X,PLAZA_Y),PLAZA_SIZE,PLAZA_SIZE,color="gray",alpha=.4))
    for b in bs:
        ax.add_patch(plt.Rectangle((b["x"],b["y"]),b["width"],b["height"],
                     color="blue" if b["type"]=="A" else "green",alpha=.7))
    ax.set_aspect("equal")
    plt.savefig(f"output/layout_{i}.png")
    plt.close()

def main():
    c=0
    while c<2:
        bs=[gen("A"),gen("A"),gen("B"),gen("B"),gen("B")]
        if valid(bs):
            draw(bs,c+1)
            c+=1

if __name__=="__main__": main()
