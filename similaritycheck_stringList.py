import sys
from thefuzz import fuzz
from thefuzz import process

def get_closest_match(inputList, topN):
    #newList = [list1[:i] + list1[(i+1):] for i in range(len(list1))]
    #print(newList)
    ret = []
    for i in range(len(inputList)):
        #[print(process.extract(inputList[i], inputList[:i] + inputList[(i+1):], limit=topN, scorer=fuzz.ratio))]
        [ret.append(process.extract(inputList[i], inputList[:i] + inputList[(i+1):], limit=topN, scorer=fuzz.token_set_ratio))]
    return ret

if __name__ == "__main__":
    inputList = sys.argv[1]
    topN = sys.argv[2]
    #inputList = ["string1", "string2", "string10", "strong1", "strong10"]
    #inputList = ["ABC Hotel", "Hotel ABC", "Hotl AB", "Hotel AB NewYork State"]
    #topN = 3
    print(get_closest_match(inputList, topN))