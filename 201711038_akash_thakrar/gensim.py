import numpy as np
import pandas as pd
import csv
import sklearn.preprocessing as sk
from gensim.corpora import MmCorpus
from gensim.test.utils import get_tmpfile
import gensim
import gensim.models.lsimodel as ls

from sklearn.decomposition import TruncatedSVD
from sklearn.random_projection import sparse_random_matrix
from sklearn.utils.extmath import randomized_svd

df = pd.read_csv('Ratings_10_1.csv', dtype={'rating': float})
df.loc[:,'rating'] = sk.minmax_scale(df.loc[:,'rating'] )

R_df = df.pivot(index = 'user_id', columns ='song_id', values = 'rating').fillna(0).to_sparse(fill_value=0)
print(R_df.head())

R = R_df.as_matrix()
if(np.isinf(R).all()==False):
    print("tr")

Z=gensim.matutils.Dense2Corpus(R, documents_columns=True)
print(Z)

lsi=ls.LsiModel(Z, num_topics=3)
print("Sigma")

print(lsi.projection.s)
print("U")

print(lsi.projection.u)
print("VT")
V = gensim.matutils.corpus2dense(lsi[Z], len(lsi.projection.s)).T / lsi.projection.s
print(V)
