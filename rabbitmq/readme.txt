brew install rabbitmq-server
brew services restart rabbitmq
listen on port 15672 
URL localhost:15672

python -m pip install pika --upgrade
python -m pip install rabbitmq --upgrade
