FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "M6_app.py", "--server.port=8501", "--server.address=0.0.0.0"]