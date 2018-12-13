import matplotlib.pyplot as plt
import numpy as np

class Day29:
    def __init__(self):
        print('Initialised')
        #self.fob = plt.figure(figsize = (6,6), facecolor = '#00FF00')
        self.fob = plt.figure(figsize = (8,8), facecolor = '#00FF00')

    def annotaeFunc(self):
        
        spoj = self.fob.add_subplot(1,1,1)
        yn = np.random.randint(1,100,10)
        xn = np.arange(2,21,2)
        print(yn)
        print("==========")
        print(xn)
        #Now Plot graph
        yn.sort()
        for x,y in zip(xn, yn):
            spoj.annotate('(' + str(x) + ',' + str(y) + ')',xy = (x,y))
            #spoj.annotate('(' + str(x) + ',' + str(y) + ')',xy = (x,y))
        spoj.annotate("Khan Example",xy = (4,75))
        spoj.plot(xn, yn,'ro:')
        plt.show()

    def scatterGraph(self):
        spoj = self.fob.add_subplot(1,1,1)
        yn = np.random.randint(1,1000,100)
        xn = np.arange(2,401,4)
        spoj.scatter(xn, yn, color = 'y',marker = '$k$',edgecolors = 'r')
        plt.show()
        
    def scatterSize(self):
        spoj = self.fob.add_subplot(1,1,1)
        yn = np.random.randint(1,100,10)
        xn = np.arange(2,21,2)
        spoj.scatter(xn, yn, color = 'y',marker = 'v', edgecolors = 'r',s=100)
        plt.show()

    def barGraph(self):
        spoj = self.fob.add_subplot(1,1,1)
        studNameXticks = 'Khan Ram Rahul Ganga Mango kalka'.split()
        x_val=np.arange(len(studNameXticks))
        stuScore = [90,30,60,50,25,80]
        print x_val
        spoj.bar(x_val, stuScore,align='center',width=0.3,alpha=0.5,color='r')
        spoj.set_xticks(x_val)
        spoj.set_xticklabels(studNameXticks)
        spoj.set_yticks(x_val)
        spoj.set_yticklabels(studNameXticks)
        spoj.set_ylabel('Candidates')
        spoj.set_title('Assessment chart')
        spoj.margins(0.05)
        plt.show()

    def barGraph2(self):
        spobj=self.fob.add_subplot(1,1,1)
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

    def barGraph3(self):
        spobj=self.fob.add_subplot(1,1,1)
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

    def stemGraph(self):
        spobj=self.fob.add_subplot(1,1,1)
        stud_name_xticks='Ram Tom Raj Ravi Roy Anil'.split()
        xVal = np.arange(len(stud_name_xticks))
        studScore = [50,90,60,70,41,20]
        spobj.stem(studScore)
        spobj.set_xticks(xVal)
        spobj.set_xticklabels(stud_name_xticks)
        plt.show()


    def pieGraph(self):
        spobj=self.fob.add_subplot(2,1,1)
        fruits='Apple Orange Grapes Mango Pineapple'.split()
        sales=[30,40,25,10,35]
        colrs='r y c g b'.split()
        spobj.pie(sales,colors=colrs)
        plt.show()


    def day29Qa(self):
        mpplt=self.fob.add_subplot(3,3,1)
        rajplt=self.fob.add_subplot(3,3,3)
        chplt=self.fob.add_subplot(3,3,4)
        telPlt=self.fob.add_subplot(3,3,4)
        mijPlt=self.fob.add_subplot(3,3,5)
        
        mp = [('inc',114),('bjp',15),('independent',4),('other',2)]
        
        rajVal = [99,73,3,14]
        rajName = ['INC','BJP','Independet','other']

        chVal = [68,15,9,7]
        chName = ['INC','BJP','Independet','other']

        telVal = [88,19,1,11]
        telName = ['TRS','INC','BJP','Others']

        mejVal = [26,5,1,8]
        mejName = ['MNF','INC','BJP','Others']
        
        val = []
        name = []
        for x1,y1 in mp:
            val.append(y1)
            name.append(x1)
        
        patches,texts=mpplt.pie(val,labels = name,shadow=True,startangle=45)
        
        rajplt.pie(rajVal,labels = rajName,shadow=True,startangle=45)
        
        chplt.pie(chVal,labels = chName,shadow=True,startangle=45)

        telPlt.pie(telVal,labels = telName,shadow=True,startangle=45)

        mijPlt.pie(mejVal,labels = mejName,shadow=True,startangle=45)
       
       
        #plt.legend(patches,name,loc='best')
        plt.show()


    def qaBarChart(self):
        spobj=self.fob.add_subplot(1,1,1)
        months = ['jan','fab','mar','apr','may','june','jul','aug','sep','oct','nov','dec']
        high1 = [32,32,33,32,30,30,30,30,30,31,31,14]
        low = [23,23,24,25,24,24,24,24,23,23,23,25]
        x_val=np.arange(len(months))
        barwidth=0.3
        print(len(low))
        
        spobj.bar(x_val,high1,width=barwidth,alpha=0.5,color='b',label='maths')
        spobj.bar(x_val+barwidth,low,width=barwidth,alpha=0.5,color='r',label='science')
        plt.xticks(x_val,months)
        spobj.set_xticks(x_val+barwidth)
        spobj.set_xticklabels(months)
        spobj.set_xlabel('Graph')
        spobj.set_title('Assessment chart')
       #spobj.legend(loc='center')
        plt.show()
        
    
    


s1 = Day29()
#s1.annotaeFunc()
#s1.scatterGraph()
#s1.scatterSize()
#s1.barGraph()
#s1.barGraph2()
#s1.barGraph3()
#s1.stemGraph()
#s1.pieGraph()
#s1.day29Qa()
s1.qaBarChart()


