import pandas as pd
import matplotlib.pyplot as plt

def distance_price(dataframe: pd.DataFrame) -> None:
    print("Bus travel distance less than 200: ")
    Bus_price_200 = dataframe.loc[dataframe['cities_distance'] <= 200]
    print("Average price is %.2f cents for %.2f hours travel" % (Bus_price_200["price_in_cents"].mean(), Bus_price_200["travel_time"].mean()))
    print("Minimun price is %.2f cents for %.2f hours travel" % (Bus_price_200["price_in_cents"].min(), Bus_price_200["travel_time"].min()))
    print("Maximum price is %.2f cents for %.2f hours travel" % (Bus_price_200["price_in_cents"].max(), Bus_price_200["travel_time"].max()))
    print("\n")

    print("Bus travel distance between 201 - 800: ")
    Bus_price_800 = dataframe[(dataframe.cities_distance >= 201) | (dataframe.cities_distance <= 800)]
    print("Average price is %.2f cents for %.2f hours travel" % (Bus_price_800["price_in_cents"].mean(), Bus_price_800["travel_time"].mean()))
    print("Minimun price is %.2f cents for %.2f hours travel" % (Bus_price_800["price_in_cents"].min(), Bus_price_800["travel_time"].min()))
    print("Maximum price is %.2f cents for %.2f hours travel" % (Bus_price_800["price_in_cents"].max(), Bus_price_800["travel_time"].max()))
    print("\n")

    print("Bus travel distance more than 801: ")
    Bus_price_2000 = dataframe[dataframe.cities_distance >= 801]
    print("Average price is %.2f cents for %.2f hours travel" % (Bus_price_2000["price_in_cents"].mean(), Bus_price_2000["travel_time"].mean()))
    print("Minimun price is %.2f cents for %.2f hours travel" % (Bus_price_2000["price_in_cents"].min(), Bus_price_2000["travel_time"].min()))
    print("Maximum price is %.2f cents for %.2f hours travel" % (Bus_price_2000["price_in_cents"].max(), Bus_price_2000["travel_time"].max()))