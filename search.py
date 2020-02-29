import csv    

output = []

f = open( 'data.txt', 'r' ) #open the file in read universal mode
for line in f:
    cells = line.split( " " )
    output.append( ( cells[ 0 ], cells[ 1 ],cells[2],cells[3],cells[4],cells[5] ) ) #since we want the first, second column
print (output)

