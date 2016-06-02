# coding=utf-8
import networkx as nx
import matplotlib.pyplot as plt
import random
import dns.resolver
G = nx.Graph()


def main():
    iplist = {}
    while 1:
        domain = raw_input('Please input an domain: ')  # 输入域名地址
        if not domain:
            break
        try:
            A = dns.resolver.query(domain, 'A')
        except Exception, e:
            print e
            continue  # 指定查询类型为A记录
        for i in A.response.answer:  # 通过response.answer方法获取查询回应信息
            for j in i.items:
                addressc = str(j.address)
                iplist[addressc] = domain
    print iplist

    domainset = []
    for i, j in iplist.items():
        G.add_node(i)
        G.add_node(j)
        G.add_edge(i, j)
        domainset.append(j)

    domainset= list(set(domainset))
    lens = 20
    for i in domainset:
        if len(i) < lens:
            lens = len(i)
            mark = i
        else:
            pass
    
    for i in domainset:
        if mark != i:
            G.add_edge(mark,i)


    nx.draw_networkx(G, node_size=100,node_color='b')

    plt.show()


if __name__ == "__main__":
    main()
