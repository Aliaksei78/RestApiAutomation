import requests
from utilities.resources import ApiResources
from utilities.configurations import get_config


def after_scenario(context, scenario):
    if 'library' in scenario.tags:
        url_delete_book = get_config()['API']['endpoint'] + ApiResources.deleteBook
        book_id = context.add_book_response_json['ID']
        body_delete_book = {"ID": book_id}
        headers_delete_book = {"Content-Type": "application/json"}
        response_delete_book = requests.post(url_delete_book, json=body_delete_book, headers=headers_delete_book)
        response_delete_book_json = response_delete_book.json()
        print(response_delete_book_json)
        assert response_delete_book.status_code == 200
        assert response_delete_book_json["msg"] == "book is successfully deleted"
    else:
        pass
