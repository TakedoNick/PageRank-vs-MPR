from pagerank_motif_direct import *

# code adapted from motif_construct_direct to find the adjacency matrix without computing a motif
def get_adjacency_matrix(network_file):
    # read the network file to find sources and destinations for edges
    # entry will be a list of tuples [src id, dst id]
    entry = []
    f = open(network_file)
    while True:
        line = f.readline()
        if line:
            temp = []
            line = line.replace('\n', '')
            line = line.split(';')
            for i in range(len(line)):
                temp.append(int(line[i]))
            entry.append(temp)
        else:
            break
            
    # create the sparse adjacency matrix using the edge data
    sparse_array_row = []
    sparse_array_col = []
    sparse_array_data = []
    entry_all = [] # to keep track of corresponding IDs
    for i in range(len(entry)):
        sparse_array_row.append(entry[i][0])
        sparse_array_col.append(entry[i][1])
        sparse_array_data.append(1)
        entry_all.append(entry[i][0])
        entry_all.append(entry[i][1])
    entry_unique = np.unique(entry_all)
    newsparse_array_row = []
    newsparse_array_col = []
    counttt = 0
    for nnn in range(len(sparse_array_row)):
        if counttt % 300000 == 0:
            print('echo is %d' % counttt)
        counttt += 1
        id1 = sparse_array_row[nnn]
        id2 = sparse_array_col[nnn]
        id1new = np.where(entry_unique == id1)[0][0]
        id2new = np.where(entry_unique == id2)[0][0]
        newsparse_array_row.append(id1new)
        newsparse_array_col.append(id2new)
    maxnum = len(entry_unique)
    adjacency_matrix = csr_matrix((sparse_array_data, (newsparse_array_row, newsparse_array_col)), shape=(maxnum, maxnum), dtype = np.float64)
    return adjacency_matrix, entry_unique

def compute_pagerank(adjacency_matrix, alpha):
    M = graphMove_new(adjacency_matrix)
    pr = firstPr(M)
    p = 1 - alpha
    v = pageRank(p, M, pr)
    return v

if __name__ == '__main__':
    PR_adj, PR_id = get_adjacency_matrix('data/DBLP/citation_network.txt')
    PR_0_adj, PR_0_id = get_adjacency_matrix('data/DBLP/citation_network_modified_0.txt')
    MPR_adj, MPR_id = construct_motif('data/DBLP/citation_network.txt', 1, 'M6', 0.4)
    MPR_0_adj, MPR_0_id = construct_motif('data/DBLP/citation_network_modified_0.txt', 1, 'M6', 0.4)
    
    print(array_equal(PR_id, MPR_id))
    print(array_equal(PR_0_id, MPR_0_id))
    
    PR = compute_pagerank(PR_adj, 0.4)
    PR_0 = compute_pagerank(PR_0_adj, 0.4)
    MPR = compute_pagerank(MPR_adj, 0.4)
    MPR_0 = compute_pagerank(MPR_0_adj, 0.4)
    
    
    error_PR = np.sum(np.absolute(PR - PR_0[:len(PR)]))
    error_MPR = np.sum(np.absolute(MPR - MPR_0[:len(MPR)]))
    
    print(error_PR)
    print(error_MPR)
    
