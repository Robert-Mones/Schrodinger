#include "Arduino.h"
#include "Control.h"

Control_ Control;

void Control_::setup() {

}

void Control_::loop() {
    if(Sensor.enableButton.pressed()) {
        enabled = !enabled;

        Serial.print("Enable button pressed -- ");
        Serial.println(enabled ? "ENABLED" : "DISABLED");
    }
}
