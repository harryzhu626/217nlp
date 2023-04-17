import pandas as pd

def todf(entities):
    return pd.DataFrame(data=entities, columns=['entity', 'count'])