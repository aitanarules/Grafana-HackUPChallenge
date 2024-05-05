#include "HardwareSerial.h"
#include "DHT.h"

#define LIGHT_SENSOR_PIN 32 // ESP32 pin GIOP27 (ADC17)
#define DHTPIN 33
#define DHTTYPE DHT11

HardwareSerial USBserial(0);
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  USBserial.begin(115200);
  dht.begin();
}

void loop() {
  // 1. Tomamos luminosidad
  int analogValue = analogRead(LIGHT_SENSOR_PIN);
  USBserial.println(analogValue);
  delay(500);

  // 2. Tomamos temperatura y humedad
  float t = dht.readTemperature();
  float h = dht.readHumidity();

  if (isnan(h) || isnan(t)) {
    t = 0;
    h = 0;
    return;
  }

  USBserial.println(t);
  USBserial.println(h);
}

