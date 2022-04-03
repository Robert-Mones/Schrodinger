// File to manage control of servo motors and other effectors.
#ifndef Control_h
#define Control_h

#include "Arduino.h"
#include <Adafruit_PWMServoDriver.h>

#include "Display.h"
#include "Sensor.h"

#define ENABLE_5V 31
#define ENABLE_6V 32

#define FAN_LEFT 36
#define FAN_RIGHT 37

#define SERVO_ENABLE 9

class Control_ {
    public:
        void setup();
        void loop();
        void writeServo(uint8_t i, float deg);
        float getServo(uint8_t i);

    private:
        Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(65, Wire1);

        bool enabled;
        int16_t servo[16]; // Populated with a pulse value for each servo
        int16_t servoMid[16] = 
            {409, 97, 277, 297, 177, 279, 437, 297,
             79, 276, 408, 297, 297, 171, 491, 297};
        bool servoInvert[16] =
            {true, false, false, false, false, true, true, false,
             false, false, true, false, false, false, true, true};
};
extern Control_ Control;

#endif
