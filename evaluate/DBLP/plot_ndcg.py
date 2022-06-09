from matplotlib import pyplot as plt

if __name__ == '__main__':
    f = open("output/DBLP/ndcg_PR.txt")
    
    K_list = []
    ndcg_PR = []
    while True:
        line = f.readline()
        if line:
            line = line.strip()
            line = line.split(';')
            K = line[0]
            val = float(line[1])
            
            K_list.append(K)
            ndcg_PR.append(val)
        else:
            break
    f.close()
        
    ndcg_M = []
    for i in range(1,8):
        ndcg_M_i = []
        f = open("output/DBLP/ndcg_M%s.txt" %(i))
        while True:
            line = f.readline()
            if line:
                line = line.strip()
                line = line.split(';')
                K = line[0]
                val = float(line[1])
                
                ndcg_M_i.append(val)
            else:
                break
        f.close()
        ndcg_M.append(ndcg_M_i)
    
    fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize = (10,6))
    
    for i in range(1,8):
        axes[0].plot(K_list, ndcg_M[i-1], label = "M%s" % (i))
    
    axes[0].set_ylim(0.885, 0.965)
    axes[0].set_xlabel("top K values used")
    axes[0].set_ylabel("NDCG")
    axes[0].legend()
    
    for i in range(1,8):
        axes[1].plot(K_list, ndcg_M[i-1], label = "M%s" % (i), color = 'black')
    axes[1].plot(K_list, ndcg_PR, label = "PR", color = 'blue')
    axes[1].set_ylim(0.885, 0.965)
    axes[1].set_xlabel("top K values used")
    axes[1].set_ylabel("NDCG")
    axes[1].legend()
    
    fig.tight_layout()
    plt.show()
