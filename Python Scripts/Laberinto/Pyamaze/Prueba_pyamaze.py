from pyamaze import maze, COLOR, agent

m=maze()
m.CreateMaze()
m.run()

m=maze(5,5)
m.CreateMaze()
m.run()

m=maze(10,10)
m.CreateMaze(theme=COLOR.light)
a=agent(m)
m.run()

m=maze(5,5)
m.CreateMaze()
a=agent(m, shape='arrow', footprints=True)
a.position=(5,4)
a.position=(5,3)
a.position=(5,2)
m.run()

m=maze(25,25)
m.CreateMaze(loopPercent=50)
a=agent(m,filled=True,footprints=True)
m.tracePath({a:m.path})
m.run()