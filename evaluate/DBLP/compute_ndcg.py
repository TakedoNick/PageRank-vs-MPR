from ndcg_DBLP import *

# generalizes __main__ code from ndcg_DBLP for our experiments
def compute_ndcg(results_file):
    txt_name3 = 'data/DBLP/h_index_all.txt'
    dict_author = construct(txt_name3)
    txt_name = results_file
    rank_value = 50
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
    out = open("output/DBLP/ndcg_values.txt", 'w')
    
    score = compute_ndcg("output/DBLP/result_PR.txt")
    out.write("%s;%f\n" % ('PR', score))
    
    for i in range(1,8):
        motif = "M%d" % (i)
        score = compute_ndcg("output/DBLP/result_%s.txt" % (motif))
        out.write("%s;%f\n" % (motif, score))
