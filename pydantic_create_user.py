"""
{
  "id": "string",
  "email": "user@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
"""
import uuid

from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr, ValidationError

from apps.users.schema.users import CreateUserRequest
from clients.users.public_users_client import CreateUserResponseDict


class UserSchema(BaseModel):
    """
    Модель данных пользователя
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    """
    Запрос на создание пользователя
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName", default="Bond")
    first_name: str = Field(alias="firstName", default="James")
    middle_name: str = Field(alias="middleName", default="007")

class CreateUserResponseSchema(BaseModel):
    """
    Ответ с данными созданного пользователя
    """
    user: UserSchema

create_user_model = CreateUserRequestSchema(
    email="bond@james.com",
    password="007",
    lastName= "Bond",
    firstName= "James",
    middleName= "Bondovich"
)
print('Create User:', create_user_model)

user_dict = {
    "id": "user-id",
    "email": "user-bond@example.com",
    "lastName": "Ivanov",
    "firstName": "Valera",
    "middleName": "006"
}
user_dict_model = UserSchema(**user_dict)
print('User Dict model:', user_dict)

user_json = """
{
  "user": {
    "id": "user-id",
    "email": "user-bond@example.com",
    "lastName": "Ivanov",
    "firstName": "Petya",
    "middleName": "005"
  }
}
"""
user_json_model = CreateUserResponseSchema.model_validate_json(user_json)
print('User json model:', user_json_model)
print(user_json_model.model_dump(by_alias=True))
print(user_json_model.model_dump_json(by_alias=True))
