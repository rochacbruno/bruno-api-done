
def test_index(api_client):
    response = api_client.get("/")
    assert response.status_code == 200
    result = response.text
    assert "openapi.json" in result


def test_list_users(api_client, router):
    response = api_client.get(router.url_path_for('list_users'))
    assert response.status_code == 200
    assert response.json() == []
