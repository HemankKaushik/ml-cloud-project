FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install streamlit scikit-learn pandas
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]