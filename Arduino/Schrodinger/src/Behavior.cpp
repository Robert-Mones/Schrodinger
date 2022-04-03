#include "Arduino.h"
#include "Behavior.h"
#include "Communication.h"
#include "Control.h"

Behavior_ Behavior;

void Behavior_::setup() {
    servoSelect = 0;
}

void Behavior_::loop() {
    if(Communication.getAxesNewValue(6, 2, true)) {
        servoSelect++;
        servoSelect = servoSelect % 16;
    } else if(Communication.getAxesNewValue(6, 6, true)) {
        servoSelect--;
        servoSelect = servoSelect % 16;
    } else if(Communication.getAxesNewValue(6, 0, true)) {
        Control.writeServo(servoSelect, Control.getServo(servoSelect) + 0.5);
    } else if(Communication.getAxesNewValue(6, 4, true)) {
        Control.writeServo(servoSelect, Control.getServo(servoSelect) - 0.5);
    }
}
