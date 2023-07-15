import subprocess, time, random
from datetime import datetime

def send_curl_every_second(sensor_id, sensor_value, interval):
    while True:
        # SEND DATA TYPE : curl -X POST -H "Content-Type: application/json" -d \
        # '{"sensor_id": 1, "date":"2023-07-03", "time":"20:04:30", "gas_level": 50}' \
        # http://192.168.70.89:9000/data-endpoint
        subprocess.run([
            'curl', '-X', 'POST', 
            '-H', 'Content-Type: application/json', 
            '-d',f'{{"{sensor_id}": 1, "date":"{datetime.now().strftime("%Y-%m-%d")}", "time":"{datetime.now().strftime("%H:%M:%S")}", "sensor_value": {sensor_value}}}', 
            'http://192.168.70.89:9000/data-endpoint'
        ])
        time.sleep(interval)  # n초 동안 대기

# 함수 실행
send_curl_every_second('sensor_id', 'sensor_value', 'interval')
