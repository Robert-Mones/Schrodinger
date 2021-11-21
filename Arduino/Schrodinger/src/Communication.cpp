#include "Arduino.h"
#include "Communication.h"

Communication_ Communication;

void Communication_::setup() {
    Serial.begin(115200);

    radio = RF24(7, 8);
    outaddr = (const uint8_t*) "CIRO0";
    inaddr = (const uint8_t*) "CORI0";
    connected = false;

    lastCtTime = 0;
    packetCt = 0;

    if(!radio.begin()) {
        Display.updateDisplay(2, "Radio Error");
    } else {
        radio.setPALevel(RF24_PA_MAX);
        radio.setPayloadSize(sizeof(outpayload));
        radio.setRetries(5, 15);
        
        radio.openWritingPipe(outaddr);
        radio.openReadingPipe(1, inaddr);
        // Force close all pipes we don't want to read from
        for(int i = 2; i <= 5; i++) radio.closeReadingPipe(i);

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
        packetCt++;

        digitalWrite(33, inBuf.buttons);
    }

    uint32_t t = millis();
    // Count packets in one-second intervals, or if millis has overflowed
    if((t - lastCtTime) >= 1000 || t < lastCtTime) {
        char buf[DISPLAY_WIDTH+1];
        snprintf(buf, DISPLAY_WIDTH+1, "Packet rate: %dHz", (unsigned int) packetCt);
        Display.updateDisplay(3, buf);

        packetCt = 0;
        lastCtTime = t;
    }
}

bool Communication_::getConnected() {
    return connected;
}
