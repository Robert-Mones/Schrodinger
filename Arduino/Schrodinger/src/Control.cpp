#include "Arduino.h"
#include "Control.h"
#include "Communication.h"

Control_ Control;

void Control_::setup() {
    enabled = false;
    for(int i = 0; i < 16; i++) {
        servo[i] = servoMid[i];
    }

    Display.updateDisplay(0, "Status: DISABLED");

    pwm.begin();
    pwm.setOscillatorFrequency(27000000);
    pwm.setPWMFreq(50);

    pinMode(ENABLE_5V, OUTPUT);
    pinMode(ENABLE_6V, OUTPUT_OPENDRAIN);
    pinMode(FAN_LEFT, OUTPUT);
    pinMode(FAN_RIGHT, OUTPUT);
}

void Control_::loop() {
    if(Sensor.enableButton.pressed() || Communication.getButtonNewValue(12, true)) {
        enabled = !enabled;
        Display.updateDisplay(0, enabled ? "Status: ENABLED" : "Status: DISABLED");

        Serial.print("Enable button pressed -- ");
        Serial.println(enabled ? "ENABLED" : "DISABLED");
    }

    for(int i = 0; i < 16; i++) {
        pwm.setPWM(i, 0, servo[i]);
    }
    
    digitalWrite(ENABLE_6V, !enabled);
    digitalWrite(FAN_LEFT, enabled);
    digitalWrite(FAN_RIGHT, enabled);
}

void Control_::writeServo(uint8_t i, float deg) {
    int16_t inv = servoInvert[i] ? -1 : 1;
    int16_t pulse = inv * roundf(2.0 * deg) + servoMid[i];
    servo[i] = pulse;
}

float Control_::getServo(uint8_t i) {
    int16_t inv = servoInvert[i] ? -1 : 1;
    return (float) (inv * (servo[i] - servoMid[i])) / 2.0;
}
