Evaluates Google's PageRank algorithm against Motif-based PageRank (Zhao et. al., https://arxiv.org/pdf/1912.11817.pdf) according to multiple metrics including robustness to adding malicious links. Base implementation of MPR is from https://github.com/HKUST-KnowComp/Motif-based-PageRank.

IMPORTANT: The instructions to execute this code is below. If you have any trouble with using specific version of Python or these libraries, please instead use the jupyer notebook DSC291_NLA_PageRankvsMPR_Project_Main.ipynb. The code is transcribed there for easy use. It also displays the plots and visuals of our results.

Please use Python 2.7 and use the following libraries:

Numpy 1.11.0, Networkx 1.11, Scipy

If you do not have these, please install Python 2.7 from the official page, then run:

python2.7 -m pip install numpy==1.11.0

python2.7 -m pip install networkx==1.11

python2.7 -m pip install scipy



To produce the modified networks, run experiment/DBLP/build_modified_network.py. This creates citation_network_modified_#.txt for all # in [0,29], where each citation network has a number of extra nodes equal to 13935 (1% of the original edge count). Each of these extra nodes represents a new person in the network that points to exactly 1 random node that was originally in the network. This simulates adding extraneous links to the graph for testing robustness.

To use these networks to find robustness errors, run experiment/DBLP/compare.py. This creates errors for pagerank and for the highest performing motif, M7, when alpha is 0.1, 0.3, and 0.5. The errors are found in the files M7_alpha0.1_errors.txt, M7_alpha0.3_errors.txt, and M7_alpha0.5_errors.txt. Each error is the sum of absolute differences between pagerank values on the original citation network and the pagerank values on a modified (gamed) citation network.

That also creates time_log.py, which records the time taken to construct the matrices used for pagerank and MPR under the 7 different motifs.

To produce the pagerank values necessary for computing NDCG, run experiment/DBLP/obtain_pageranks.py. This creates result_PR.txt and result_M#.txt for # in [1,7]. The format of each line is id;name;ranking_value.

Then compute NDCG by running evalute/DBLP/compute_ndcg.py. This finds the NDCG values using the top 50, 100, 250, 500, and 1000 entries in the result files for pagerank and for MPR with each motif from 1 to 7. The results are stored in output/DBLP/ndcg_PR.txt and output/DBLP/ndcg_M#.txt for # in [1,7]. The format of each line is top_K;ndcg_value.
