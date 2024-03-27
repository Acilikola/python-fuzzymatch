import sys
from thefuzz import fuzz

def fuzz_example():
    # Check the similarity score
    name = "Kurtis Pykes"
    full_name = "Kurtis K D Pykes"

    #simple ratio - Order will not effect if strings do not match
    print(f"Similarity score: {fuzz.ratio(name, full_name)}")

    #partial ratio - Order matters
    print(f"Similarity score: {fuzz.partial_ratio(name, full_name)}")

    #token sort ratio - Order does not matter
    print(f"Token sort ratio similarity score: {fuzz.token_sort_ratio(name, full_name)}")
    #token set ratio - similar to token sort, except common words are removed
    print(f"Token set ratio similarity score: {fuzz.token_set_ratio(name, full_name)}")

    #list example using process()
    # more at https://www.datacamp.com/tutorial/fuzzy-string-python
    from thefuzz import process
    collection = ["AFC Barcelona", "Barcelona AFC", "barcelona fc", "afc barcalona"]
    print(process.extract("barcelona", collection, scorer=fuzz.ratio))
    return

def get_similarity_scores(str1, str2):
    #simple ratio
    ret = f"Simple ratio similarity score: {fuzz.ratio(str1, str2)}\n"
    #partial ratio
    ret += f"Partial ratio similarity score: {fuzz.partial_ratio(str1, str2)}\n"
    #token sort ratio
    ret += f"Token sort ratio similarity score: {fuzz.token_sort_ratio(str1, str2)}\n"
    #token set ratio
    ret += f"Token set ratio similarity score: {fuzz.token_set_ratio(str1, str2)}"
    return ret

if __name__ == "__main__":
    #fuzz_example()
    #str1 = sys.argv[1]
    #str2 = sys.argv[2]
    str1 = "ABC Hotel"
    #str2 = "Hotel ABC"
    str2 = "Hotel AB NewYork Allstate Way"
    print(get_similarity_scores(str1, str2))