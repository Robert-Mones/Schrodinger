// File to manage control of servo motors and other effectors.
#ifndef Control_h
#define Control_h

#include "Arduino.h"
#include "Display.h"
#include "Sensor.h"

class Control_ {
    public:
        void setup();
        void loop();

    private:
        bool enabled;
};
extern Control_ Control;

#endif
