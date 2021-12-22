#include <Arduino.h>

#include "Behavior.h"
#include "Communication.h"
#include "Control.h"
#include "Display.h"
#include "Kinematics.h"
#include "Sensor.h"

void setup() {
  Communication.setup();
  Sensor.setup();
  Kinematics.setup();
  Behavior.setup();
  Control.setup();
  Display.setup();
}

void loop() {
  uint32_t t1 = micros();

  Communication.loop();
  Sensor.loop();
  Kinematics.loop();
  Behavior.loop();
  Control.loop();
  Display.loop();

  uint32_t t2 = micros();
  if(t2-t1 > 75) Serial.printf("Long loop time: %d us\n", t2-t1);
}