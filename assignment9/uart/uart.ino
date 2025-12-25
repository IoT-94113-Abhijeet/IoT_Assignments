void setup() {
  Serial.begin(115200);  // Start serial communication
}

void loop() {
  Serial.println("Hello from ESP32");  // Print message to Serial Monitor
  delay(3000);  // Wait for 3 seconds
}

