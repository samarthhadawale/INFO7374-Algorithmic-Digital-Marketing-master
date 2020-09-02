#Core Packages
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from recommendAPI import recommend_user_user, recommend_item_item, recommend_similar_user_item

#init app
app = FastAPI(title="Snack Recommender System",
              description='''API to call from the recommendAPI''',
              version="0.1.0",)


@app.get("/recommend_users")
def get_recommend_users(userID:int):

    prediction_list = recommend_user_user(userID)

    if not prediction_list:
        raise HTTPException(status_code=400, detail="User Doesn’t Exist")
    else:
        return prediction_list
    
    
@app.get("/recommend_items")
def get_recommend_items(itemID:int):
    prediction_list_item = recommend_item_item(itemID)
    
    
    if not prediction_list_item:
        raise HTTPException(status_code=400, detail="Item Doesn’t Exist")

    else:
        return prediction_list_item
    
    
@app.get("/recommend_items_users")
def get_recommend_items_user(itemID:int):
    prediction_list_item_user = recommend_similar_user_item(itemID)
    
    
    if not prediction_list_item_user:
        raise HTTPException(status_code=400, detail="Item Doesn’t Exist")

    else:
        return prediction_list_item_user