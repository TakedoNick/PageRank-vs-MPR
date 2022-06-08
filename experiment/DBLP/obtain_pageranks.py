from pagerank_motif_direct import *
from result_read import *
from compare import *
import time

# same as the __main__ code in pagerank_motif_direct but more general
# network_file: network file path, e.g. 'data/DBLP/citation_network.txt'
# motif: 'M1' or 'M2' or ... or 'M7'
# alpha: probability of restart, so float in 0 to 1
# out_file: should be 'output/DBLP/<desired file name>' e.g. 'output/DBLP/result_citation_M6_alpha0.4.txt'
# time_log will record the time taken to build the motif
def write_mpr_output(network_file, motif, alpha, out_file, time_file):

    # construct the adjacency matrix for MPR and record the time taken
    time_log = open(time_file, 'a')
    start = time.time()
    a, entry_unique = construct_motif(network_file, 1, motif, alpha)
    time_log.write("%s;%f\n" % (motif, time.time() - start))
    
    # get the transition matrix from the adjacency matrix
    M = graphMove_new(a)
    
    # get an initial vector estimate of the values
    pr = firstPr(M)
    
    # set our normal transition probability to 1 minus probability of random surf
    p = 1 - alpha
    
    # calculate pagerank values through power iteration
    v = pageRank(p, M, pr)
    
    # write results to a file
    output = open(out_file, 'w')
    for i in range(len(v)):
        a = "%lf %d\n" % (v[i], entry_unique[i])
        output.write(a)
    output.close()

# same as the __main__ code in result_read but more general
# out_file: use the same out_file as in write_mpr_output
def format_output(out_file):
    entry = []
    f = open(out_file)
    while True:
        line = f.readline()
        if line:
            temp = []
            line = line.replace('\n', '')
            line = line.split(' ')
            print line
            for i in range(len(line)):
                temp.append(line[i])
            entry.append(temp)
        else:
            break
    for number in range(len(entry)):
        entry[number][0] = float(entry[number][0])
    ranklist = {}
    for i in range(len(entry)):
        ranklist[entry[i][1]] = entry[i][0]
    dict = sorted(ranklist.items(), key=lambda item:item[1], reverse=True)
    top_k = []
    for i in range(50):
        top_k.append(dict[i][0])
    print top_k
    name_txt = 'data/DBLP/author_name_id.txt'
    dict_name = read_name(name_txt)
    output = open(out_file, 'w')
    for i in range(len(dict)):
        a = "%s;%s;%lf\n" % (dict[i][0], dict_name[dict[i][0]], dict[i][1])
        output.write(a)
    output.close()

def write_and_format(network_file, motif, alpha, out_file, time_file):
    write_mpr_output(network_file, motif, alpha, out_file, time_file)
    format_output(out_file)

if __name__ == "__main__":
    # clear the time log for this experiment
    # find the adjacency matrix for vanilla pagerank and report runtime
    time_log = open("output/DBLP/time_log.txt", 'w')
    start = time.time()
    a, entry_unique = get_adjacency_matrix('data/DBLP/citation_network.txt')
    time_log.write("PR;%f\n" % (time.time() - start))
    time_log.close()
    
    # use the adjacency matrix to compute pageranks with power iteration
    v = compute_pagerank(a, 0.15)
    
    # write results to a file
    output = open('output/DBLP/result_PR.txt', 'w')
    for i in range(len(v)):
        a = "%lf %d\n" % (v[i], entry_unique[i])
        output.write(a)
    output.close()
    
    # format to get the researcher names associated with their ids
    format_output('output/DBLP/result_PR.txt')
    
    # obtain pageranks for all 7 motifs with alpha = 0.15
    write_and_format('data/DBLP/citation_network.txt', 'M1', 0.15, 'output/DBLP/result_M1.txt', "output/DBLP/time_log.txt")
    write_and_format('data/DBLP/citation_network.txt', 'M2', 0.15, 'output/DBLP/result_M2.txt', "output/DBLP/time_log.txt")
    write_and_format('data/DBLP/citation_network.txt', 'M3', 0.15, 'output/DBLP/result_M3.txt', "output/DBLP/time_log.txt")
    write_and_format('data/DBLP/citation_network.txt', 'M4', 0.15, 'output/DBLP/result_M4.txt', "output/DBLP/time_log.txt")
    write_and_format('data/DBLP/citation_network.txt', 'M5', 0.15, 'output/DBLP/result_M5.txt', "output/DBLP/time_log.txt")
    write_and_format('data/DBLP/citation_network.txt', 'M6', 0.15, 'output/DBLP/result_M6.txt', "output/DBLP/time_log.txt")
    write_and_format('data/DBLP/citation_network.txt', 'M7', 0.15, 'output/DBLP/result_M7.txt', "output/DBLP/time_log.txt")

    
