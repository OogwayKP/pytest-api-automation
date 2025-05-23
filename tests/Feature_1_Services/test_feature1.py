import pytest
import requests

@pytest.mark.parametrize("index", [0, 1])
def test_api_service_with_different_payload(api_url, get_payload, index):
    # Example file path structure: adjust 'your_test_folder' and file name as needed
    file_path = "tests/sample_folder/payloads/sample_payloads.json"
    
    # Load the payload at the specified index
    selected_payload = get_payload(file_path=file_path, index=index)
    
    # Replace with the specific endpoint you are testing
    endpoint = "/your_api_endpoint"

    # Send POST request to the constructed URL with the selected payload
    response = requests.post(api_url(endpoint), json=selected_payload)

    # Basic assertion for successful response
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"