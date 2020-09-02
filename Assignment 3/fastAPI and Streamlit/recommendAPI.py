import pandas as pd
import numpy as np
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import joblib
 
        
def recommend_user_user(userID):
    interactions = joblib.load('interactions')
    user_dict = joblib.load('user_dict')
    items_dict = joblib.load('items_dict')
    model = joblib.load('mf_model')
    
    def sample_recommendation_user(model, interactions, user_id, user_dict, 
                                   item_dict,threshold = 0,nrec_items = 10, show = True):
        '''
        Function to produce user recommendations
            - Prints list of items the given user has already bought
            - Prints list of N recommended items  which user hopefully will be interested in
        '''
        n_users, n_items = interactions.shape
        user_x = user_dict[user_id]
        scores = pd.Series(model.predict(user_x,np.arange(n_items)))
        scores.index = interactions.columns
        scores = list(pd.Series(scores.sort_values(ascending=False).index))
    
        known_items = list(pd.Series(interactions.loc[user_id,:] \
                                     [interactions.loc[user_id,:] > threshold].index) \
                                     .sort_values(ascending=False))
    
        scores = [x for x in scores if x not in known_items]
        return_score_list = scores[0:nrec_items]
        known_items = list(pd.Series(known_items).apply(lambda x: item_dict[x]))
        scores = list(pd.Series(return_score_list).apply(lambda x: item_dict[x]))
        if show == True:
            print("Known Likes:")
            counter = 1
            for i in known_items:
                print(str(counter) + '- ' + i)
                counter+=1

            print("\n Recommended Items:")
            counter = 1
            for i in scores:
                print(str(counter) + '- ' + i)
                counter+=1
        return return_score_list
    
    rec_list = sample_recommendation_user(model = model, 
                                      interactions = interactions, 
                                      user_id = userID, 
                                      user_dict = user_dict,
                                      item_dict = items_dict, 
                                      threshold = 4,
                                      nrec_items = 10)
    return rec_list


def recommend_item_item(itemID):
    interactions = joblib.load('interactions')
    user_dict = joblib.load('user_dict')
    items_dict = joblib.load('items_dict')
    model = joblib.load('mf_model')
    
    def create_item_emdedding_distance_matrix(model,interactions):
        df_item_norm_sparse = sparse.csr_matrix(model.item_embeddings)
        similarities = cosine_similarity(df_item_norm_sparse)
        item_emdedding_distance_matrix = pd.DataFrame(similarities)
        item_emdedding_distance_matrix.columns = interactions.columns
        item_emdedding_distance_matrix.index = interactions.columns
        return item_emdedding_distance_matrix
    
    
    item_item_dist = create_item_emdedding_distance_matrix(model = model,
                                                       interactions = interactions)
    
    def item_item_recommendation(item_emdedding_distance_matrix, item_id, 
                                 item_dict, n_items = 10, show = True):
        '''
        Function to create item-item recommendation
            - recommended_items = List of recommended items
        '''
        recommended_items = list(pd.Series(item_emdedding_distance_matrix.loc[item_id,:]. \
                                      sort_values(ascending = False).head(n_items+1). \
                                      index[1:n_items+1]))
        if show == True:
            print("Item of interest :{0}".format(item_dict[item_id]))
            print("Item similar to the above item:")
            counter = 1
            for i in recommended_items:
                print(str(counter) + '- ' +  item_dict[i])
                counter+=1
        return recommended_items
    
    rec_list_item = item_item_recommendation(item_emdedding_distance_matrix = item_item_dist,
                                    item_id = itemID,
                                    item_dict = items_dict,
                                    n_items = 5)
    
    return rec_list_item

def recommend_similar_user_item(itemID):
    interactions = joblib.load('interactions')
    user_dict = joblib.load('user_dict')
    items_dict = joblib.load('items_dict')
    model = joblib.load('mf_model')
    
    def sample_recommendation_item(model,interactions,item_id,user_dict,item_dict,number_of_user):
        '''
        Funnction to produce a list of top N interested users for a given item
            - user_list = List of recommended users 
        '''
        n_users, n_items = interactions.shape
        x = np.array(interactions.columns)
        scores = pd.Series(model.predict(np.arange(n_users), np.repeat(x.searchsorted(item_id),n_users)))
        user_list = list(interactions.index[scores.sort_values(ascending=False).head(number_of_user).index])
        return user_list 
    
    rec_item_user = sample_recommendation_item(model = model,
                               interactions = interactions,
                               item_id = itemID,
                               user_dict = user_dict,
                               item_dict = items_dict,
                               number_of_user = 15)
    
    return rec_item_user
    
