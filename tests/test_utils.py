from covid19_countries import utils


def test_recursive_camel_case():
    messy = {
        "i am messy": "yes you are",
        "i am aSubKey": {
            "whatIsMyDATA": 1,
            "NotSoFast": 2
        },
        "IBeList": [
            {
                "with": "key"
            },
            "string",
            1
        ],
        "2/19/20": "i am a date"
    }
    result = utils.recursive_camel_case(messy)
    print(result)

    assert "iAmMessy" in result
    assert "notSoFast" in result["iAmASubKey"]
    assert "whatIsMyDATA" in result["iAmASubKey"]
    assert "with" in result["iBeList"][0]
    assert "2/19/20" in result

