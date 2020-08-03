import json

def setState(key, value):
    with open('state.json', 'rb') as fp:
        state = json.load(fp)

    state[key] = value
    with open('state.json', 'w') as fp:
        json.dump(state, fp)

def getState(key):
    with open('state.json', 'rb') as fp:
        state = json.load(fp)

    return state[key]