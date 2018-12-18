import gym
import numpy as np

class Day2:
    def __init__(self):
        print("Welcome to Reinforcement Learning")
        #self.env = gym.make("Taxi-v2") #This is for randomMove and qMatrix
        #self.env = gym.make("CartPole-v0")  # This is for onepAigym
        #self.env = gym.make("Acrobot-v1")  # This is for onepAigym
        self.env = gym.make("MountainCarContinuous-v0")  # This is for onepAigym
        self.state = self.env.reset()
        self.env.render()

    def randomMove(self):
        print("*************")
        cnt = 1;
        reword = 0
        while reword != 20:
            action = self.env.action_space.sample()
            state,reword,done,info = self.env.step(action)
            self.env.render()
            cnt = cnt + 1
        print ("Needed:",cnt,"move to reach to final state")

    def qMatrix(self):
        Q = np.zeros([500,6]);
        gamma = .801;
        for episode in range(1,1000) :
            state = self.env.reset();
            self.env.render()
            cnt = 1;
            reward = 0;
            while reward != 20:
                    action = np.argmax(Q[state]);
                    state2, reward,done,info = self.env.step(action);
                    Q[state,action] = reward + gamma * np.max(Q[state2]);
                    state = state2;
                    cnt = cnt + 1;
            print("Needed " + str(cnt) + " moves to reach the final state during episode " + str(episode));
        
        
    def onepAigym(self):
        print("*************")
        cnt = 1;
        reword = 0
        while reword != 20:
            action = self.env.action_space.sample()
            state,reword,done,info = self.env.step(action)
            self.env.render()
            cnt = cnt + 1
        print ("Needed:",cnt,"move to reach to final state")
            

        


s1 = Day2()
#s1.randomMove()
#s1.qMatrix()
s1.onepAigym()
