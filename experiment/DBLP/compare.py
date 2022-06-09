from pagerank_motif_direct import *
import time

# code adapted from motif_construct_direct to find the adjacency matrix without computing a motif (i.e. for vanilla pagerank)
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

# see obtain_pageranks.write_mpr_output for documentation on these instructions
def compute_pagerank(adjacency_matrix, alpha):
    M = graphMove_new(adjacency_matrix)
    pr = firstPr(M)
    p = 1 - alpha
    v = pageRank(p, M, pr)
    return v

# pagerank_vals contains the original pagerank values for original citation_network.txt
# networks_list is a list of indices from 0 to 29 choosing which modified citation networks to use
# motif is 'M1' or ... 'M7'
# alpha in 0 to 1
# out_file will have the errors
def compare(pagerank_vals, networks_list, motif, alpha, out_file):
    start = time.time()

    f = open(out_file, 'w')
    MPR_adj, MPR_id = construct_motif('data/DBLP/citation_network.txt', 1, motif, alpha)
    MPR = compute_pagerank(MPR_adj, alpha)
    for i in networks_list:
        PR_new_adj, PR_new_id = get_adjacency_matrix("data/DBLP/citation_network_modified_%d.txt" % (i))
        MPR_new_adj, MPR_new_id = construct_motif("data/DBLP/citation_network_modified_%d.txt" % (i), 1, motif, alpha)
    
        PR_new = compute_pagerank(PR_new_adj, alpha)
        MPR_new = compute_pagerank(MPR_new_adj, alpha)
    
        error_PR = np.sum(np.absolute(PR - PR_new[:len(PR)]))
        error_MPR = np.sum(np.absolute(MPR - MPR_new[:len(MPR)]))
    
        f.write("%f;%f\n" % (error_PR, error_MPR))
        print("---compare has taken %f seconds" % (time.time() - start))

if __name__ == '__main__':
    start = time.time()
    #alpha = 0.15
    #PR_adj, PR_id = get_adjacency_matrix('data/DBLP/citation_network.txt')
    #PR = compute_pagerank(PR_adj, alpha)
    
    # compute MPR with motif 1 on 5 of the modified networks
    #motif = 'M1'
    #compare(PR, range(5), motif, alpha, "output/DBLP/%s_errors.txt" % (motif))
    #print("main has taken %f seconds" %(time.time() - start))
    
    # compute MPR with motif 4 on a different 5 modified networks
    #motif = 'M4'
    #compare(PR, range(5, 10), motif, alpha, "output/DBLP/%s_errors.txt" % (motif))
    #print("main has taken %f seconds" %(time.time() - start))
    
    # compute MPR with motif 7 on a different 5 modified networks
    #motif = 'M7'
    #compare(PR, range(10, 15), motif, alpha, "output/DBLP/%s_errors.txt" % (motif))
    #print("main has taken %f seconds" %(time.time() - start))
    
    motif = 'M7'
    alpha = 0.1
    PR_adj, PR_id = get_adjacency_matrix('data/DBLP/citation_network.txt')
    PR = compute_pagerank(PR_adj, alpha)
    compare(PR, range(5), motif, alpha, "output/DBLP/%s_alpha%s_errors.txt" % (motif,alpha))
    print("main has taken %f seconds" %(time.time() - start))
    
    alpha = 0.3
    PR_adj, PR_id = get_adjacency_matrix('data/DBLP/citation_network.txt')
    PR = compute_pagerank(PR_adj, alpha)
    compare(PR, range(5, 10), motif, alpha, "output/DBLP/%s_alpha%s_errors.txt" % (motif,alpha))
    print("main has taken %f seconds" %(time.time() - start))
    
    alpha = 0.5
    PR_adj, PR_id = get_adjacency_matrix('data/DBLP/citation_network.txt')
    PR = compute_pagerank(PR_adj, alpha)
    compare(PR, range(10,15), motif, alpha, "output/DBLP/%s_alpha%s_errors.txt" % (motif,alpha))
    print("main has taken %f seconds" %(time.time() - start))
