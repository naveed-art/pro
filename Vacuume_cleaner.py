class Agent:
    def __init__(self,room):
        print("Before: All rooms are durt\n")
        print(room)
    def check_(self,z):
        x = 0
        y = 0
        while x < 4:
            while y < 4:
                if room[x][y]==1:
                    print("Dirt founf on that location", x,y)
                    room[x][y] =0
                    print("cleaned",x,y)
                    z+=1
                y+=1
            x+=1
            y = 0
        print("TotAL moves is:",z)
room = [[0,1,1,1],
        [1,0,1,1],
        [1,1,0,1],
        [0,1,1,1]]
agent = Agent(room)
agent.check_(0)