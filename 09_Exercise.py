import requests
import networkx as nx
import numpy as np
r = requests.get("https://raw.githubusercontent.com/datsoftlyngby/dat4sem2020spring-python/master/twitter_combined.txt", allow_redirects=True)
open("twitter_combined.txt", 'wb').write(r.content)

#Which node in the twitter data has the most connections?
g = nx.read_edgelist('twitter_combined.txt')

#print('214328887' in g)

#print(g['214328887'])


#for neighbor in g.neighbors('214328887'):
#    print(neighbor)

in_deg_vec = np.array([g.degree(n) for n in g.nodes()])
max_ind_deg = in_deg_vec.max()
print(in_deg_vec)
print(np.argmax(in_deg_vec))

