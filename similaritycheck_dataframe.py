import pandas as pd
from thefuzz import fuzz

def fuzz_pandas_df_example():
    #Create test data
    #main
    dict_main = {
        "country": ["England", "Scotland", "Wales", "United Kingdom", "Northern Ireland"],
        "population_in_millions": [55.98, 5.45, 3.14, 67.33, 1.89]
    }
    #wrong
    dict_wrong = {
        "country": ["Northern Iland", "Wles", "Scotlnd", "Englnd", "United K."],
        "GDP_per_capita": [24900, 23882, 37460, 45101, 46510.28]
    }
    existing_data = pd.DataFrame(dict_main)
    imported_data = pd.DataFrame(dict_wrong)
    print(existing_data, imported_data, sep="\n\n")

    #attempting to join as is = FAILS
    data = pd.merge(existing_data, imported_data, on="country", how="left")
    print(data.head())

    #rename misspelled columns using Fuzzy Matching, then joining = WORKS
    from thefuzz import process
    imported_data["country"] = imported_data["country"].apply(
        lambda x: process.extractOne(x, existing_data["country"], scorer=fuzz.partial_ratio)[0]
    )
    data = pd.merge(existing_data, imported_data, on="country", how="left")
    print(data.head())
    return

if __name__ == "__main__":
    fuzz_pandas_df_example()