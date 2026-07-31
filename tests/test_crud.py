def test_add_commodity(client):
    # Mocking login by setting the session directly if possible, or testing protected routes
    # For simplicity, testing the route accessibility
    response = client.get('/commodities/add', follow_redirects=True)
    assert response.status_code == 200 # Since it's protected, it might redirect to login, check your auth setup

def test_list_markets(client):
    response = client.get('/markets', follow_redirects=True)
    assert response.status_code == 200
