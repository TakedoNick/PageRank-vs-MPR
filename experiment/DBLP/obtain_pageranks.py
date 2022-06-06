from pagerank_motif_direct import *
from result_read import *

# same as the __main__ code in pagerank_motif_direct but more general
# network_file: network file path, e.g. 'data/DBLP/citation_network.txt'
# motif: 'M1' or 'M2' or ... or 'M7'
# alpha: probability of restart, so float in 0 to 1
# out_file: should be 'output/DBLP/<desired file name>' e.g. 'output/DBLP/result_citation_M6_alpha0.4.txt'
def write_mpr_output(network_file, motif, alpha, out_file):
    a, entry_unique = construct_motif(network_file, 1, motif, alpha)

    # M = graphMove_newest(a)
    M = graphMove_new(a)
    pr = firstPr(M)
    p = 1 - alpha
    v = pageRank(p, M, pr)
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

if __name__ == "__main__":
    write_mpr_output('data/DBLP/citation_network.txt', 'M6', 0.4, 'output/DBLP/result_citation_M6_alpha0.4.txt')
    format_output('output/DBLP/result_citation_M6_alpha0.4.txt')
