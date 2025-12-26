from flask import Flask, request, jsonify
import mysql.connector
import datetime
import paho.mqtt.client as mqtt

app = Flask(__name__)

# ---------- CONFIG ----------
MOISTURE_THRESHOLD = 30

MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "snehit/moisture/alert"

# ---------- MQTT SETUP ----------
mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)

# ---------- DATABASE CONNECTION ----------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="smart_agriculture"
)

cursor = db.cursor()

# ---------- FLASK ROUTE ----------
@app.route('/moisture', methods=['POST'])
def store_moisture():
    data = request.json

    sensor_id = data.get("sensor_id")
    moisture_level = data.get("moisture_level")
    timestamp = datetime.datetime.now()

    # Insert into DB
    query = """
    INSERT INTO moisture_readings (sensor_id, moisture_level, date_time)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (sensor_id, moisture_level, timestamp))
    db.commit()

    # Check threshold
    if moisture_level < MOISTURE_THRESHOLD:
        alert_msg = f"⚠️ Alert! Moisture low: {moisture_level} (Sensor: {sensor_id})"
        mqtt_client.publish(MQTT_TOPIC, alert_msg)

    return jsonify({
        "status": "success",
        "sensor_id": sensor_id,
        "moisture_level": moisture_level
    })

# ---------- RUN SERVER ----------
if __name__ == '__main__':
    app.run(debug=True)