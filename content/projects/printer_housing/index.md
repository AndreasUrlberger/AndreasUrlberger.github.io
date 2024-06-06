---
title: "Printer Housing"
description: "Temperature control and monitoring of 3D printer."
tags: ["C++", "Embedded", "Raspberry Pi"]
date: 2021-08-30
showTableOfContents: true
# series: ["Projects"]
# series_order: 2

cascade:
  showDate: false
  showAuthor: false
  invertPagination: true
---

{{< lead >}}
This project was a collaborative effort with my brother. We built a housing for our 3D printer that includes a Raspberry Pi Zero, three temperature sensors, a fan, a light, a webcam, buttons, and a small display. The Raspberry Pi runs my software, which manages the housing temperature and monitors print progress. The software also offers a simple API, which the [Flutter companion app]({{<ref "projects/printer_4_web">}}) connects to.
{{< /lead >}}

<div class="backdrop-blur">
  {{< github repo="AndreasUrlberger/PrinterServiceController" >}}
</div>

![Printer Housing](printer_housing.jpg)
<!-- ![Printer Housing](printer_housing_2.jpg) -->

## Temperature Control
With the companion app, users can create temperature profiles for specific filaments. Each profile includes a target temperature and a name. Using the app or the housing buttons, one can select a profile and initiate temperature control. The software adjusts the temperature inside the housing by considering the inside, outside, and target temperatures. To lower the temperature, the fan is activated; to raise it, the fan is turned off. An air filter is also included for the fan to prevent dust from entering the housing and to keep the outside air free of particles.

## Monitoring
When someone connects to the API, the software turns on the light, activates the webcam, and starts streaming the video feed. This enables users to monitor print progress from anywhere and ensure everything is proceeding smoothly. If a print fails, the user can quickly stop it using the Prusa Connect API.

## Control Panel

![Control Panel of Printer Housing](printer_display.jpg)
The control panel allows users to switch between temperature profiles, start and stop temperature control, and check the current temperature inside the housing. The large button on the left toggles the light on and off.

---
