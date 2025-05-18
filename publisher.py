import json
import logging
import logging.config
import os
import ssl

import paho.mqtt.client as mqtt
from paho.mqtt.packettypes import PacketTypes
from paho.mqtt.properties import Properties

logging.config.fileConfig("log.ini")
logger = logging.getLogger("console")
logger.setLevel(logging.INFO)

if __name__ == "__main__":
    client_id = "publisher-local"
    logger.info(f"Creating client: {client_id}")
    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2, client_id=client_id, protocol=mqtt.MQTTv311, transport="tcp")

    username = "test"
    password = "test123"

    client.username_pw_set(username=username, password=password)

    mqtt_host = "localhost"
    mqtt_port = 1883
    logger.info(f"Connecting to {mqtt_host}:{mqtt_port}...")
    client.connect(mqtt_host, mqtt_port, keepalive=60)
    client.loop_start()

    _topic = f"some/cool/topic"
    json_obj = {"hello": "world"}

    publish_properties = Properties(PacketTypes.PUBLISH)
    msg_info = client.publish(_topic, json.dumps(json_obj), qos=1, properties=publish_properties)
    msg_info.wait_for_publish()
    client.disconnect()
