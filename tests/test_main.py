from requests import get, post, delete, HTTPError


def test_api():
    root = "http://localhost:8000/"
    exampleitem_root = f"{root}exampleitems/"

    new_exampleitem = {
        "title": "Lorem ipsum",
        "value": 100,
        "code": "LIPS01",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    }

    try:
        response = get(root)
        response.raise_for_status()

        response = post(exampleitem_root, json=new_exampleitem)
        response.raise_for_status()
        doc = response.json()
        inserted_id = doc["id"]
        assert doc["title"] == "Lorem ipsum"
        assert doc["value"] == 100
        assert doc["code"] == "LIPS01"

        response = get(exampleitem_root)
        response.raise_for_status()
        ids = [s["id"] for s in response.json()]
        assert inserted_id in ids

        response = get(exampleitem_root + inserted_id)
        response.raise_for_status()

        response = delete(exampleitem_root + inserted_id)
        response.raise_for_status()

    except HTTPError as he:
        print(he.response.json())
        raise


if __name__ == "__main__":
    test_api()
