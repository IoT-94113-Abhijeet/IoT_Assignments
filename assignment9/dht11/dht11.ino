#include"DHT.h"


#define DHT_PIN 4
#define DHT_TYPE  DHT11

DHT dht(DHT_PIN, DHT_TYPE);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

  dht.begin();

  Serial.println("DHT setup is done");
}

void loop() {
  float temp = dht.readTemperature();
  float humidity = dht.readHumidity();

  if (isnan(temp) || isnan(humidity)) {
    Serial.println("Failed to read from DHT sensor!");
    delay(3000);
    return;
  }

  Serial.printf("Temperature = %.1f °C, Humidity = %.1f %%\n", temp, humidity);
  delay(3000);
}










