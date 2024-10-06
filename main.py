from fastapi import FastAPI
from enum import Enum

class AvailableCuisines(str, Enum):
    indian = 'indian'
    italian = 'italian'
    american = 'american'

app = FastAPI()

food_items = {
    'indian':['samosa','pav bhaji'],
    'italian': ['pasta','pizza'],
    'american': ['hot dog', 'chicken over rice']
}

@app.get("/get_items/{cuisine}")
async def get_items(cuisine: AvailableCuisines):
    return food_items.get(cuisine)

coupon_code = {
    1: '10%',
    2: '20%',
    3: '30%' 
}

@app.get('/get_code/{code}')
async def get_items(code: int):
    return {'Discount Amount': coupon_code.get(code)}

# Get documentation
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc