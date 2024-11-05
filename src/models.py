from enum import Enum
from pydantic import BaseModel


class Gender(str, Enum):
    male = "male"
    female = "female"


class Ethnicity(str, Enum):
    other = "other"
    hispanic = "hispanic"
    afam = "afam"


class Income(str, Enum):
    low = "low"
    high = "high"


class Region(str, Enum):
    other = "other"
    west = "west"


class ModelInput(BaseModel):
    gender: Gender
    ethnicity: Ethnicity
    fcollege: bool
    mcollege: bool
    home: bool
    urban: bool
    unemp: float
    wage: float
    distance: float
    tuition: float
    education: int
    income: Income
    region: Region
