from typing import Dict, Union, List
from stringcase import camelcase as camel
from stringcase import lowercase as lower
from stringcase import snakecase as snake
import re

def recursive_camel_case(obj):
        if isinstance(obj, dict):
            return _handle_dict(obj)
        elif isinstance(obj, list):
            return _handle_list(obj)
        else:
            return obj


def _handle_dict(dict: Dict) -> Dict:
    return {prep_n_camel(k): recursive_camel_case(dict[k]) for k in dict}

def _handle_list(list_: List) -> List:
    return [recursive_camel_case(el) for el in list_]

def prep_n_camel(key: str) -> str:
    """
    preps a string and then passes it to stringcase camel
    """
    #ignore keys that start with a number (because these are dates and likely special)
    if re.match("^[0-9]", key) is not None:
        return key
    #else make it camel case
    return camel(lower(snake(re.sub('[^0-9a-zA-Z]+', '_', key))))

