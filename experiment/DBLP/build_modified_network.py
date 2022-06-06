# code adapted from __main__ code in pagerank_motif_direct to instead keep a set of all node ids in the graph
# network_file: network file path, e.g. 'data/DBLP/citation_network.txt'
def get_ids(network_file):
    ids = set()
    f = open(network_file)
    while True:
        line = f.readline()
        if line:
            line = line.replace('\n', '')
            line = line.split(';')
            for i in range(len(line)):
                ids.add(int(line[i]))
        else:
            break
            
    return list(ids)
    
if __name__ == "__main__":
    print(get_ids('data/DBLP/citation_network.txt'))
