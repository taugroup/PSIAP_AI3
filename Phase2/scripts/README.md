## 1. air_quality_hivemq.py

The only library needed for the Python script is Paho. You can install the library with
```
$pip install paho-mqtt
```
## 2. subscribe to the topic nist/psiap/ai3/air_quality 
```
TOPIC = "nist/psiap/ai3/air_quality"
client.subscribe(topic, qos=1)
```
## 3. subscribe to other topics
Other topics could be subscribed in the same way. You just need to update the value of TOPIC.
```
TOPIC = "ONE_OF_AI3_TOPICS"
```
