#include "Arduino.h"
#include "Communication.h"

Communication_ Communication;

void Communication_::setup() {
    Serial.begin(115200);

    radio = RF24(7, 8);
    outaddr = (const uint8_t*) "CIRO0";
    inaddr = (const uint8_t*) "CORI0";
    connected = false;

    if(!radio.begin()) {
        Display.updateDisplay(2, "Radio Error");
    } else {
        radio.setPALevel(RF24_PA_MAX);
        radio.setPayloadSize(sizeof(outpayload));
        radio.setRetries(5, 15);
        
        radio.openWritingPipe(outaddr);
        radio.openReadingPipe(1, inaddr);
        radio.startListening();

        connected = radio.isChipConnected();
        Display.updateDisplay(2, connected ? "Radio Enabled" : "Radio Disabled");
    }

    Display.updateDisplay(3, "No Packets Recieved");
}

void Communication_::loop() {
    bool connectedNow = radio.isChipConnected();
    if(connectedNow != connected) {
        connected = connectedNow;
        Display.updateDisplay(2, connected ? "Radio Enabled" : "Radio Disabled");
    }

    uint8_t pipe;
    if(radio.available(&pipe)) {
        inpayload inBuf;
        uint8_t bytes = radio.getPayloadSize();
        radio.read(&inBuf, bytes);
        
        char buf[DISPLAY_WIDTH+1];
        snprintf(buf, DISPLAY_WIDTH+1, "Received: 0x%x", inBuf.buttons);
        Display.updateDisplay(3, buf);

        digitalWrite(33, inBuf.buttons);
    }
}

bool Communication_::getConnected() {
    return connected;
}
