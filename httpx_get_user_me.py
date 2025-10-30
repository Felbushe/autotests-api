import httpx

login_payload_user = {
    "email": "user@example.com",
    "password": "string"
}

login_response_user = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload_user)
login_response_data_user = login_response_user.json()

print("Login response user:", login_response_data_user)
print("Status Code:", login_response_user.status_code)


get_users_headers = {
    "Authorization": f"Bearer {login_response_data_user['token']['accessToken']}"
}

get_users_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=get_users_headers)
get_users_response_data = get_users_response.json()

print("Get user response:", get_users_response_data)
print("Status Code:", get_users_response.status_code)
