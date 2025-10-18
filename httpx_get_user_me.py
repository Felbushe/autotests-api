import httpx

login_payload_user = {
    "email": "user@example.com",
    "password": "string"
}

login_response_user = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload_user)
login_response_data_user = login_response_user.json()

print("Login response user:", login_response_data_user)
print("Status Code:", login_response_user.status_code)

refresh_payload = {
    "refreshToken": login_response_data_user["token"]["refreshToken"]
}

# Выполняем запрос на обновление токена
refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()

# Выводим обновленные токены
print("Refresh response:", refresh_response_data)
print("Status Code:", refresh_response.status_code)

access_token = {
        login_response_data_user ['token']['accessToken']
}
headers = {
    "Authorization": f"Bearer {access_token}"
}

users_me = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
users_me_data = users_me.json()

print("Info:", users_me_data)
print("Status Code:", users_me.status_code)
