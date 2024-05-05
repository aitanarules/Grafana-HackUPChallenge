#include "HardwareSerial.h"

#define LIGHT_SENSOR_PIN 27 // ESP32 pin GIOP27 (ADC17)
HardwareSerial USBserial(0);

void setup() {
  USBserial.begin(115200);
}

void loop() {
  int analogValue = analogRead(LIGHT_SENSOR_PIN);
  USBserial.println(analogValue);
  delay(500);
}
