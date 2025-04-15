from dotenv import load_dotenv
from openai import OpenAI
import os

# Загружаем переменные из файла .env
load_dotenv()

# Получаем значение API ключа из переменных окружения
api_key = os.getenv("OPENAI_API_KEY")

# Проверяем, что ключ существует
if not api_key:
    raise ValueError("API ключ не найден в файле .env")


# Создаем клиент OpenAI
client = OpenAI()

try:
    # Отправляем запрос
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Скажи, что это тест"}],
    )
    print(stream)
except Exception as e:
    print(f"Произошла ошибка: {e}")

    