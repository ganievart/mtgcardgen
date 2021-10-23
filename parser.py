import json


def parse_json():
    # with open('CovenCounters_MIC.json') as f:
    with open('ModernAtomic.json') as f:
        d = json.load(f)
        names = []
        text = []

    for k, item in d['data'].items():
        if 'foreignData' in item[0] and len(item[0]['foreignData']) > 0:
            for i in item[0]['foreignData']:
                if i['language'] == 'Russian':
                    if 'text' in i:
                        names.append(i['name'])
                        text.append(i['text'])

    with open("names.txt", "w") as output:
        output.write('\n'.join(names))
    with open("text.txt", "w") as output:
        output.write('\n'.join(text))


if __name__ == '__main__':
    parse_json()
