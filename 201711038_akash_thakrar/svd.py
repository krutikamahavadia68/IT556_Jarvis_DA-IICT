import pandas as pd
import numpy as np
import sklearn.preprocessing as sk
from sklearn.decomposition import TruncatedSVD
from sklearn.random_projection import sparse_random_matrix
from sklearn.utils.extmath import randomized_svd

df = pd.read_csv('./Ratings_10_1.csv', dtype={'rating': float})
df.loc[:,'rating'] = sk.minmax_scale(df.loc[:,'rating'] )
R_df = df.pivot(index = 'user_id', columns ='song_id', values = 'rating').fillna(0)

R = R_df.as_matrix()
user_ratings_mean = np.mean(R, axis = 1)

R_demeaned = R - user_ratings_mean.reshape(-1, 1)
U, Sigma, VT = randomized_svd(R,n_components=2)

svd = TruncatedSVD(n_components=20, n_iter=7)
svd.fit(R)
print("U : ")
print(U)
print("Sigma : ")
print(Sigma)
print("VT : ")
print(VT)


print(svd.explained_variance_ratio_)  

print(svd.components_)  

print(svd.singular_values_) 
