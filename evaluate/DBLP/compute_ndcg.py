from ndcg_DBLP import *

# generalizes __main__ code from ndcg_DBLP for our experiments
def compute_ndcg(results_file, K):
    txt_name3 = 'data/DBLP/h_index_all.txt'
    dict_author = construct(txt_name3)
    txt_name = results_file
    rank_value = K
    rank_array, name_array = read_top(txt_name, dict_author, rank_value)
    result = {}
    for i in range(len(rank_array)):
        score = dict_author[name_array[i]]
        result[name_array[i]] = score
    result_array = []
    dict = sorted(result.items(), key=lambda item: item[1], reverse=True)
    for i in range(len(dict)):
        result_array.append(dict[i][1])

    score = get_ndcg(result_array, rank_array)
    print score
    return score

if __name__ == '__main__':
    # for top 10, top 50, top 250, and top 500
    K_list = [50,100,250,500,1000]
    out = open("output/DBLP/ndcg_PR.txt", 'w')
    
    for K in K_list:
        score = compute_ndcg("output/DBLP/result_PR.txt", K)
        out.write("%d;%f\n" % (K,score))
    out.close()
    
    for i in range(1,8):
        motif = "M%d" % (i)
        out = open("output/DBLP/ndcg_%s.txt" % (motif), 'w')
        for K in K_list:
            score = compute_ndcg("output/DBLP/result_%s.txt" % (motif), K)
            out.write("%d;%f\n" % (K,score))
        out.close()
