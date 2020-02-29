import csv   

class node:##node
    path=[]
    classes=[]
    goalb=[]
    goalc=[]
    unit=0
    output = []
    f= open( 'data.txt', 'r' ) #open the file in read univ ersal mode
    for line in f:
        cells = line.split( " " )
        output.append( ( cells[ 0 ], cells[ 1 ],cells[2],cells[3],cells[4],cells[5] ) ) #since we want the first, second column

        Course=None

    def expand(self):
        parent = self
        explored.append(parent)
        for course,unit,pre1,pre2,pre3,pre4 in parent.output:
            if (pre1 or pre2 or pre3 or pre4 == parent.Course):
                parent.classes.append(course)
                
        for x in parent.classes:
            child=node()
            child.path=parent.path
            child.path.append(parent.Course)
            child.classes=parent.classes
            child.Course=x
            child.unit=parent.unit+4
            if(False == (explored.__contains__(child))):
               frontier.append(child)
            print(child.Course)
            #print(child.path)
            
    

            



explored = []

frontier=[]
def sort(self):
    #Brendan will deal with this
    Placeholder=89

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
while True:
    frontier.pop().expand()
    frontier.sort(key="node.unit") 
    
    
    