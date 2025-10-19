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

users_me = httpx.get("http://localhost:8000/api/v1/users/me", headers=get_users_headers)
users_me_data = users_me.json()

print("Get user response:", users_me_data)
print("Status Code:", users_me.status_code)
