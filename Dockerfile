FROM python:3.8-slim
WORKDIR /app
COPY . /app 
RUN pip install discord.py==1.7.3
CMD ["python3", "bot.py"]
