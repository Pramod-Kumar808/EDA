import pandas as pd
import numpy as np


def data_clean(tickets: pd.DataFrame, cities: pd.DataFrame, stations: pd.DataFrame, providers: pd.DataFrame, distances: pd.DataFrame) -> pd.DataFrame:
    cities_col = cities[["id", "unique_name"]]
    new_df = pd.merge(left=tickets, right=cities_col, how='left', left_on="o_city", right_on="id")
    new_df = new_df.rename(columns={"unique_name": "city_origin"})
    new_df = new_df.drop("id_y", axis=1)

    new_df = pd.merge(left=new_df, right=cities_col, how='left', left_on="d_city", right_on="id")
    new_df = new_df.rename(columns={"unique_name": "city_destiny"})
    new_df = new_df.drop("id", axis=1)

    stations_col = stations[["id", "unique_name"]]
    new_df = pd.merge(left=new_df, right=stations_col, how='left', left_on="o_station", right_on="id")
    new_df = new_df.rename(columns={"unique_name": "station_origin"})
    new_df = new_df.drop("id", axis=1)
    new_df

    new_df = pd.merge(left=new_df, right=stations_col, how='left', left_on="d_station", right_on="id")
    new_df = new_df.rename(columns={"unique_name": "station_destiny"})
    new_df = new_df.drop("id", axis=1)

    providers_col = providers[["id", "name", "transport_type"]]
    new_df = pd.merge(left=new_df, right=providers_col, how='left', left_on="company", right_on="id")
    new_df = new_df.rename(columns={"name": "transport_name", "transport_type": "type"})
    new_df = new_df.drop("id", axis=1)

    # new_df = new_df.dropna()
    # new_df["station_distance"] = new_df.apply(lambda x: result[x["station_origin"]][x["station_destiny"]], axis=1)
    new_df["Cities_distance"] = new_df.apply(lambda x: distances[x["city_origin"]][x["city_destiny"]], axis=1)
    return new_df