from api_client_get_user import private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUsersRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
# Добавили импорт функции validate_json_schema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

# Инициализируем запрос на создание пользователя
create_user_request = CreateUsersRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string1",
    first_name="string1",
    middle_name="string1"
)
create_user_response = public_users_client.create_user(create_user_request)
get_users = private_users_client.get_user_api(create_user_response.user.id)

# Получаем JSON схему из модели ответа
get_user_response_schema = GetUserResponseSchema.model_json_schema()

# Проверяем, что JSON ответ от API соответствует ожидаемой JSON схеме
validate_json_schema(instance=get_users.json(), schema=get_user_response_schema)