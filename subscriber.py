import logging
import logging.config
import os
import time

import paho.mqtt.client as mqtt

logging.config.fileConfig("log.ini")
logger = logging.getLogger("console")
logger.setLevel(logging.INFO)


def on_connect(client, userdata, flags, reason_code, properties):
    """Handles MQTT connection"""
    logger.info(f"Connected with result code: {reason_code}")

    if reason_code.is_failure:
        logger.error(f"Failed to connect: {reason_code}")
        return

    subscription_list = [
        ("some/cool/#", 1),
    ]
    client.subscribe(subscription_list)


def on_message(client, userdata, message):
    """Handles incoming MQTT messages"""
    if message.retain:
        logger.info("Skipping retained message")
        return

    logger.info(message.topic)
    logger.info(message.payload)


def on_subscribe(client, userdata, mid, reason_code_list, properties):
    """Handles MQTT subscription acknowledgment"""
    for reason_code in reason_code_list:
        if reason_code.is_failure:
            logger.error(f"Subscription rejected: {reason_code}")
        else:
            logger.info(f"Subscribed with QoS: {reason_code.value}")


def on_unsubscribe(client, userdata, mid, reason_code_list, properties):
    """Handles MQTT unsubscription acknowledgment"""
    if not reason_code_list or not reason_code_list[0].is_failure:
        logger.info("Unsubscribe succeeded")
    else:
        logger.error(f"Unsubscribe failed: {reason_code_list[0]}")


if __name__ == "__main__":
    client_id = "subscriber-local"
    logger.info(f"Creating client: {client_id}")
    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2, client_id=client_id, protocol=mqtt.MQTTv311, transport="tcp")

    username = "test"
    password = "test123"

    client.username_pw_set(username=username, password=password)

    client.on_connect = on_connect
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.on_unsubscribe = on_unsubscribe

    mqtt_host = "localhost"
    mqtt_port = 1883
    logger.info(f"Connecting to {mqtt_host}:{mqtt_port}...")
    client.connect(mqtt_host, mqtt_port, keepalive=60)

    counter = 0
    client.loop_start()
    while True:
        time.sleep(0.1)
        counter += 1
        if counter % 1000 == 0:
            logger.info(f"Heartbeat: {counter}")
            counter = 0
