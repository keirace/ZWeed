from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import dotenv_values

from actions import BaseActions
from schemas import Payload

config = dotenv_values(".env")

# print(os.environ)
# path = os.environ.get('PATH')
path = config['PATH']
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


class Payload(BaseModel):
    url: str
    image_id: str


@app.post("/"+path+"/predict")
# @app.post("/rovula/predict")
def predict(payload: Payload):
    print(payload)
    print('12344')
    return BaseActions.predict(payload)
    # return {
    #     "image_id": payload.image_id,
    #     "bbox_list": [{
    #         "category_id": 0,
    #         "bbox": {
    #             "x": 0,
    #             "y": 220.66666666666669,
    #             "w": 1050.0986882341442,
    #             "h": 525.3333333333333
    #         },
    #         "score": 0.63508011493555
    #     }]
    # }
