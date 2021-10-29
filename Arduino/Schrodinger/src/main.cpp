#include <Arduino.h>

#include "Behavior.h"
#include "Communication.h"
#include "Control.h"
#include "Display.h"
#include "Kinematics.h"
#include "Sensor.h"

Behavior_ Behavior;
Communication_ Communication;
Control_ Control;
Display_ Display;
Kinematics_ Kinematics;
Sensor_ Sensor;

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