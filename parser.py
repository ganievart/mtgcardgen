import json


def parse_json():
    # with open('CovenCounters_MIC.json') as f:
    with open('ModernAtomic.json') as f:
        d = json.load(f)

    # print(d["data"][0])
    for k, item in d['data'].items():  # use iteritems() if you're on Python 2
        # print('{};{};{}'.format(k, item['name'], item['text']))
        print(k + "\n" + item[0]['text'])
    # print('\n')


if __name__ == '__main__':
    parse_json()
