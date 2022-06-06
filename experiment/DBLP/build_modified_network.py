import random

# code adapted from __main__ code in pagerank_motif_direct to instead keep a set of all node ids in the graph
# network_file: network file path, e.g. 'data/DBLP/citation_network.txt'
def get_ids_and_copy(network_file, out_file):
    ids = set()
    f = open(network_file)
    o = open(out_file, 'w')
    edge_count = 0
    while True:
        line = f.readline()
        o.write(line)
        if line:
            edge_count += 1
            line = line.replace('\n', '')
            line = line.split(';')
            for i in range(len(line)):
                ids.add(int(line[i]))
        else:
            break
    return list(ids), edge_count
    
def append_extraneous_links(ids, edge_count, out_file, seed_val):
    n = len(ids)
    num_extra = int(0.01 * edge_count)
    id_counter = max(ids)
    out = open(out_file, 'a')
    random.seed(seed_val)
    for i in range(num_extra):
        id_counter += 1
        dst_ind = random.randint(0, n - 1) # choose a random node's index to point to
        # point new dummy citation to the random destination
        line = "%d;%d\n" % (id_counter, ids[dst_ind])
        out.write(line)
        
    
# given a network, fill a new network with extra links
def build_modified_network(network_file, out_file, seed_val):
    ids, edge_count = get_ids_and_copy(network_file, out_file)
    append_extraneous_links(ids, edge_count, out_file, seed_val)
    
if __name__ == "__main__":
    build_modified_network('data/DBLP/citation_network.txt', 'data/DBLP/citation_network_modified.txt', 42)
    
