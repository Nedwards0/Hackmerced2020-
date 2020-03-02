import csv 
import time


class node:##node
    path=[]
    classes=[]
    goalb=[]
    goalc=[]
    unit=0
    output = []
    childpath=[]
  
    f= open( 'data.txt', 'r' ) #open the file in read univ ersal mode
    for line in f:
        cells = line.split( " " )
        output.append( ( cells[ 0 ], cells[ 1 ],cells[2],cells[3],cells[4],cells[5] ) ) #since we want the first, second column

        Course=None

    def expand(self):
        
        explored.append(self)
        for course,unit,pre1,pre2,pre3,pre4 in self.output:
            if (pre1 or pre2 or pre3 or pre4 == self.Course):
                self.classes.append(course)
        
        for x in self.classes:
            
            child=node()
            
            
            child.classes=self.classes
            
            
            child.Course=x
            child.childpath=(child.Course)
            child.childpath=(self.path)
            child.childpath.append(child.Course)
            print(child.childpath)
            

           
            
            
            child.unit=self.unit+4
            if(False == (explored.__contains__(child))):
               frontier.append(child)
            
               
            
           
            time.sleep(4)
           


  



explored = []

frontier=[]

output = []


f = open( 'data.txt', 'r' ) #open the file in read universal mode
for line in f:
    cells = line.split( " " )
    output.append( ( cells[ 0 ], cells[ 1 ],cells[2],cells[3],cells[4],cells[5] ) ) #since we want the first, second column


c=node() 

for course,unit,pre1,pre2,pre3,pre4 in output:
    if pre1 == "0":
        c.classes.append(course)

c.Course="CSE20"
c.unit=4
frontier.append(c)
c.path.append(c.Course)
while True:
    frontier.pop(0).expand()
    
    
    
    