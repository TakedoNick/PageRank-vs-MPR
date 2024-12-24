# Motif-Based PageRank Algorithm for Improving Search Relevance in Computer Science Journals

This repository contains the implementation and comparative study of Google's original PageRank algorithm and a modified Motif-Based PageRank (MPR) algorithm. The project focuses on improving search relevance within computer science journals tested using the DBLP dataset.

## Project Overview

Search engines like Google have revolutionized how information is retrieved. At the core of Google's original algorithm is the PageRank algorithm, which evaluates the importance of web pages. This project builds upon this foundation by introducing Motif-Based PageRank (MPR), an algorithm that incorporates higher-order graph structures (motifs) to improve node influence metrics.

The primary goals of this project include:
- Enhancing search relevance in research paper citations.
- Comparing the performance of PageRank and MPR based on efficiency, robustness, and relevance.
- Leveraging the DBLP dataset as a benchmark for experimentation.

---

## Features

- **Algorithms**: 
  - Original PageRank
  - Motif-Based PageRank (MPR)
- **Dataset**: DBLP citation dataset (comprehensive computer science bibliography).
- **Metrics**: Normalized Discounted Cumulative Gain (NDCG), computational efficiency, and robustness against graph modifications.
- **Visualization**: Error and NDCG plots for algorithm comparison.

---

## Experimental Setup

The project is structured into the following stages:
1. **Data Preprocessing**: Converting DBLP citation data into graph representations.
2. **Algorithm Implementation**:
   - PageRank algorithm using random-walk-based transition matrices.
   - MPR algorithm utilizing motifs as higher-order structures.
3. **Evaluation Metrics**:
   - Efficiency (computation time and memory).
   - Robustness (resilience to extraneous data).
   - Relevance (NDCG for search ranking).
4. **Visualization**: Comparative plots and insights.


![](/images/Experimental%20Setup.png)

---

## Tools and Libraries

- **Python 2.7**: Primary language for implementation.
- **Libraries**:
  - [NetworkX](https://networkx.org/) for graph processing.
  - [Pandas](https://pandas.pydata.org/) for data handling.
  - [Numpy](https://numpy.org/) and [Scipy](https://scipy.org/) for matrix operations.
  - [Matplotlib](https://matplotlib.org/) for result visualization.
  - [psutil](https://psutil.readthedocs.io/) and [tqdm](https://github.com/tqdm/tqdm) for profiling.
- **Platform**: Google Colab for cloud-based execution.
- **Dataset**: DBLP XML snapshot.

---

## Setup Instructions

### Prerequisites

Use **Python 2.7** with the following library versions:
- `Numpy 1.11.0`
- `Networkx 1.11`
- `Scipy`

If you do not have these installed, you can install Python 2.7 from the official website and use the following commands to install the required libraries:
```bash
python2.7 -m pip install numpy==1.11.0
python2.7 -m pip install networkx==1.11
python2.7 -m pip install scipy
```

---

## Instructions for Execution

### Step 1: Simulating Modified Networks

To produce modified networks for robustness testing:

1.	Run the script:

```python2.7 experiment/DBLP/build_modified_network.py```

2.	This will generate citation_network_modified_#.txt files for all # in [0,29]. Each file simulates the addition of 1% extraneous nodes to the original network, where each citation network has a number of extra nodes equal to 13935 (1% of the original edge count). Each of these extra nodes represents a new person in the network that points to exactly 1 random node that was originally in the network.


### Step 2: Compute Robustness Errors

1. Run the comparision script

```python2.7 experiment/DBLP/compare.py```

2.	This generates:
  •	M7_alpha0.1_errors.txt
	•	M7_alpha0.3_errors.txt
	•	M7_alpha0.5_errors.txt
Each file records the error between PageRank and MPR for the highest performing motif, M7, when alpha is 0.1, 0.3, and 0.5.

### Step 3: Record Populate and Search Times

```python2.7 experiment/DBLP/time_log.py```

This records the time taken to construct the matrices used for pagerank and MPR under the 7 different motifs.

### Step 4: Obtain PageRank Values

```python2.7 experiment/DBLP/obtain_pageranks.py```

This creates result_PR.txt and result_M#.txt for motifs in [1,7]. The format of each line is id;name;ranking_value.

### Step 5: Compute Normalized Discounted Cumulative Gain

```python2.7 evalute/DBLP/compute_nodes.py```

This finds the NDCG values using the top 50, 100, 250, 500, and 1000 entries in the result files for pagerank and for MPR with each motif from 1 to 7. The results are stored in output/DBLP/ndcg_PR.txt and output/DBLP/ndcg_M#.txt for # in [1,7] which contains lines in the format: `top_K;ndcg_value`
Where top_K represents the number of top-ranked results used.



The instructions to execute this code are below. If you have issues with using a specific version of Python or these libraries, instead use the [jupyter notebook](https://github.com/takedonick/PageRank-vs-MPR/blob/master/DSC291_NLA_PageRankvsMPR_Project_Main.ipynb). The code is transcribed there for easy use. It also displays the plots and visuals of our results.


# Results

![Compute Time](/images/Compute%20Time.png)
![Memory Usage](/images/Memory%20Usage.png)
![Robustness Error](/images/Robustness%20Error.png)
![NDCG](/images/NDCG.png)

# Refereces

[1] Dehmer, Matthias, ed. Structural analysis of complex networks. Springer Science & Business Media, 2010.

[2] H. Zhao, X. Xu, Y. Song, D. L. Lee, Z. Chen and H. Gao, "Ranking Users in Social Networks with Motif-Based PageRank," in IEEE Transactions on Knowledge and Data Engineering, vol. 33, no. 5, pp. 2179-2192, 1 May 2021, doi: 10.1109/TKDE.2019.2953264.

[3] Brin, Sergey, and Lawrence Page. "The anatomy of a large-scale hypertextual web search engine." Computer networks and ISDN systems 30.1-7 (1998): 107-117.

[4] Page, Lawrence, et al. The PageRank citation ranking: Bringing order to the web. Stanford InfoLab, 1999.

[5] Altman, Alon; Tennenholtz, Moshe (2005). Ranking systems. New York, New York, USA: ACM Press.

[6] Palacios-Huerta, Ignacio; Volij, Oscar (2004). "The Measurement of Intellectual Influence" (PDF). Econometrica. The Econometric Society. 72 (3): 963–977.

[7] Martin, Kimball (2014). Graph Theory and Social Networks.

