def GenerateGraphs(size, base):
    dic=GenerateDic()
    for i in range(1,5):  
        for j in range(10):              
            G=AddEdges(nx.dense_gnm_random_graph(size,int(size*size*0.03 ))) 
            nodes=RandNodes(size-1)          
            for k in range (5):               
                edmond=[]
                din=[]
                boyk=[]
                for l in range(5):
                    edmond.append(Edmond(G,nodes[l][0],nodes[l][1]))
                    din.append(Din(G,nodes[l][0],nodes[l][1]))
                    boyk.append(Boyk(G,nodes[l][0],nodes[l][1]))
                Asign(dic, "dense","Edmond", G.number_of_nodes(),G.number_of_edges(),nodes[k],np.median(edmond),np.mean(edmond),np.std(edmond),np.var(edmond),nx.density(G))   
                Asign(dic, "dense","Dinitz", G.number_of_nodes(), G.number_of_edges(),nodes[k],np.median(din),np.mean(din),np.std(din),np.var(din),nx.density(G))   
                Asign(dic, "dense","Boyk", G.number_of_nodes(), G.number_of_edges(),nodes[k],np.median(boyk),np.mean(boyk),np.std(boyk), np.var(boyk),nx.density(G)) 
            G=AddEdges(nx.erdos_renyi_graph(size, 0.1))
            for k in range (5):
                edmond=[]
                din=[]
                boyk=[]
                for l in range(5):
                    edmond.append(Edmond(G,nodes[l][0],nodes[l][1]))
                    din.append(Din(G,nodes[l][0],nodes[l][1]))
                    boyk.append(Boyk(G,nodes[l][0],nodes[l][1]))
                Asign(dic, "erdos","Edmond", G.number_of_nodes(), G.number_of_edges(),nodes[k],np.median(edmond),np.mean(edmond),np.std(edmond),np.var(edmond),nx.density(G))   
                Asign(dic, "erdos","Dinitz", G.number_of_nodes(),  G.number_of_edges(),nodes[k],np.median(din),np.mean(din),np.std(din),np.var(din),nx.density(G))   
                Asign(dic, "erdos","Boyk", G.number_of_nodes(),  G.number_of_edges(),nodes[k],np.median(boyk),np.mean(boyk),np.std(boyk),np.var(boyk),nx.density(G))   
            G=AddEdges(AddEdges(nx.random_tree(size)))
            for k in range (5):
                edmond=[]
                din=[]
                boyk=[]
                for l in range(5):
                    edmond.append(Edmond(G,nodes[l][0],nodes[l][1]))
                    din.append(Din(G,nodes[l][0],nodes[l][1]))
                    boyk.append(Boyk(G,nodes[l][0],nodes[l][1]))
                Asign(dic, "tree","Edmond", G.number_of_nodes(), G.number_of_edges(),nodes[k],np.median(edmond),np.mean(edmond),np.std(edmond),np.var(edmond),nx.density(G))   
                Asign(dic, "tree","Dinitz", G.number_of_nodes(), G.number_of_edges(),nodes[k],np.median(din),np.mean(din),np.std(din),np.var(din),nx.density(G))   
                Asign(dic, "tree","Boyk", G.number_of_nodes(), G.number_of_edges(),nodes[k],np.median(boyk),np.mean(boyk),np.std(boyk),np.var(boyk),nx.density(G))                                        
        size*=base;
    df=pd.DataFrame(dic)
    df.to_csv("matrix.csv") 