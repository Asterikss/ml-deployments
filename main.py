import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

coll_dist = pd.read_csv("./data/CollegeDistance.csv", index_col=0)

categorical_columns = coll_dist.select_dtypes(include=["object", "bool", "category"]).columns

encoder = OrdinalEncoder()

coll_dist[categorical_columns] = encoder.fit_transform(coll_dist[categorical_columns])

coll_dist[categorical_columns] = coll_dist[categorical_columns].astype(int)

coll_dist.to_csv("CollegeDistanceCleaned.csv", index=False)
