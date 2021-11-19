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

  Serial.print("outpayload size: ");
  Serial.println(sizeof(Communication_::outpayload));
  Serial.print("inpayload size: ");
  Serial.println(sizeof(Communication_::inpayload));
}

void loop() {
  Communication.loop();
  Sensor.loop();
  Kinematics.loop();
  Behavior.loop();
  Control.loop();
  Display.loop();
}