from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_read_main():
    """ Test the Root Route"""
    response = client.get("/")
    assert response.status_code == 200
    message = "This REST API will extract the key phrases or keywords from the input text"
    assert response.json() == {"message": message}


def test_extract_phrases():
    """ Extract Key Phrases test"""
    input_data = {
        "input_text": [
            "Welcome to Rake processing service"
        ]
    }
    response = client.post("/extract-phrases",json=input_data)
    output = response.json()
    output.pop("response_id")
    assert response.status_code == 200
    assert output == {
                    "key_phrases": [
                        [
                        "rake processing service",
                        "welcome"
                        ]
                    ],
                    "request_id": None,
                    "message": "Keywords Extracted Successfully"
                    }


def test_extract_phrases_error():
    """ Extract Key Phrases Error"""
    input_data = {
                "input_tex": [
                    "Welcome to Rake processing service"
                ]
                }
    response = client.post("/extract-phrases",json=input_data)
    assert response.status_code == 422
    assert response.json() == {
                            "detail": [
                                {
                                "loc": [
                                    "body",
                                    "input_text"
                                ],
                                "msg": "field required",
                                "type": "value_error.missing"
                                }
                            ]
                            }
                            