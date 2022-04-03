// File to provide methods of computing forward and inverse kinematics for the robot.
#ifndef Kinematics_h
#define Kinematics_h

#include "Arduino.h"

class Kinematics_ {
    public:
        void setup();
        void loop();
        
        float norm2D(float* vec);
        float norm3D(float* vec);

        float targetPos[3] = {0.055, -0.01, -0.025};
        float maxZ = -0.025;
        float minZ = -0.260;
        float maxY = 0.2;
        float minY = -0.2;
    
    private:
        float legA = 0.055;
        float legB = 0.134503;
        float legC = 0.148;
};
extern Kinematics_ Kinematics;

#endif
