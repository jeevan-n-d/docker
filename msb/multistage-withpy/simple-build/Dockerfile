FROM python:3.14-slim
LABEL maintainer="jeeva"
LABEL project="simple-calculator"
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN ls -ltr
ENV APP_NAME=Calculator
CMD ["python3","cal.py"]
