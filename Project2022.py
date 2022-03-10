import random
from operator import itemgetter
import math
from collections import defaultdict

class solForGraph:
    def __init__(self, v):
        self.g=[]
        self.result=[]
        self.vertex=v
        self.comp=[]
        self.yet=[]

    def appendEdge(self, startv,vertices,weight):
        self.g.append([startv,vertices,weight])

    def spot(self, lst,a):
        if(lst[a]==a):
            return a
        return self.spot(lst, lst[a])

    def unionimplement(self, lst,rr,a,b):
        yR=self.spot(lst,b)
        xR=self.spot(lst,a)

        if (rr[xR]>rr[yR]):
            lst[yR]=xR
        elif (rr[xR]<rr[yR]):
            lst[xR]=yR
        else:
            lst[yR]=xR
            rr[xR]+=1

    def Algkruskal(self,inp=20):
        for k in range(inp+1):
            random.shuffle(self.g)
            k=0
            countt=0
            lst, rr = [],[]
            self.g = sorted(self.g,key=lambda item:item[2])

            for nn in range(self.vertex):
                lst.append(nn)
                rr.append(0)

            self.comp.clear()

            while countt<self.vertex-1:
                startv, vertices, weight = self.g[k]
                k=k + 1
                a=self.spot(lst, startv)
                b=self.spot(lst, vertices)

                if(b != a):
                    countt = countt + 1
                    self.result.append([startv, vertices, weight])
                    self.comp.append([startv,vertices,weight])
                    self.unionimplement(lst, rr, a, b)

            self.comp = sorted(self.comp)
            self.result=sorted(self.result)
            if self.comp not in self.yet:
                self.yet.append(self.comp)
            self.yet=sorted(self.yet)

            if self.result in self.yet:
                for i in range(len(self.result)-1):
                    if self.result[i:i+1]==self.comp[i:i+1]:
                        Cost = 0
                        print("For this algortihm (Kruskal), we get these edges:")
                        for startv, vertices, weightt in self.result:
                            print("%d <---> %d" % (startv, vertices))
                            Cost = Cost + weightt
                        print("The Cost of Minimum Spanning Tree: ", Cost)
                        print(self.g)
                        print("                    ")
                        print(self.result)
                        print("                    ")
                        self.result.clear()
                    else:
                        self.result.clear()


res = solForGraph(4)
res.appendEdge(0,2,1)
res.appendEdge(0,3,1)
res.appendEdge(1,3,1)
res.appendEdge(1,2,1)
res.appendEdge(2,3,1)
res.Algkruskal()


