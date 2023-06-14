from collections import defaultdict
import glob
# import matplotlib.pyplot as plt
import os
import pandas as pd
# from venn import venn

tmp = pd.read_excel('Clusters.xlsx', sheet_name='Sheet2')
mapper = dict(zip(tmp.Genome, tmp.Cluster))
