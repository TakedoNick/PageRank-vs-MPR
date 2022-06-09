from matplotlib import pyplot as plt

if __name__ == '__main__':
    
    f = open("output/DBLP/M7_alpha0.1_errors.txt")
    pr_1 = []
    mpr_1 = []
    while True:
        line = f.readline()
        if line:
            line = line.strip()
            line = line.split(';')
            pr_1.append(float(line[0]))
            mpr_1.append(float(line[1]))
        else:
            break
    f.close()
        
    f = open("output/DBLP/M7_alpha0.3_errors.txt")
    pr_3 = []
    mpr_3 = []
    while True:
        line = f.readline()
        if line:
            line = line.strip()
            line = line.split(';')
            pr_3.append(float(line[0]))
            mpr_3.append(float(line[1]))
        else:
            break
    f.close()
        
    f = open("output/DBLP/M7_alpha0.5_errors.txt")
    pr_5 = []
    mpr_5 = []
    while True:
        line = f.readline()
        if line:
            line = line.strip()
            line = line.split(';')
            pr_5.append(float(line[0]))
            mpr_5.append(float(line[1]))
        else:
            break
    f.close()
    
    fig, axes = plt.subplots(nrows = 1, ncols = 3, figsize = (10,6))
    
    axes[0].plot(range(5), pr_1, label = "PR")
    axes[0].plot(range(5), mpr_1, label = "MPR")
    axes[0].set_ylim(0.04, 0.2)
    axes[0].set_xlabel("modified citation network #")
    axes[0].set_ylabel("error")
    axes[0].legend()
    axes[0].set_title("alpha = 0.1")
    
    axes[1].plot(range(5,10), pr_3, label = "PR")
    axes[1].plot(range(5,10), mpr_3, label = "MPR")
    axes[1].set_ylim(0.04, 0.2)
    axes[1].set_xlabel("modified citation network #")
    axes[1].set_ylabel("error")
    axes[1].legend()
    axes[1].set_title("alpha = 0.3")
    
    axes[2].plot(range(10,15), pr_5, label = "PR")
    axes[2].plot(range(10,15), mpr_5, label = "MPR")
    axes[2].set_ylim(0.04, 0.2)
    axes[2].set_xlabel("modified citation network #")
    axes[2].set_ylabel("error")
    axes[2].legend()
    axes[2].set_title("alpha = 0.5")
    
    fig.tight_layout()
    plt.show()

