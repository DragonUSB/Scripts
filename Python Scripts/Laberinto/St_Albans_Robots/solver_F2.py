from random import randint

FILL_CODES = " ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

NORTH = 32
SOUTH = 128
EAST = 64
WEST = 16
VISITED = 8

mazemap = []
mazework = []
for i in range(256):
    mazemap.append(0)
    mazework.append(0)
#    mazework.append(randint(0, 0))

for i in range(len(mazemap)):
    if i < 16:
        mazemap[i] |= NORTH

    if i > 239:
        mazemap[i] |= SOUTH

    if i % 16 == 0:
        mazemap[i] |= WEST
        mazemap[i+15] |= EAST

mazemap[255] |= EAST + SOUTH
mazemap[136] |= NORTH + WEST + EAST + SOUTH

mazemap[136] = NORTH + WEST + EAST
mazemap[135] = EAST
mazemap[137] = WEST
mazemap[138] = NORTH

mazework[136] = 0

def printmaze(mazemap):
    """displays the maze to the shell window"""

    line1 = ""
    line2 = ""

    for i in range(len(mazemap)):
        line1 += "+"
        code = FILL_CODES[mazework[i]%36]
        if (mazemap[i] & NORTH) != 0 or ((mazemap[i-16] & SOUTH) != 0 and i > 15):
            line1 += "-"

        else:
            line1 += " "

        if (mazemap[i] & WEST) != 0 or (mazemap[i-1] & EAST) != 0:
            line2 += "|" + code

        else:
            line2 += " " + code

        if (i+1) % 16 == 0 and mazemap[i] & EAST != 0:
            line2 += "|"

        if (i+1) % 16 == 0:
            line1 += "+"
            print(line1)
            print(line2)
            line1, line2 = "", ""

    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

#printmaze(mazemap)

#setup.py

pos=0
dig=0

def dowall(wall,pos):
    global mazemap
    bit=0
    othpos=0
    othbit=0
    if wall=="W":
        bit=WEST
        othpos = pos-1
        othbit=EAST
    elif wall=="E":
        bit=EAST
        othpos = pos+1
        othbit=WEST
    elif wall=="N":
        bit=NORTH
        othpos = pos-16
        othbit=SOUTH
    elif wall=="S":
        bit=SOUTH
        othpos = pos+16
        othbit=NORTH
    mazemap[pos] |= bit
    if othpos>=0 and othpos<256:
        mazemap[othpos] |= othbit

def setp(strg):
    global pos
    dig=0
    for i in range(len(strg)):
        ch=strg[i].upper()
        if ch in("0123456789"):
            if dig==0:
                pos = int(ch)
            else:
                pos = pos*10 +int(ch)
            dig=1
        else:
            if dig==1:
                print(pos)
            dig=0
            if ch == "U":
                pos -=16
            elif ch== "D":
                pos +=16
            elif ch== "R":
                pos +=1
            elif ch== "L":
                pos -=1
            dowall(ch,pos)
            # print(ch,pos)

Target = 128+8
# Target = 255-36

# from Derek Hall's C++ code:
'''bool mazeClass::solvePart(void) {
  byte high;
  bool solved = true;
  for (int i = 0; i < sizeof(mazemap); i++) {
    if (i == target) {
      mazework[i] = 0;
    } else {
      high = 254;
      if (!(mazemap[i].north)) {
        if (mazework[(byte)i - Maze_Width] < high) {
          high = mazework[(byte)i - Maze_Width];
        }
      }

      if (!(mazemap[i].east)) {
        if (mazework[(byte)i + 1] < high) {
          high = mazework[(byte)i + 1];
        }
      }

      if (!(mazemap[i].south)) {
        if (mazework[(byte)i + Maze_Width] < high) {
          high = mazework[(byte)i + Maze_Width];
        }
      }

      if (!(mazemap[i].west)) {
        if (mazework[(byte)i - 1] < high) {
          high = mazework[(byte)i - 1];
        }
      }
      high++;
      if (mazework[(byte)i] != high) {
        mazework[(byte)i] = high;
        solved = false;
      }
    }
  }
  return solved;
}

'''
def solvepart():
    global solved
    solved = True;
    for i in range(len(mazemap)):
        if i == Target:
            mazework[i]=0
        else:
            high = 254;
            if (mazemap[i]&NORTH)==0:
                if (mazework[i - 20] < high):
                    high = mazework[i - 16];
            if (mazemap[i]&EAST)==0:
                if (mazework[i +1] < high):
                    high = mazework[i + 1];
            if (mazemap[i]&SOUTH)==0:
                if (mazework[i + 16] < high):
                    high = mazework[i + 16];

            if (mazemap[i]&WEST)==0:
                if (mazework[i - 1] < high):
                    high = mazework[i - 1];

            high += 1
            if (mazework[i] != high):
                mazework[i] = high;
                solved = False;

def solve2():
    global solved
    solved = False;
    count=0
    while solved == False:
        solvepart()
        count += 1

    print("Count:",count)
    
        
def checkmaze(mazemap):
    """displays the maze to the shell window"""
    for i in range(len(mazemap)):
        if (mazemap[i] & NORTH) != 0 and (mazemap[i-16] & SOUTH)== 0:
            print(i,"N")

        if (i<255):
            if (mazemap[i] & EAST) != 0 and (mazemap[i+1] & WEST)== 0:
                print(i,"E")
        if (mazemap[i] & WEST) != 0 and (mazemap[i-1] & EAST)== 0:
            print(i,"W")

        if (i<240):
            if (mazemap[i] & SOUTH) != 0 and (mazemap[i+16] & NORTH)== 0 :
                print(i,"S")            

#modify maze

fred = "240EUEUEUNRNSRNSRNSrnedewdewdwsrnsrnsrnsresuwnrnsrnsrnsresuewuewuewuenlnslnslnslnwdewdselswuwuw"
setp(fred)
fred2= "128nrnrnrnrnrnrnrnrnrnrnrnrnrnrnrn"            
setp(fred2)
print(1)
printmaze(mazemap)
checkmaze(mazemap)
solvepart()
print()
print(2)
printmaze(mazemap)
solvepart()
print()
print(3)
printmaze(mazemap)
print("Calling solve2()")
solve2()
print()
print(4)
printmaze(mazemap)