#include "Arduino.h"
#include "Communication.h"

Communication_ Communication;

void Communication_::setup() {
    Serial.begin(115200);
    
    Display.updateDisplay(2, "IP Addr: 192.168.0.12");
}

void Communication_::loop() {
}
