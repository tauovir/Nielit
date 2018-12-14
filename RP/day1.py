import gym

class Day1:
    def __init__(self):
        print("Initialised")
        self.env = gym.make("Taxi-v2")

    def firstFunc(self):
        print("Diffrent possible states :" + str(self.env.observation_space.n))
        print("Action List :" + str(self.env.action_space.n))


    def secondQa(self):
       # 0=> down,1=> up,2> right,3=> left,4=>pick-up,5=> drop-off
        print("========Second Question==========")
        #Blue color is passanger and passanger want to go purple color position
        self.env.reset()
        self.env.env.s = 254
        # Turn to right
        self.env.step(2)
        self.env.render()
        # Go down
        self.env.step(0)
        self.env.render()
        
        self.env.step(0)
        self.env.render()
        # Pickup passanger
        self.env.step(4)
        self.env.render()
        #========Now go to destination============
        #Go to up direction
        self.env.step(1)
        self.env.render()
        
        self.env.step(1)
        self.env.render()
        #Tern to left
        self.env.step(3)
        self.env.render()
        
        self.env.step(3)
        self.env.render()
        
        self.env.step(3)
        self.env.render()
        #Go down
        self.env.step(0)
        self.env.render()
        
        self.env.step(0)
        self.env.render()
        #Drop panssager
        self.env.step(5)
        self.env.render()
        
       
                
        
s1 = Day1()
s1.firstFunc()
s1.secondQa()

    

