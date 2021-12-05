from django.shortcuts import render
import requests
import pika

# Create your views here.

def callback(body):
    print("[x] Received %r" % body)

def consume_message():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    ) 
    channel = connection.channel()
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    
def index(request):
    return render(request, 'index.html')

def city_temperatures(request):

    # api_key = '58ad826db161fab880e01b5a75215e8e'

    city_query = request.GET
    city = city_query.get('City')
    def produce_message():
        connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue = 'hello')
        channel.basic_publish(exchange='', routing_key = 'hello', body = city)

    if city != None:
        produce_message()    
        message = consume_message()

    if city == 'Lancaster':
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=58ad826db161fab880e01b5a75215e8e".format(message)
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        # relevant data set from this call. Temperature returned in kelvin units. 
        kelvin_temp = int(data.get('main', {}).get('temp'))
        celsius_temp_lancaster = round((kelvin_temp - 273.15))
        print(celsius_temp_lancaster)
        return render(request, 'weather.html', {"celsius_temp_lancaster":celsius_temp_lancaster})

    elif city == 'Toronto':
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=58ad826db161fab880e01b5a75215e8e".format(message)
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        # relevant data set from this call. Temperature returned in kelvin units.
        kelvin_temp = int(data.get('main', {}).get('temp'))
        celsius_temp_toronto = round((kelvin_temp - 273.15))  
        print(celsius_temp_toronto)
        return render(request, 'weather.html', {"celsius_temp_toronto":celsius_temp_toronto})
    return render(request, 'weather.html',)




