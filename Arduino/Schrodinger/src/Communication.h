// File to manage communication with the controller via radio and other devices.
#ifndef Communication_h
#define Communication_h

#include "Arduino.h"
#include "Display.h"
#include "SPI.h"
#include "RF24.h"

class Communication_ {
    public:
        void setup();
        void loop();

        bool getConnected();

        // These structs must have same size <= 32 bytes
        struct outpayload { // 20 bytes (20 actual)
            uint8_t data[20];
        };
        struct inpayload { // 19 bytes (20 actual)
            uint16_t touch[2];
            uint16_t buttons;
            int16_t accel[3];
            uint8_t axes[7];
        };
    
    private:
        RF24 radio = RF24(7, 8); // 10 MHz SPI communication
        uint8_t outaddr[3] = {0, 0, 1};
        uint8_t inaddr[3] = {0, 0, 0};
        uint8_t address[2][6] = {"1Node", "2Node"};
        bool connected = false;
};
extern Communication_ Communication;

#endif
