import requests
import pytest

BASE_URL = "https://cat-fact.herokuapp.com"


def test_fact_data_integrity():
    url = f"{BASE_URL}/facts"
    response = requests.get(url)

    # Validate status code
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Validate response structure
    facts = response.json()
    assert isinstance(facts, list), "Expected response to be a list of facts"

    # Validate each fact's type and text
    for fact in facts:
        assert fact['type'] == 'cat', f"Expected type 'cat', but got {fact['type']}"
        assert isinstance(fact['text'], str) and fact['text'], "Expected non-empty string for text"


if __name__ == "__main__":
    pytest.main([__file__])
