#include <Arduino.h>

#include "Behavior.h"
#include "Communication.h"
#include "Control.h"
#include "Display.h"
#include "Kinematics.h"
#include "Sensor.h"

#define LOOP_TIME 10000 // Minimum time (us) to wait between control loops

void setup() {
    Communication.setup();
    Sensor.setup();
    Kinematics.setup();
    Behavior.setup();
    Control.setup();
    Display.setup();

    Wire1.setClock(400000);
}

void loop() {
    uint32_t t1 = micros();

    Communication.loop();
    uint32_t t2 = micros();
    // if(t2-t1 > 75)
    //     Serial.printf("Long Communication loop: %d us\n", t2-t1);

    Sensor.loop();
    uint32_t t3 = micros();
    // if(t3-t2 > 3350)
    //     Serial.printf("Long Sensor loop:        %d us\n", t3-t2);

    Behavior.loop();
    uint32_t t4 = micros();
    // if(t4-t3 > 75)
    //     Serial.printf("Long Kinematics loop:    %d us\n", t4-t3);

    Kinematics.loop();
    uint32_t t5 = micros();
    // if(t5-t4 > 75)
    //     Serial.printf("Long Behavior loop:      %d us\n", t5-t4);

    Control.loop();
    uint32_t t6 = micros();
    // if(t6-t5 > 2350)
    //     Serial.printf("Long Control loop:       %d us\n", t6-t5);

    Display.loop();
    uint32_t t7 = micros();
    // if(t7-t6 > 75)
    //     Serial.printf("Long Display loop:       %d us\n", t7-t6);

    Serial.printf("%.2f V  %.2f A  %d us  %d Hz", Sensor.battVoltage/1000.0, Sensor.battCurrent/1000.0, t7-t1, Communication.packetFreq);
    Serial.printf("  %d  [%.3f, %.3f, %.3f]", Communication.getAxesValue(1), Kinematics.targetPos[0], Kinematics.targetPos[1], Kinematics.targetPos[2]);
    for(uint8_t i = 0; i < 16; i++) {
        Serial.printf(" |%d %.1f|", i, Control.getServo(i));
    }
    Serial.printf("\n");

    // Wait a specified amount of time before continuing to the next iteration
    while(micros() < t1 + LOOP_TIME);
}