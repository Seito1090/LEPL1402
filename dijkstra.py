import heapq

def dijkstra (trajets, durees,voyage):
    """

    :param:
    trajets: list of str like "BRU-PAR", all the possible roads 
    durees: list of int, all costs associated with the corresponding roads in trajets
    voyage: str like "BRU-PAR", the road we want to find the shortest path for

    :return:
    tuple: (trajet_min, duree_min), trajet_min shortest path for voyage, str "BRU-PAR-LUX", duree_min cost of trajet_min, int 

    """

    #set the start of our journey and its end 
    begin = voyage.split('-')[0]
    end = voyage.split('-')[1]

    #create a list with every node as well as a dictionary to keep track of the 
    # shortest paths stored as (node : "str" path)
    nodes = []
    pathkeeping = {begin : begin}
    for i in trajets :
        i = i.split("-")
        if i[0] not in nodes: 
            nodes.append(i[0])
        if i[1] not in nodes:
            nodes.append(i[1])

    #while we're at it we can check if we have the means to get to the end node
    #and that we did not fat finger the input
    if end not in nodes or begin not in nodes:
        return ("Pas de trajet possible", float("inf"))

    #create a list that will keep track of all the visited nodes such as 
    # visitedNodes[1] means nodes[1] was visited 
    visitedNodes = [False for node in nodes]

    #lastly we have to create a list that will keep track of the lowest 
    # cost to reach a node from the start node stored like costKeeping[2] 
    # refers to the cost to reach nodes[2] from the start node
    costKeeping = [float("inf") for node in nodes]

    #for the while look conditions, we can stop at the either if 
    # 1) the current node we are itterating on is the end node because it 
    # means we found the shortest path to where we wanted to go so no need to continue
    # 2) if the number of itterations exceeds the number of nodes, it means the graph 
    # is not connected

    currentNode = begin
    itteration = 0
    costKeeping[nodes.index(begin)] = 0
    visitedNodes[nodes.index(begin)] = True

    if begin == end:
        return pathkeeping[begin], costKeeping[nodes.index(begin)]

    while currentNode != end and itteration < len(nodes):
        itteration += 1
        currentCost = costKeeping[nodes.index(currentNode)]  #we get the current cost to reach the current node
        
        #in this loop we check all the possible roads from the current node and compare the cost 
        # to reach the new nodes (as in we add the road cost to currentCost) to update the 
        # costKeeping list accordingly
        
        for i in trajets:
            if i.split("-")[0] == currentNode:  
                node = i.split("-")[1]
                reachNode = nodes.index(node) #index of the node we can reach with the current road 
                reachCost = durees[trajets.index(i)] + currentCost
                if reachCost < costKeeping[reachNode]: #here we check if the cost to reach the node is less than what we had, if it is we update costKeeping and pathkeeping
                    costKeeping[reachNode] = reachCost
                    pathkeeping[node] = pathkeeping[currentNode] + "-" + node
            if i.split("-")[1] == currentNode: #same as above but for the other direction
                node = i.split("-")[0]
                reachNode = nodes.index(node)  
                reachCost = durees[trajets.index(i)] + currentCost
                if reachCost < costKeeping[reachNode]: 
                    costKeeping[reachNode] = reachCost
                    pathkeeping[node] = pathkeeping[currentNode] + "-" + node
        
        #we have an updated list of nodes and costs to reach them, we now have to chose the next node to visit
        # todo that we have to check the lowest costs in costKeeping and take the 1st node not visited yet
        
        orderedCosts = heapq.nsmallest(len(nodes), costKeeping)[visitedNodes.count(True)]   
        
        #with orderedCosts we get the lowest cost unvisited node but we still have to determine which node it is since 
        #multiple nodes can have the same "lowest"
        #first we get the index in costKeeping which will be the same as the index in nodes 

        indx = costKeeping.index(orderedCosts)

        #now we try to see if it is not a duplicate (another node with the same cost but which was visited)

        while visitedNodes[indx] == True:  #if it is we get the index of the next lowest cost node that is not visited
            indx = costKeeping.index(orderedCosts, indx+1, len(nodes))

        #now that we found it we can update the currentNode and visitedNodes
        currentNode = nodes[indx]
        visitedNodes[indx] = True
        if currentNode == end:
            return pathkeeping[end], costKeeping[nodes.index(end)]

    #if we did not visit the end node it means the graph is not connected
    if not visitedNodes[nodes.index(end)]:
        return ("Pas de trajet possible", float("inf"))
    

if __name__ == "__main__" :
    trajetsTest1 = [
         "BRU-PAR", "BRU-LUX", "BRU-COL", "BRU-AMS",\
         "PAR-LUX", "PAR-STR", "PAR-LYO", \
         "AMS-COL", "AMS-HAM", \
         "LUX-STR", "LUX-COL","LUX-FRA", \
         "STR-LYO", "STR-FRA","STR-MUN", \
         "LYO-MIL", \
         "HAM-BER","HAM-COL","HAM-FRA",\
         "COL-FRA","COL-BER", \
         "FRA-BER","FRA-MUN", \
         "BER-MUN","BER-PRA", \
         "MUN-PRA", \
         "PRA-VIE", \
         "VIE-MUN","VIE-BRA","VIE-ZAG","VIE-LIU","VIE-MIL", \
         "MUN-LIU","MUN-MIL", \
         "BRA-BUD", \
         "BUD-ZAG",\
         "LIU-MIL","LIU-ZAG"
            ]
    dureesTest1 = [1,3,3,2,3,3,2,4,5,3,4,5,4,2,5,5,2,4,4,1,5,4,4,5,5,6,4,4,2,6,7,11,7,9,2,5,7,2]
    trajetsTest2 = [
         "BRU-PAR", "BRU-LUX",\
         "PAR-LUX", "PAR-STR", "PAR-LYO", "PAR-BOR",\
         "LUX-STR",\
         "STR-LYO",\
         "LYO-BAR", "LYO-MAR",\
         "MAR-BOR", "MAR-BAR", \
         "BOR-BAR","BOR-MAD",\
         "MAD-POR", "MAD-LIS", "BAR-MAD",\
         "POR-LIS"
            ]
    dureesTest2 = [1,3,3,3,2,2,3,4,5,2,6,5,6,9,9,10,2,3]
    assert dijkstra(trajetsTest1, dureesTest1, "BRU-BUD") == ("BRU-COL-FRA-MUN-VIE-BRA-BUD", 16)
    assert dijkstra(trajetsTest1, dureesTest1, "BUD-BRU") == ("BUD-BRA-VIE-MUN-FRA-COL-BRU", 16)
    assert dijkstra(trajetsTest2, dureesTest2, "BRU-LIS") == ("BRU-PAR-LYO-BAR-MAD-LIS", 20)
    assert dijkstra(trajetsTest2, dureesTest2, "LIS-BRU") == ("LIS-MAD-BAR-LYO-PAR-BRU", 20)
    assert dijkstra(trajetsTest1, dureesTest1, "BRU-TKY") == ("Pas de trajet possible", float("inf"))
    assert dijkstra(trajetsTest1, dureesTest1, "TKY-BRU") == ("Pas de trajet possible", float("inf"))