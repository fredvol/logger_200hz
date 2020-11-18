# Acceleration during parachute opening 
*2020/11/17 - fred  - v 1.0*

## Goals
The goal is to have a idea of the force apply on the mass during an EN 12491 Load test session. For that an accelerometer has been installed on the dummy mass.

## Contex
* Test done by  Para-test on 11/11/2020.
* Number of parachutes tested : 12.
* All tests has been perform at 40m/s horizontal speed.
* Sensor :  
    * WitMotion WT901SDCL. 
    * log acceleration (x,y,z) at 200 Hz with timestamp
    * Max : 16 g on each axis. ( we checked that we never exceed 16g during and opening shock , but it was reach several time during ground shock)
    * https://www.amazon.fr/gp/product/B085NWVRS2/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1
* Units:
    * Mass : Kg
    * Force : daN
    * g = 9.81 m/s2


## Overview
This is an overview of the full log .
With the index of the drop.

*Note : , right click , view image to explore all the graph*

 <figure>
    <img src="image\Figure_all.png" alt="Figure_all" style="width:100%">
    <figcaption>Fig.1 - Full log wwith index drop.</figcaption>
</figure> 

When we zoom on the first drop :
<figure>
    <img src="image\Figure_1out_modif.png" alt="Figure_1out_modif" style="width:100%">
    <figcaption>Fig.2 - Full run of drop 1.</figcaption>
</figure> 

Zoom on the opening of the first drop :
<figure>
    <img src="image\Figure_1_modif.png" alt="Figure_1_modif" style="width:100%">
    <figcaption>Fig.3 - Full run of drop 1.</figcaption>
</figure>

## Results:
This table resume all the test parameters and the calculated force :

     force [daN] = mass [kg] * max_g * g [m/s2]

| Drop Id |Mass [Kg] |Pass/Fail | Max g force [g] | Start [hh:mm:ss.s] | Force [daN]|
|-----:|-------:|-------:|:-------:|:-----------:|:--------:|
|    1 |    230 | **Pass** |  12.5  | 12:31:38.0 |  **2820**  |
|    2 |    220 |     Fail |  19    | 12:35:47.0 |  **4100**  |
|    3 |    220 |     Fail |   9.8  | 12:40:48.0 |  **2115**  |
|    4 |    220 |     Fail |   9.36 | 12:45:35.0 |  **2020**  |
|    5 |    135 | **Pass** |  13.1  | 12:52:21.0 |  **1735**  |
|    6 |    125 |     Fail |  13.7  | 12:57:08.0 |  **1680**  |
|    7 |    120 | **Pass** |  16.7  | 13:01:39.0 |  **1966**  |
|    8 |    115 |     Fail |  17.3  | 13:05:29.0 |  **1952**  |
|    9 |    100 | **Pass** |  11.7  | 13:09:01.0 |  **1148**  |
|   10 |    100 |     Fail |   9.54 | 13:12:36.0 |  **936**   |
|   11 |    100 | **Pass** |  13.1  | 13:15:58.0 |  **1285**  |
|   12 |     80 | **Pass** |  11.8  | 13:19:35.0 |  **926**   |

Note: 

* Start time is just approximative to get an idea on the full log, no precise criteria were use to set it.

## Zoom on each drop
All graph: 

<figure>
    <img src="image\Figure_1.png" alt="Figure_1" style="width:100%">
    <figcaption>Fig.4 - drop 1.</figcaption>
</figure>

<figure>
    <img src="image\Figure_2.png" alt="Figure_2" style="width:100%">
    <figcaption>Fig.5 - drop 2.</figcaption>
</figure>

<figure>
    <img src="image\Figure_3.png" alt="Figure_3" style="width:100%">
    <figcaption>Fig.6 - drop 3.</figcaption>
</figure>

<figure>
    <img src="image\Figure_4.png" alt="Figure_4" style="width:100%">
    <figcaption>Fig.7 - drop 4.</figcaption>
</figure>

<figure>
    <img src="image\Figure_5.png" alt="Figure_5" style="width:100%">
    <figcaption>Fig.8 - drop 5.</figcaption>
</figure>

<figure>
    <img src="image\Figure_6.png" alt="Figure_6" style="width:100%">
    <figcaption>Fig.9 - drop 6.</figcaption>
</figure>

<figure>
    <img src="image\Figure_7.png" alt="Figure_7" style="width:100%">
    <figcaption>Fig.10 - drop 7.</figcaption>
</figure>

<figure>
    <img src="image\Figure_8.png" alt="Figure_8" style="width:100%">
    <figcaption>Fig.11 - drop 8.</figcaption>
</figure>

<figure>
    <img src="image\Figure_9.png" alt="Figure_9" style="width:100%">
    <figcaption>Fig.11 - drop 9.</figcaption>
</figure>

<figure>
    <img src="image\Figure_10.png" alt="Figure_10" style="width:100%">
    <figcaption>Fig.12 - drop 10.</figcaption>
</figure>

<figure>
    <img src="image\Figure_11.png" alt="Figure_11" style="width:100%">
    <figcaption>Fig.13 - drop 11.</figcaption>
</figure>

<figure>
    <img src="image\Figure_12.png" alt="Figure_12" style="width:100%">
    <figcaption>Fig.14 - drop 12.</figcaption>
</figure>

**The End !**