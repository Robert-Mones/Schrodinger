// File to manage displaying information on the OLED display, LEDs, and other data-presenting media.
#ifndef Display_h
#define Display_h

#include "Arduino.h"
#include <U8g2lib.h>
#include <Wire.h>

class Display_ {
    public:
        void setup();
        void loop();

        void updateDisplay(int i, const char *s);
    
    private:
        U8G2_SSD1306_128X64_NONAME_F_HW_I2C display
            = U8G2_SSD1306_128X64_NONAME_F_HW_I2C(U8G2_R0, U8X8_PIN_NONE);
        
        const char *displayData[6] = {"--", "--", "--", "--", "--", "--"};
        bool needsUpdate;
};
extern Display_ Display;

#endif
