    # Используем официальный образ Python
   FROM python:3.10

   # Устанавливаем рабочую директорию
   WORKDIR /app/portfolio

   # Копируем зависимости
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   # Копируем все файлы вашего проекта
   COPY . /app/
   COPY .env .env

   EXPOSE 8000

   RUN python manage.py collectstatic

   # Указываем команду для запуска приложения с Gunicorn
   CMD ["sh", "-c", "PYTHONPATH=/app/portfolio gunicorn portfolio.wsgi:application -b 0.0.0.0:8000"]









