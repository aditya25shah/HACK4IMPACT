from fastapi import FastAPI 
router = FastAPI()

@router.get("/")
def read_root():
    return {"Heyy" : "There"}