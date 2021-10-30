#include "Arduino.h"
#include "Control.h"

Control_ Control;

void Control_::setup() {
    enabled = false;
    Display.updateDisplay(0, "Status: DISABLED");
}

void Control_::loop() {
    if(Sensor.enableButton.pressed()) {
        enabled = !enabled;
        Display.updateDisplay(0, enabled ? "Status: ENABLED" : "Status: DISABLED");

        Serial.print("Enable button pressed -- ");
        Serial.println(enabled ? "ENABLED" : "DISABLED");
    }
}
