# Weds 11 Jan 14:03 works.
from random import randint



FILL_CODES = " V^<>ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
DOWN = 1
UP=2
LEFT=3
RIGHT=4



NORTH = 32
SOUTH = 128
EAST = 64
WEST = 16
VISITED = 8

DONE = 4             # bitmap done flag in eacj cell
negDONE = 255-DONE   # inverse of DONE
done = 0             # either 4 or 0


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
mazework[136] = 0

def printmaze(mazemap):
    """displays the maze to the shell window"""

    line1 = ""
    line2 = ""

    for i in range(len(mazemap)):
        line1 += "+"
        code = FILL_CODES[mazework[i]%32]
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
            #print(ch,pos)

Target = 128+8
Target = 255-32

# from BASIC version
'''

solve_maze:				'Solve the maze

	'save varibals
	poke backup_b0,map_walls
	poke backup_b1,map_walls2
	
	switch on yellow_led
	let list1=$50		'initalize list1 address
	let list2=$C0		'initalize list2 address
	poke list1,target		'add maze center to list 1
	poke $51,target		'terminate list1
	read target,map_walls2
	let w_done2=done
	write target,map_walls2
	
	do
		do
			peek list1,maze_pos 'get next pos from list1
			inc list1
			
			read maze_pos,map_walls2 	'get wall map
			

			if w_north2=0 then
								'add_north
				let b2=maze_pos-16
				read b2,map_walls
				if w_done<>done and w_south=0 then
					let w_done=done
					let w_direc1=0
					let w_direc2=1
					write b2,map_walls
					poke list2,b2	 'add to list2
					inc list2	
				endif
			endif
			
			if w_south2 = 0 then
								'add_south
				let b2=maze_pos+16
				read b2,map_walls
				if w_done<>done and w_north=0 then
					let w_done=done
					let w_direc1=0
					let w_direc2=0
					write b2,map_walls
					poke list2,b2	 'add to list2
					inc list2	
				endif
			endif
			
			if w_east2 = 0 then
								'add_east
				let b2=maze_pos+1
				read b2,map_walls
				if w_done<>done and w_west=0 then
					let w_done=done
					let w_direc1=1
					let w_direc2=1
					write b2,map_walls
					poke list2,b2	 'add to list2
					inc list2	
				endif
			endif
			
			if w_west2 = 0 then
								'add_west
				let b2=maze_pos-1
				read b2,map_walls
				if w_done<>done and w_east=0 then
					let w_done=done
					let w_direc1=1
					let w_direc2=0
					write b2,map_walls 
					poke list2,b2	 'add to list2
					inc list2	
				endif
			endif
			
		loop until maze_pos = target
	
		poke list2,target		'terminate list 2
		if	list1<$C0 then	'Swap and reset the lists
			let list1=$C0
			let list2=$50
		 else
			let list1=$50
			let list2=$C0
		endif

		peek list1,maze_pos 'get next pos from list1
		
	loop until maze_pos=target
	
	if done=0 then
		let done=1		  'invert done 1=0,0=1
	else
		let done=0
	endif
	
	read pos,map_walls
	if w_done = done then goto maze_unsolvable
	
	'the maze is solved
	peek backup_b0,map_walls
	peek backup_b1,map_walls2
	switch off yellow_led
return



'''
done=4


def cleardone(done):
    global mazemap
    for i in range(256):
        mazemap[i] = (mazemap[i]&negDONE) + done


def solve():
    global done
    global list1
    global list2
    global mazemap
    global mazework
    list1 = [Target]   #'add maze center to list 1
    list2=[]           # empty list2
    # set DONE bit in target to done.
    mazemap[Target] = mazemap[Target]&negDONE + done
    while True:    # repeat until list2 is empty
        for i in range(len(list1)):
            pos = list1[i]
            if (mazemap[pos] & NORTH ==0 ):
                cand=pos-16
                if (cand>=0) and(mazemap[cand] & DONE) != done:
                    mazemap[cand] =  (mazemap[cand]&negDONE) + done # set it as done
                    mazework[cand] = DOWN      # downarrow
                    list2.append(cand)         # add to list2
                    #print (pos,cand,mazemap[cand],mazework[cand])
                
            if (mazemap[pos] & SOUTH ==0 ):
                cand=pos+16
                if (cand<=255) and(mazemap[cand] & DONE) != done:
                    mazemap[cand] =  (mazemap[cand]&negDONE) + done # set it as done
                    mazework[cand] = UP      # uparrow
                    list2.append(cand)         # add to list2
                    #print (pos,cand,mazemap[cand],mazework[cand])
                
            if (mazemap[pos] & WEST ==0 ):
                cand=pos-1
                if (cand>=0) and(mazemap[cand] & DONE) != done:
                    mazemap[cand] =  (mazemap[cand]&negDONE) + done # set it as done
                    mazework[cand] = RIGHT      # right arrow
                    list2.append(cand)         # add to list2
                    #print (pos,cand,mazemap[cand],mazework[cand])
                
            if (mazemap[pos] & EAST ==0 ):
                cand=pos+1
                if (cand<=255) and(mazemap[cand] & DONE) != done:
                    mazemap[cand] =  (mazemap[cand]&negDONE) + done # set it as done
                    mazework[cand] = LEFT      # left arrow
                    list2.append(cand)         # add to list2
                    #print (pos,cand,mazemap[cand],mazework[cand])

        #print(done,list1,list2)
        list1=list2
        list2=[]
        if list1== []:
            break
    if done==0:
        done=4
    else:
        done=0
#modify maze

fred = "240EUEUEUNRNSRNSRNSrnedewdewdws"
setp(fred)
fred2= "128nrnrnrnrnrnrnrnrnrnrnrnrnrnrnrn"            
setp(fred2)
printmaze(mazemap)
cleardone(0)
solve()
printmaze(mazemap)

