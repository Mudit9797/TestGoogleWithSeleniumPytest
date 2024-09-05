import requests

def test_get_request():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    # Check if the status code is 200 (OK)
    assert response.status_code == 200
    
    # Check if the response content type is JSON
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    
    # Parse the JSON response
    json_response = response.json()
    
    # Check if the JSON response contains the expected data
    assert json_response["id"] == 1
    assert json_response["userId"] == 1
    assert json_response["title"] is not None
    assert json_response["body"] is not None

def test_post_request():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    
    response = requests.post(url, json=payload)
    
    # Check if the status code is 201 (Created)
    assert response.status_code == 201
    
    # Parse the JSON response
    json_response = response.json()
    
    # Check if the JSON response contains the expected data
    assert json_response["title"] == "foo"
    assert json_response["body"] == "bar"
    assert json_response["userId"] == 1
    assert "id" in json_response

def test_put_request():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    payload = {
        "id": 1,
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }
    
    response = requests.put(url, json=payload)
    
    # Check if the status code is 200 (OK)
    assert response.status_code == 200
    
    # Parse the JSON response
    json_response = response.json()
    
    # Check if the JSON response contains the expected data
    assert json_response["id"] == 1
    assert json_response["title"] == "updated title"
    assert json_response["body"] == "updated body"
    assert json_response["userId"] == 1

def test_delete_request():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    response = requests.delete(url)
    
    # Check if the status code is 200 (OK)
    assert response.status_code == 200