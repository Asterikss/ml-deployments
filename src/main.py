import logging
from typing import Dict

from fastapi import FastAPI
import uvicorn

from models import ModelInput
from predict import get_prediction

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

app = FastAPI()

@app.post("/predict")
async def predict(data: ModelInput) -> Dict[str, float]:
    logger.info("Predict endpoint was accessed")
    return {"score": await get_prediction(data)}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8032, reload=False)
