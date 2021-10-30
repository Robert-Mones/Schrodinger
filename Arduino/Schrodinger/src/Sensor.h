// File to manage reading and processing data from the IMU, JeVois, and other sensors on the robot.
#ifndef Sensor_h
#define Sensor_h

#include "Arduino.h"
#include <Bounce2.h>
#include "Display.h"

#define ENABLE_BUTTON 31

class Sensor_ {
    public:
        void setup();
        void loop();
    
        Button enableButton = Button();
};
extern Sensor_ Sensor;

#endif
