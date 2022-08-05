import requests

def getData():
    url = "https://v1.nocodeapi.com/ascoding/fit/IYZznFpbqYyzwDJw/aggregatesDatasets?dataTypeName=weight,calories_expended,steps_count,heart_minutes"
    params = {}
    r = requests.get(url = url, params = params)
    result = r.json()
    return result
    # print(result)
