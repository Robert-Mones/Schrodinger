// File to manage communication with the controller via radio and other devices.
#ifndef Communication_h
#define Communication_h

#include "Arduino.h"
#include "Display.h"

class Communication_ {
    public:
        void setup();
        void loop();
};
extern Communication_ Communication;

#endif
