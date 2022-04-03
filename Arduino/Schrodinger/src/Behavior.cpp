#include "Arduino.h"
#include "Behavior.h"
#include "Communication.h"
#include "Kinematics.h"

Behavior_ Behavior;

void Behavior_::setup() {
    
}

void Behavior_::loop() {
    float yInput = (float) Communication.getAxesValue(0);
    float targetY = ((Kinematics.maxY - Kinematics.minY) * yInput / 255.0) + Kinematics.minY;    
    
    float zInput = (float) Communication.getAxesValue(1);
    float targetZ = ((Kinematics.maxZ - Kinematics.minZ) * zInput / 255.0) + Kinematics.minZ;

    Kinematics.targetPos[1] = targetY;
    Kinematics.targetPos[2] = targetZ;
}
