// File to control the robot with a range of behaviors (sitting, standing, walking, etc).
#ifndef Behavior_h
#define Behavior_h

#include "Arduino.h"

class Behavior_ {
    public:
        void setup();
        void loop();
};
extern Behavior_ Behavior;

#endif
