import pandas as pd

def data_clean(tickets: pd.DataFrame, cities: pd.DataFrame, stations: pd.DataFrame, providers: pd.DataFrame, distances: pd.DataFrame) -> pd.DataFrame:
    cities_col = cities[["id", "unique_name"]]
    dataframe = pd.merge(left=tickets, right=cities_col, how='left', left_on="o_city", right_on="id")
    dataframe = dataframe.rename(columns={"unique_name": "city_origin"})
    dataframe = dataframe.drop("id_y", axis=1)

    dataframe = pd.merge(left=dataframe, right=cities_col, how='left', left_on="d_city", right_on="id")
    dataframe = dataframe.rename(columns={"unique_name": "city_destiny"})
    dataframe = dataframe.drop("id", axis=1)

    stations_col = stations[["id", "unique_name"]]
    dataframe = pd.merge(left=dataframe, right=stations_col, how='left', left_on="o_station", right_on="id")
    dataframe = dataframe.rename(columns={"unique_name": "station_origin"})
    dataframe = dataframe.drop("id", axis=1)

    dataframe = pd.merge(left=dataframe, right=stations_col, how='left', left_on="d_station", right_on="id")
    dataframe = dataframe.rename(columns={"unique_name": "station_destiny"})
    dataframe = dataframe.drop("id", axis=1)

    providers_col = providers[["id", "name", "transport_type"]]
    dataframe = pd.merge(left=dataframe, right=providers_col, how='left', left_on="company", right_on="id")
    dataframe = dataframe.rename(columns={"name": "transport_name", "transport_type": "type"})
    dataframe = dataframe.drop("id", axis=1)

    # dataframe = dataframe.dropna()
    # dataframe["station_distance"] = new_df.apply(lambda x: result[x["station_origin"]][x["station_destiny"]], axis=1)
    dataframe["cities_distance"] = dataframe.apply(lambda x: distances[x["city_origin"]][x["city_destiny"]], axis=1)

    dataframe['departure_ts']= pd.to_datetime(dataframe['departure_ts']) 
    dataframe['arrival_ts']= pd.to_datetime(dataframe['arrival_ts'])
    travel_time = dataframe.arrival_ts - dataframe.departure_ts
    dataframe["travel_time"] = travel_time.dt.total_seconds() * 0.000277
    return dataframe