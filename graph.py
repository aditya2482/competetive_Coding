class graphx:
    global graph_represeneted_dictionary 
    def __init__(self,edges):
        self.edges = edges
        self.graph_represeneted_dictionary = {}
        for start,end in edges:
            if start in self.graph_represeneted_dictionary:
                # print(type(start),type(end))
                self.graph_represeneted_dictionary[start].append(end)  # otherwise append it in list of particular key
            else:
                self.graph_represeneted_dictionary[start] = [end] # if a state is encountered first time - append as it is in dict
        # print(self.graph_represeneted_dictionary)

    
    def get_path(self,start,end,path = []):
        path = path + [start] # path will contain starting point

        if start ==  end:
            return path

        if start not in self.graph_represeneted_dictionary:
            return []     
        
        paths = []
        for node in self.graph_represeneted_dictionary[start]:
            if node not in path:
                new_path = self.get_path(node,end,path) 
                for p in new_path:
                    paths.append(p)
        
        return paths
        
       



# runtime - O(n)
# driver program
if __name__ == "__main__":
    # routes defined as the edges bettween the nodes
    #states are the individual nodes
    flight_routes = [

        ("delhi","jaipur"),
        ("delhi","chittor"),
        ("delhi","luckhnow"),
        ("chittor","bihar"),
        ("bihar","jharkhand"),
        ("jaipur","bihar"),
        ("lukhnow","jharkhand"),

    ]

    graph_ = graphx(flight_routes)
    print(graph_.get_path("delhi","bihar"))
