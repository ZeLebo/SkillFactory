import json
Error = []
item_list = {
    'timestamp': 'int',
    'item_price': 'int',
    'referer': 'url',
    'location': 'url',
    'item_url': 'url',
    'remoteHost': 'str',
    'partyId': 'str',
    'sessionId': 'str',
    'pageViewId': 'str',
    'item_id': 'str',
    'basket_price': 'str',
    'userAgentName': 'str',
    'eventType': 'val',
    'detectedDuplicate': 'bool',
    'detectedCorruption': 'bool',
    'firstInSession': 'bool'
}


def check_int(item):
    return isinstance(item, int)


def check_str(item):
    return isinstance(item, str)


def check_bool(item):
    return isinstance(item, bool)


def check_url(item):
    if isinstance(item, str):
        return item.startswith("http://") or item.startswith("https://")
    else:
        return False


def check_str_value(item, val):
    if isinstance(item, str):
        return item in val
    else:
        return False
    
    
def error_logging(item, value, string):
    Error.append({item: f'{value}, {string}'})
    
    
def main():
    with open('newFile.json', encoding="utf8") as f:
        templates = json.load(f)
    for items in templates:
        for item in items:
            if item in item_list:
                if item_list[item] == 'int':
                    if not check_int(items[item]):
                        error_logging(item, item[item], f'{item_list[item]} type was expected')
                elif item_list[item] == 'str':
                    if not check_str(items[item]):
                        error_logging(item, item[item], f'{item_list[item]} type was expected')
                elif item_list[item] == 'bool':
                    if not check_bool(items[item]):
                        error_logging(item, item[item], f'{item_list[item]} type was expected')
                elif item_list[item] == 'url':
                    if not check_url(items[item]):
                        error_logging(item, item[item], f'{item_list[item]} type was expected')
                elif item_list[item] == 'val':
                    if not check_str_value(items[item], ['itemBuyEvent', 'itemViewEvent']):
                        error_logging(item, item[item], f'itemBuyEvent or itemViewEvent types were expected')
                else:
                    error_logging(item, item[item], 'unexpected value')
            else:
                error_logging(item, items[item], 'unexpected variable')

    if Error:
        print(f"Test failed")
        for err in Error:
            print(err)
    else:
        print("Test is passed")


if __name__ == "__main__":
    main()
