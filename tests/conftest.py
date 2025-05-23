import pytest
import json

# Fixture for constructing full API URLs
@pytest.fixture
def api_url():
    def get_api_url(endpoint):
        base_url = "https://your-api-domain.com"  # Replace with your actual base URL
        return f"{base_url}{endpoint}"
    return get_api_url


# Fixture for loading JSON payloads from a file
@pytest.fixture
def get_payload():
    def load_payload(file_path, index=0):
        with open(file_path, "r") as file:
            data = json.load(file)
            if "payloads" in data and len(data["payloads"]) > index:
                return data["payloads"][index]
            raise IndexError(f"No payload found at index {index}.")
    return load_payload