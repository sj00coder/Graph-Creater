import math
import matplotlib.pyplot as plt

size = 50
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)

#construct function
def constructGraph(vertex,edges):
    x=[]
    y=[]
    joinx=[]
    joiny=[]
    
    for i in range(vertex):
        
        x.append(2 + round(1.5* math.sin((2*math.pi*i)/vertex),2))
        y.append(2 + round(1.5* math.cos((2*math.pi*i)/vertex),2))

    plt.scatter(x, y)
    
    for i in range(vertex):
        plt.annotate(
            "P"+str(i),
            xy=(x[i] , y[i]), xycoords='data',
            xytext=(15, 25), textcoords='offset points',
            )
    print(edges)
    for i in edges:
        k = int(i[0]) 
        l = int(i[1])
        if( k >= len(x) or l >= len(x) ):
            print("please enter valid input")
            return
        joinx.append(x[k])
        joinx.append(x[l])
        joiny.append(y[k])
        joiny.append(y[l])

        plt.plot(joinx,joiny ,color = "orange")
        joinx.clear()
        joiny.clear()

    # plt.savefig("out.png")

    plt.axis([int(min(x)-2), int(max(x)+2),int(min(y)-2),int(max(y)+2)])
    fig.savefig('test2png.png', dpi=100)
    plt.show()

# function to convert adjacenty list to pair list 
def edgeConverter(adj):
    edges = []
    for i in adj.keys():
        for j in adj[i]:
            edges.append((i,j))
    
    return edges

#function of converting adjacent matrix into edges
def MatrixToedge(n,matrix):
    edges= []
    for i in range(n):
        for j in range(n):
            if(matrix[i][j] == 1):
                edges.append((i,j))
    
    return edges
# driver functiions
edges=[]
vertex= int(input("Enter no of vertex  "))
mode=int(input("Enter the mode of graph representation \n For direct pair method press 0  \n For adjaceny list press 1\n For adjaceny Matrix press 2\n"))

if( mode == 0):
    NoEdge =int(input("Enter no of edges:  "))
    for i in range(NoEdge):
        print("Enter the point to join:  ")
        k, l = input().split()
        edges.append((k,l))
    
    constructGraph(vertex,edges)


elif( mode == 1):
    adj = dict()
    for i in range(vertex):
        print(f"Enter the point to join to {i}:  ")
        a = list(map(int,input().strip().split())) 
        adj[i] = a
    
    edges = edgeConverter(adj)
    constructGraph(vertex,edges)

elif(mode == 2):
    matrix= []
    # NoEdge =int(input("Enter no of edges:  "))
    for i in range(vertex):
        print(f"Enter the matrix row for  {i} of {vertex} numbers:  ")
        a = list(map(int,input().strip().split()))
        if(len(a) != vertex):
            print("Enter valid input")
            break
            
        else:
            matrix.append(a)
    
    if(len(matrix) != vertex):
        print("please enter valid input")
        
    else:

        edges=MatrixToedge(vertex,matrix)
        constructGraph(vertex,edges)

else:
    print ("Enter a valid input")

