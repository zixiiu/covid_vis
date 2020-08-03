import json


def getTop10(keyword):
    with open('./Data/today.json', 'rb') as fp:
        today = json.load(fp)
    cleaned_today = []
    for x in today:
        if type(x) == list and len(x) == 1:
            cleaned_today.append(x[0])

    today = cleaned_today

    today.sort(key=lambda x: x[keyword], reverse = True)

    res = {}
    rank = 1
    for i in today[:10]:
        res[rank] = (i['country'],i[keyword])
        rank += 1

    return res


if __name__ == '__main__':
    res = getTop10()
    print(res)