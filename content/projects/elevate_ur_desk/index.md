---
title: "Elevate Ur Desk"
description: "Custom built, height adjustable desk."
tags: ["C++", "Andruino", "Embedded"]
date: 2023-01-18
# series: ["Projects"]
# series_order: 2

cascade:
  showDate: false
  showAuthor: false
  invertPagination: true
---

{{< lead >}}
This is a project that I started together with my brother, who studies mechanical engineering. The self crafted wooden structure of the desk is already finished. The software is partially done, the most fundamental features are implemented, some others will be added later on. What's still lacking is the electrical part, as we faced some issues with the gearing of the motors, giving us not enough torque to lift the desk.
{{< /lead >}}

<div class="backdrop-blur">
  {{< github repo="AndreasUrlberger/ElevateUrDesk" >}}
</div>

<!-- TODO: How to add .rounded CSS class? -->
<!-- {{< carousel images="gallery/*" interval="2500" aspectRatio="16-9" >}} -->


## Structure

The desk is mounted to a wall and uses two identical stepper motors to lift the desk. This two motor setup comes with some challenges, as the motors need to be synchronized. Additionally, the desk has two brakes on each side to ensure a safe stay in all circumstances. Each motor and brakes are controlled by a separate ESP32 microcontroller, which are connected to another ESP32 that acts as a general controller. It takes care of the synchronization of the motors and the communication with the user interface. The user interface is currently a control panel with 4 buttons and a rotary encoder, but will later also feature a display that is embedded into the wooden frame. The control panel is connected to the general controller via UART. 


## Motor Controller

...

## General Controller

...

## Control Panel
The control panel consists of 5 buttons, 1 piezo buzzer and a rotary encoder. The control panel is integrated on the  underside of the desk, allowing for easy access while hiding it from view. The panel has a complex menu system that not only allows for the up and down movement of the desk and the configuration of different profiles, but also for the control of peripherals like the LED strip around the desk and the control of spotify connect. It is connected to the general controller via UART. 

One additional useless feature is the piezo buzzer, which can be used to play simple songs or soundeffects.

## LED Matrix Controller

...

---
