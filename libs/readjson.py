import json
def readjson(jsonpath,name,rootname='Config'):
    json_read = json.load(open(jsonpath))
    return json_read[rootname][name]