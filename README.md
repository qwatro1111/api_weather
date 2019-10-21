# Api weather

### Start

This application uses https://openweathermap.org service to receive data.
To continue, you must register on the service and receive a app id.

Data is sent via the telegram messenger. You need to register on it to create
a new bot and get a secret key. After that, you should create a chat and connect
a bot to it to receive information.

### To configure the application, you must open the config.py file.

For "WEATHER" enter all the necessary data that you will receive on the service https://openweathermap.org/

To change the city in the WEATHER dictionary, in the "city" element, specify the new city.

After changing the city, you must specify the appropriate country code in the
WEATHER dictionary in the "country_code" element.

To configure the necessary messenger in the TELEGRAM dictionary,
specify the channel in the "channel" element and specify the token in the "token" element.

### Run the application

To run the application, run the send.py file.
