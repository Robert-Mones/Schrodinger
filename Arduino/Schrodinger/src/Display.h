// File to manage displaying information on the OLED display, LEDs, and other data-presenting media.
#ifndef Display_h
#define Display_h

#include "Arduino.h"
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Fonts/FreeMonoBold9pt7b.h>
#include <TeensyThreads.h>

#define DISPLAY_WIDTH 21
#define DISPLAY_TIME 50

class Display_ {
    public:
        void setup();
        void loop();

        void updateDisplay(int i, const char *s, bool append = false);
    
    private:
        Adafruit_SSD1306 display = Adafruit_SSD1306(128, 64, &Wire1, -1);
        
        char displayData[6][DISPLAY_WIDTH+1] = {"--", "--", "--", "--", "--", "--"};
        bool needsUpdate;
        uint32_t lastUpdate;

        void writeDisplay();
};
extern Display_ Display;

#endif
