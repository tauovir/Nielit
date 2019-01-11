import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def annotFun():
    framObj = plt.figure(figsize = (6,6),facecolor=(1,0,1))
    framObj.canvas.set_window_title("Annot Function")
    subObj = framObj.add_subplot(111)
    x = np.arange(1,2001,2)
    y = np.random.randint(1,1000,5)
    print(x)
    print(y)
    y.sort()
    for x,y in zip(x,y):
        subObj.annotate('(' + str(x) + ',' + str(y) + ')',xy = (x,y))
        #subObj.annotate("Khan Example",xy = (4,75))
        subObj.plot(x, y,'ro:')
    plt.show()

def scatterGraph():
    framObj = plt.figure(figsize=(6,6),facecolor=(1,0,1))
    framObj.canvas.set_window_title("Scatter Graph")
    subObj = framObj.add_subplot(111)
    y = np.random.randint(1,100,10)
    x = np.arange(1,21,2)
    subObj.scatter(x, y,color = 'y',marker='*', edgecolor = 'r',s = 100)
    plt.show()

def barGraph():
    framObj = plt.figure(figsize=(6,6),facecolor=(1,0,1))
    framObj.canvas.set_window_title("Scatter Graph")
    subObj = framObj.add_subplot(111)
    xLabel = ['Khan','Taukir','Banana','Ganga','Mango']
    xVal = np.arange(len(xLabel))
    studentScore = [60,80,70,50,86]
    print(xVal)
    subObj.bar(xVal,studentScore)
    subObj.set_xticks(xVal)
    subObj.set_xticklabels(xLabel)
   # subObj.set_yticks(xVal)
    #subObj.set_yticklabels(studentScore)
    subObj.set_ylabel("Marks")
    subObj.set_xlabel("Candidates")
    subObj.set_title('Performance Chart')
    subObj.margins(0.05)

    plt.show()
def barGraph2():
    framObj = plt.figure(figsize=(6,6),facecolor=(1,0,1))
    spobj=framObj.add_subplot(1,1,1)
    stud_name_xticks='Ram Tom Raj Ravi Roy Anil'.split()
    x_val=np.arange(len(stud_name_xticks))
    #x_val=np.linspace(0,200,len(stud_name_xticks))
    barwidth=0.3
    stud_scores_m=[90,30,60,50,25,80]
    stud_scores_s=[60,70,50,50,35,70]
    spobj.bar(x_val,stud_scores_m,width=barwidth,alpha=0.5,color='b',label='maths')
    spobj.bar(x_val+barwidth,stud_scores_s,width=barwidth,alpha=0.5,color='r',label='science')
    #plt.xticks(x_val,stud_name_xticks)
    spobj.set_xticks(x_val+barwidth)
    spobj.set_xticklabels(stud_name_xticks)
    spobj.set_xlabel('Candidates')
    spobj.set_title('Assessment chart')
    spobj.legend(loc='center')
    plt.show()

#annotFun()
#scatterGraph()
#barGraph()
barGraph2()