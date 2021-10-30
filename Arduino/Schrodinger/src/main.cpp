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
  Communication.loop();
  Sensor.loop();
  Kinematics.loop();
  Behavior.loop();
  Control.loop();
  Display.loop();
}