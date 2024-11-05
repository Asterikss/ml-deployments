import joblib
import pandas as pd
from functools import lru_cache

from models import ModelInput
from constants import CATEGORICAL_COLUMNS, BOOLEAN_COLUMNS


@lru_cache(maxsize=1)
def get_model():
    return joblib.load("./models/gradient_boosting_model.joblib")


@lru_cache(maxsize=1)
def get_encoder():
    return joblib.load("./models/ordinal_encoder.pkl")


async def get_prediction(data: ModelInput) -> float:
    model = get_model()
    encoder = get_encoder()

    data_df = pd.DataFrame([data.model_dump()])

    data_df[BOOLEAN_COLUMNS] = data_df[BOOLEAN_COLUMNS].replace({False: "no", True: "yes"})

    data_df[CATEGORICAL_COLUMNS] = encoder.transform(data_df[CATEGORICAL_COLUMNS])

    return model.predict(data_df)[0]
