import pandas
import sklearn
triplets_file = '10000.txt'
from sklearn.model_selection import train_test_split
songs_metadata_file = 'song_data.csv'
song_df_1 = pandas.read_table(triplets_file,header=None)
song_df_1.columns = ['user_id', 'song_id', 'listen_count']
song_df_2 =  pandas.read_csv(songs_metadata_file)
song_df = pandas.merge(song_df_1, song_df_2.drop_duplicates(['song_id']), on="song_id", how="left")
#print(song_df.head())
song_df.to_csv('Main.csv')
song_grouped = song_df.groupby(['song_id']).agg({'listen_count': 'count'}).reset_index()
grouped_sum = song_grouped['listen_count'].sum()
song_grouped['percentage']  = song_grouped['listen_count'].div(grouped_sum)*100
song_grouped.sort_values(['listen_count', 'song_id'], ascending = [0,1])
#print(song_grouped.head())
train_data, test_data = train_test_split(song_df, test_size = 0.99, random_state=0)
import Recommenders
pm = Recommenders.popularity_recommender_py()
pm.create(train_data, 'user_id', 'song_id')
print("\n\n *****WELCOME*****")
print("\n SELECT WHICH USER YOU ARE?\n")
temp =int(input('1. New User?\n2. Existing User?\n'))
if temp == 2:
	user_id = str(input('Enter User ID\n'))
	#user_id = '94d5bdc37683950e90c56c9b32721edb5d347600'
	choice = 0
	is_model = Recommenders.item_similarity_recommender_py()
	is_model.create(train_data, 'user_id', 'song_id')
	user_items = is_model.get_user_items(user_id)
	print(is_model.recommend(user_id))	
else:
	print("You want to choose Artist?")
	x=int(input('\n 1. Yes \n 2.No\n'))
	is_model = Recommenders.item_similarity_recommender_py()
	if x==1:
		artist= str(input('Enter Artist Name: '))
		user_id = 'new'
		print(pm.recommend(user_id))
	else:
		user_id = 'new'
		print(pm.recommend(user_id))
'''
969cc6fb74e076a68e36a04409cb9d3765757508
is_model = Recommenders.item_similarity_recommender_py()
is_model.create(train_data, 'user_id', 'song_id')
#Print the songs for the user in training data
#user_id = '969cc6fb74e076a68e36a04409cb9d3765757508'
user_items = is_model.get_user_items(user_id)
#
print("------------------------------------------------------------------------------------")
print("Training data songs for the user userid: %s:" % user_id)
print("------------------------------------------------------------------------------------")

for user_item in user_items:
    print(user_item)

print("----------------------------------------------------------------------")
print("Recommendation process going on:")
print("----------------------------------------------------------------------")

#Recommend songs for the user using personalized model
print(is_model.recommend(user_id))
print(is_model.get_similar_items(['U Smile - Justin Bieber']))'''