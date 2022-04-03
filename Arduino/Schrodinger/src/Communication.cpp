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
}

void Communication_::loop() {
    uint32_t t1 = micros();

    bool connectedNow = radio.isChipConnected();
    if(connectedNow != connected) {
        connected = connectedNow;
        if(!connected) Display.updateDisplay(2, "Radio Disabled");
    }

    uint32_t t2 = micros();

    recent = false;
    uint8_t pipe;
    if(radio.available(&pipe)) {
        inpayload inBuf;
        uint8_t bytes = radio.getPayloadSize();
        radio.read(&inBuf, bytes);
        lastPacket = packet;
        packet = inBuf;
        recent = true;
        packetCt++;
    }

    uint32_t t3 = micros();

    uint32_t t = millis();
    // Count packets in one-second intervals
    if(t >= lastCtTime + 1000) {
        Display.updateDisplay(2, connected ? "Radio Enabled" : "Radio Disabled");
        char buf[DISPLAY_WIDTH+1];
        snprintf(buf, DISPLAY_WIDTH+1, " (%dHz)", (unsigned int) packetCt);
        Display.updateDisplay(2, buf, true);

        packetFreq = packetCt;
        packetCt = 0;
        lastCtTime = t;
    }

    uint32_t t4 = micros();
    if(t4-t1 > 100) Serial.printf("Comm time: %d\t%d\t%d\n", t2-t1, t3-t2, t4-t3);
}

bool Communication_::getConnected() {
    return connected;
}

bool Communication_::getButtonValue(uint8_t button, bool requireRecent) {
    // requireRecent is false by default
    return (recent || !requireRecent) && (Communication.packet.buttons & (1 << button));
}

bool Communication_::getButtonNewValue(uint8_t button, bool requireRecent) {
    // requireRecent is false by default
    return (recent || !requireRecent) && (Communication.packet.buttons & (1 << button))
        && !(Communication.lastPacket.buttons & (1 << button));
}

uint8_t Communication_::getAxesValue(uint8_t axis) {
    return Communication.packet.axes[axis];
}

bool Communication_::getAxesIsValue(uint8_t axis, uint8_t val, bool requireRecent) {
    // requireRecent is false by default
    return (recent || !requireRecent) && Communication.packet.axes[axis] == val;
}

bool Communication_::getAxesIsNewValue(uint8_t axis, uint8_t val, bool requireRecent) {
    // requireRecent is false by default
    return (recent || !requireRecent) && Communication.packet.axes[axis] == val
        && Communication.lastPacket.axes[axis] != val;
}
