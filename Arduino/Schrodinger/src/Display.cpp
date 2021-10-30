#include "Arduino.h"
#include "Display.h"

Display_ Display;

void Display_::setup() {
    display.begin();
    display.setFont(u8g2_font_ncenB08_tr);
    needsUpdate = true;
}

void Display_::loop() {
    if(needsUpdate) {
        display.clearBuffer();
        for (int i = 0; i < 6; i++) {
            display.drawStr(0, 8 + (11*i), displayData[i]);
        }
        display.sendBuffer();
        Serial.println("Updated display");

        needsUpdate = false;
    }
}

void Display_::updateDisplay(int i, const char *s) {
    displayData[i] = s;
    needsUpdate = true;
}