import networkx as nx
import matplotlib.pyplot as plt
import random
G = nx.Graph()
iplist = ["1.52.27.1",
    "1.52.34.180",
    "1.52.40.250",
    "1.52.127.255",
    "1.52.182.32",
    "1.52.237.199",
    "1.54.45.113",
    "1.54.208.113",
    "1.55.70.23",
    "1.55.228.76",
    "1.59.142.32",
    "1.161.124.51",
    "1.231.159.77",
    "2.50.135.182",
    "2.104.132.203",
    "2.132.160.207",
    "2.133.231.81",
    "2.229.50.183",
    "5.8.37.205",
    "5.8.37.212",
    "5.8.37.213",
    "5.8.37.214",
    "5.8.37.220",
    "5.8.37.223",
    "5.8.37.224",
    "5.8.37.230"]

# for i,ip in enumerate(iplist):
#     G.add_node(i,name=ip)
for i in iplist:
    G.add_node(i)
counts = len(iplist)
edgecounts = random.randint(0,counts)
for i in range(edgecounts):
    G.add_edge(iplist[random.randint(0,counts-1)],iplist[random.randint(0,counts-1)])

nx.draw_networkx(G,pos=nx.random_layout(G),node_size=100,node_color='b')
plt.show()