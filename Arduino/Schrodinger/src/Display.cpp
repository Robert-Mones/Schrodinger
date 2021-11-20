#include "Arduino.h"
#include "Display.h"

Display_ Display;

void Display_::setup() {
    display.begin();
    display.setFont(u8g2_font_ncenB08_tr);

    needsUpdate = true;
    lastUpdate = 0;
}

void Display_::loop() {
    uint32_t t = millis();
    if(needsUpdate && (((t - lastUpdate) >= DISPLAY_TIME) || t < lastUpdate)) {
        display.clearBuffer();
        for (int i = 0; i < 6; i++) {
            display.drawStr(0, 8 + (11*i), displayData[i]);
        }
        display.sendBuffer();

        needsUpdate = false;
        lastUpdate = t;
    }
}

// append is false by default
void Display_::updateDisplay(int i, const char *s, bool append) {
    if(append) {
        int8_t len = DISPLAY_WIDTH - strlen(displayData[i]);
        strncat(displayData[i], s, len);
    } else {
        strncpy(displayData[i], s, DISPLAY_WIDTH);
        displayData[i][DISPLAY_WIDTH] = 0;
    }
    needsUpdate = true;
}