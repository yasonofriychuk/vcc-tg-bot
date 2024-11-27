# Используем Python 3.11
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt и устанавливаем зависимости
COPY bot/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код бота
COPY bot/ .

# Указываем точку входа
CMD ["python", "main.py"]
