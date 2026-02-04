from fastapi import FastAPI, APIRouter

app = FastAPI()

api = APIRouter(prefix="/koth/api")

@api.get("")      
@api.get("/")     
def read_root():
    return {"message":"Pikaista paranemista"}

app.include_router(api)