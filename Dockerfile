FROM python:3.9-slim
WORKDIR /app

# install required packages for system
#  1. First we have updated the packages in linux system
#  2. Second we have upgraded the system packages
#  3. Then we have installed mysqlclinet required to run  mysql database
#  4. removed all the list of the packages not packages 

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install app dependencies
RUN pip install mysqlclient
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Specify the command to run your application
CMD ["python", "app.py"]