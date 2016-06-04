#!usr/bin/env python
#coding=utf-8
import random
def graphc(content):
    filec = ""
    filec = filec + "graph [\n" + content + "\n]"
    return filec

def nodec(nodecontent,label):
    filec = ""
    filec = filec + "node \n[\nid " + str(nodecontent) + "\nlable " +'\"' + label + '\"' + "\n]\n"
    return filec

def edgec(source,target):
    filec = ""
    filec = filec + "edge \n[\nsource " + str(source) + "\ntarget " + str(target) + "\n]\n"
    return filec

def main():
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

    results = ""
    for i,ip in enumerate(iplist):
        results += nodec(i+1, ip)
    counts = i
    for _ in range(15):
        results += edgec(random.randint(1,counts), random.randint(1,counts))
    print graphc(results)

    f = open('wzj.gml','w')
    f.write(graphc(results))

if __name__ == "__main__":
    main()
