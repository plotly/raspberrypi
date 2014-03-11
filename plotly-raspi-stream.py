import plotly
import json
import time
import readadc

# Fill in the config.json file in this directory with your plotly username,
# plotly API key, and your generated plotly streaming tokens
# Sign up to plotly here: https://plot.ly/ssu
# View your API key and streaming tokens here: https://plot.ly/settings

with open('./config.json') as config_file:
    plotly_user_config = json.load(config_file)

username = plotly_user_config['plotly_username']
api_key = plotly_user_config['plotly_api_key']
stream_token = plotly_user_config['plotly_streaming_tokens'][0]
stream_server = 'http://stream.plot.ly'

p = plotly.plotly(username, api_key)
p.ioff();

print p.plot([{'x': [], 'y': [], 'type': 'scatter',
            'stream': {'token': stream_token, 'maxpoints': 200}
          }], filename='Raspberry Pi Streaming Example Values', fileopt='overwrite')

# temperature sensor connected channel 0 of mcp3008
sensor_pin = 0
readadc.initialize()

i=0
s = plotly.stream(stream_token)

#the main sensor reading loop
while True:
		sensor_data = readadc.readadc(sensor_pin, readadc.PINS.SPICLK, readadc.PINS.SPIMOSI, readadc.PINS.SPIMISO, readadc.PINS.SPICS)
		s.write({'x': i, 'y': sensor_data })
		i+=1
		# delay between stream posts
		time.sleep(0.25)