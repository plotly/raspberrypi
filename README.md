## Raspberry Pi Realtime Streaming with Plot.ly
https://plot.ly/~demos/1441/
[![Plotly-imp](readme_images/pi.jpg)](https://raspberrypi.com)

First, install the required modules and dependencies:
```bash
sudo apt-get install python-dev
wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | sudo python
sudo easy_install -U distribute
sudo apt-get install python-pip
sudo pip install rpi.gpio
sudo pip install plotly
```

Create a config.json file in this directory and input your
plotly API key, and your generated plotly streaming tokens
Sign up to plotly here: https://plot.ly/ssu
View your API key and streaming tokens here: https://plot.ly/settings

Example config.json:
```json
{
"plotly_streaming_tokens": ["your", "stream", "tokens"],
"plotly_api_key": "your_api_key",
"plotly_username": "your_user_name"
}
```

Create your sensor reading script, and start importing some modules in it!
```python
import plotly # plotly library
import json # used to parse config.json
import time # timer functions
import readadc # helper functions to read ADC from the Raspberry Pi
```

Initialize some variables with your creditials
```python
with open('./config.json') as config_file:
    plotly_user_config = json.load(config_file)

username = plotly_user_config['plotly_username']
api_key = plotly_user_config['plotly_api_key']
stream_token = plotly_user_config['plotly_streaming_tokens'][0]
stream_server = 'http://stream.plot.ly'
```

Initialize a Plotly Object
```python
p = plotly.plotly(username, api_key)
```


Initialize your graph (not streaming yet)
```python
p.plot([
	{'x': [],
	'y': [],
	'type': 'scatter',
	'stream': {
		'token': stream_token,
		'maxpoints': 1000
		}
	}],
	filename='Stream Example8888',
	fileopt='overwrite')
```

Specify the connected channel for your sensor
```python
sensor_pin = 0
```

Initialize the GPIO
```python
readadc.initialize()
```

Initialize the Plotly Streaming Object
```python
stream = plotly.stream(stream_token)
i = 0
```

Start looping and streamin'!
```python
while True:
	sensor_data = readadc.readadc(sensor_pin, readadc.PINS.SPICLK, readadc.PINS.SPIMOSI, readadc.PINS.SPIMISO, readadc.PINS.SPICS)
	s.write({'x': i, 'y': sensor_data })
	i+=1 # increment 1 on the 'x' axis with each reading
	time.sleep(1) # delay between stream posts
```
