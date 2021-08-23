import pandas as pd

def distance_price(dataframe: pd.DataFrame) -> None:
    Bus_price_200 = dataframe.loc[dataframe['Cities_distance'] <= 200]
    print("Average Bus price for 200 km travel: ", round(Bus_price_200["price_in_cents"].mean(),2), " cents")
    print("Minimum Bus price for 200 km travel: ", Bus_price_200["price_in_cents"].min(), " cents")
    print("Maximum Bus price for 200 km travel: ", Bus_price_200["price_in_cents"].max(), " cents")
    print("\n")

    Bus_price_800 = dataframe[(dataframe.Cities_distance >= 201) | (dataframe.Cities_distance <= 800)]
    print("Average Bus price for 201-800 km travel: ", round(Bus_price_800["price_in_cents"].mean(),2), " cents")
    print("Minimum Bus price for 201-800 km travel: ", Bus_price_800["price_in_cents"].min(), " cents")
    print("Maximum Bus price for 201-800 km travel: ", Bus_price_800["price_in_cents"].max(), " cents")
    print("\n")

    Bus_price_2000 = dataframe[(dataframe.Cities_distance >= 801) | (dataframe.Cities_distance <= 2000)]
    print("Average Bus price for 801-2000 km travel: ", round(Bus_price_2000["price_in_cents"].mean(),2), " cents")
    print("Minimum Bus price for 801-2000 km travel: ", Bus_price_2000["price_in_cents"].min(), " cents")
    print("Maximum Bus price for 801-2000 km travel: ", Bus_price_2000["price_in_cents"].max(), " cents")