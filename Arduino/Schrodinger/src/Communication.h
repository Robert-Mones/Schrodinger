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
        bool getButtonValue(uint8_t button, bool requireRecent = false);
        bool getButtonNewValue(uint8_t button, bool requireRecent = false);
        uint8_t getAxesValue(uint8_t axis);
        bool getAxesIsValue(uint8_t axis, uint8_t val, bool requireRecent = false);
        bool getAxesIsNewValue(uint8_t axis, uint8_t val, bool requireRecent = false);

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
        
        bool recent;
        inpayload packet;
        inpayload lastPacket;
        uint32_t packetFreq;
    
    private:
        RF24 radio; // 10 MHz SPI communication
        const uint8_t *outaddr; // Controller in, robot out
        const uint8_t *inaddr;  // Controller out, robot in
        bool connected;

        uint32_t lastCtTime;
        uint32_t packetCt;
};
extern Communication_ Communication;

#endif
