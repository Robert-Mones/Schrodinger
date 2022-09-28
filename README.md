# Schrodinger
3D-Printable quadrupedal robot driven by hobby servos.

<p align="center">
<img width="49%" src="https://github.com/Robert-Mones/Schrodinger/blob/main/images/renders/isometric-v117.png" alt="A Rendering of the CAD Model of Schrodinger" />
<img width="49%" src="https://github.com/Robert-Mones/Schrodinger/blob/main/images/renders/isometric-standing-v91.png" alt="A Rendering of the CAD Model of Schrodinger in a Standing Position" />
<img width="49%" src="https://github.com/Robert-Mones/Schrodinger/blob/main/images/kinematics.png" alt="A Screenshot of the Simulation Environment Running the Kinematic Model" />
<img width="49%" src="https://github.com/Robert-Mones/Schrodinger/blob/main/images/test-stand.png" alt="An Image of Schrodinger on a Test Stand" />
</p>

Hardware v2 (shown below) is being developed now, then work on control system and autonomy software will continue.
<p align="center">
<img width="100%" src="https://github.com/Robert-Mones/Schrodinger/blob/main/images/renders/isometric-hardware-v2-v50.png" alt="A Rendering of the CAD Model of Schrodinger v2 Hardware" />
</p>

## About
Features
- ~~13~~ 12 articulating joints with [standard-size high-torque hobby servo motors](https://www.amazon.com/gp/product/B097DWW6PY)
    - Each leg rotates at the knee and about two axes at the shoulder
    - ~~Articulating collar~~ Fixed collar
- On-board control system based around a [Teensy 4.1 microcontroller](https://www.pjrc.com/store/teensy41.html) operating a main control loop at 100Hz
    - Absolute orientation from a [fusion BNO055 IMU](https://www.adafruit.com/product/2472)
    - Medium-range (50-100ft), medium-bandwidth communication with a [2.4GHz NRFL01-based radio](https://www.amazon.com/gp/product/B00WG9HO6Q)
        - Bandwidth of the radio is fundamentally software-limited as only one 32-byte packet is received during every control loop
    - Servo control is offloaded to a [PCA9685-based servo driver](https://www.sunfounder.com/products/pca9685-servo-driver) and updated on every control loop
- Integrated 4S4P 18650-based battery pack using [Samsung cells](https://www.18650batterystore.com/collections/18650-batteries/products/samsung-35e) and [BMS](https://www.amazon.com/gp/product/B09QPWHWT6)
- On-board vision processing with a [JeVois vision camera](http://www.jevois.org/) and an [RGBW NeoPixel Ring](https://www.adafruit.com/product/2853) in the head
- On-board camera feed stream over WiFi with a [Raspberry Pi Zero 2 W](https://www.adafruit.com/product/5291)
- Entirely 3D-printed construction (plus some bolts & threaded inserts)

## Progress
- [x] CAD Modelling
- [ ] Simulation (On hold)
- [ ] Fabrication & Assembly (In progress)
- [ ] Electronics Development (In progress)
- [ ] Control System Development (On hold)
