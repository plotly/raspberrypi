## Raspberry Pi Realtime Streaming with Plot.ly

Create a config.json file in this directory and input your
plotly API key, and your generated plotly streaming tokens
Sign up to plotly here: https://plot.ly/ssu
View your API key and streaming tokens here: https://plot.ly/settings

Example config.json:
	{
    "plotly_streaming_tokens": ["your", "stream", "tokens"],
    "plotly_api_key": "your_api_key",
    "plotly_username": "your_user_name"
	}

Next, a few imports
	import plotly # plotly library
	import json # used to parse config.json
	import time # timer functions
	import readadc # helper functions to read ADC from the Raspberry Pi

initialize some variables with your creditials
	username = plotly_user_config['plotly_username']
	api_key = plotly_user_config['plotly_api_key']
	stream_token = plotly_user_config['plotly_streaming_tokens'][0]
	stream_server = 'http://stream.plot.ly'

initialize a Plotly Object
	p = plotly.plotly(username, api_key)


initialize your graph (not streaming yet)
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

Specify the connected channel for your sensor
	sensor_pin = 0

Initialize the GPIO
	readadc.initialize()

Initialize the Plotly Streaming Object
	stream = plotly.stream(stream_token)
	i = 0

Start looping and stremain'!
	while True:
		sensor_data = readadc.readadc(sensor_pin, readadc.PINS.SPICLK, readadc.PINS.SPIMOSI, readadc.PINS.SPIMISO, readadc.PINS.SPICS)
		s.write({'x': i, 'y': sensor_data })
		i+=1 # increment 1 on the 'x' axis with each reading
		time.sleep(1) # delay between stream posts
