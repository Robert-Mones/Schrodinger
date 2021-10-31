#include "Arduino.h"
#include "Sensor.h"

Sensor_ Sensor;

void Sensor_::setup() {
    enableButton.attach(ENABLE_BUTTON, INPUT_PULLUP);
    enableButton.interval(10);
    enableButton.setPressedState(LOW);
    
    Display.updateDisplay(1, "Batt Voltage: 13.56V");
}

void Sensor_::loop() {
    enableButton.update();
}
