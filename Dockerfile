# filepath: c:\Users\Lenovo\Desktop\mini-project-lpu-1\Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]