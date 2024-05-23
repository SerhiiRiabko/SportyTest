import requests
import pytest

BASE_URL = "https://cat-fact.herokuapp.com"


def test_facts_endpoint():
    url = f"{BASE_URL}/facts"
    response = requests.get(url)

    # Validate status code
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Validate response structure
    facts = response.json()
    assert isinstance(facts, list), "Expected response to be a list of facts"

    # Validate each fact contains necessary fields
    required_fields = {'_id', 'text', 'type', 'user', 'upvotes'}
    for fact in facts:
        assert required_fields.issubset(
            fact.keys()), f"Fact is missing required fields: {required_fields - set(fact.keys())}"


if __name__ == "__main__":
    pytest.main([__file__])
