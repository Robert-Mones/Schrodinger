#include "Arduino.h"
#include "Kinematics.h"
#include "Control.h"
#include <math.h>

Kinematics_ Kinematics;

void Kinematics_::setup() {

}

void Kinematics_::loop() {
    float abc = norm3D(targetPos);
    float bc = sqrt(pow(abc,2) - pow(legA,2));
    float C = acos((pow(legB,2) + pow(legC,2) - pow(bc,2)) / (2.0*legB*legC));
    float B = asin(targetPos[1] / bc) + (PI/2) - asin((legC * sin(C)) / bc);
    float abc_proj = sqrt(pow(targetPos[0],2) + pow(targetPos[2],2));
    float A = acos(legA / abc_proj) - acos(targetPos[0] / abc_proj);

    C -= 0.15;
    B -= 0.15;

    Control.writeServo(1, 180.0 * C / PI); // Knee
    Control.writeServo(8, 180.0 * C / PI);
    Control.writeServo(6, 180.0 * C / PI);
    Control.writeServo(14, 180.0 * C / PI);

    Control.writeServo(0, 180.0 * B / PI); // Shoulder
    Control.writeServo(10, 180.0 * B / PI);
    Control.writeServo(4, 180.0 * B / PI);
    Control.writeServo(13, 180.0 * B / PI);

    Control.writeServo(2, 180.0 * A / PI); // Hip
    Control.writeServo(9, 180.0 * A / PI);
    Control.writeServo(5, 180.0 * A / PI);
    Control.writeServo(15, 180.0 * A / PI);
}

float Kinematics_::norm2D(float *vec) {
    return sqrt(pow(vec[0], 2) + pow(vec[1], 2));
}

float Kinematics_::norm3D(float *vec) {
    return sqrt(pow(vec[0], 2) + pow(vec[1], 2) + pow(vec[2], 2));
}
