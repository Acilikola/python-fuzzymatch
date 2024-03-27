import sys
from ast import literal_eval
from thefuzz import fuzz
from thefuzz import process

def get_closest_match(inputDict, topN, onlyKeys=False):
    #newDict = [{i:inputDict[i] for i in inputDict if i!=k} for k in inputDict.keys()]
    #print(newDict)
    ret = []
    for k in inputDict.keys():
        #[print(process.extract(inputDict[k], {i:inputDict[i] for i in inputDict if i!=k}, limit=topN, scorer=fuzz.ratio))]
        ret.append(process.extract(inputDict[k], {i:inputDict[i] for i in inputDict if i!=k}, limit=topN, scorer=fuzz.ratio))
    
    if(onlyKeys):
        ret2 = []
        for lst in ret:
            tmpLst = []
            for i in lst:
                tmpLst.append(i[1:])
            ret2.append(tmpLst)
        #print(ret2)
        return ret2
    return ret

if __name__ == "__main__":
    i = sys.argv[1]
    inputDict = literal_eval(i)
    #print(inputDict)
    #print(type(inputDict))
    topN = sys.argv[2]
    onlyKeys = sys.argv[3]
    #inputDict = {"key1":"string1", "key2":"string2", "key3":"string10", "key4":"strong1", "key5":"strong10"}
    #topN = 3
    #onlyKeys = True
    print(get_closest_match(inputDict, topN, onlyKeys))