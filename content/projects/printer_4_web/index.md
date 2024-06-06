---
title: "Printer 4 Web"
description: "Flutter companion app for printer housing."
tags: ["Flutter", "Dart", "Web", "App-Development"]
date: 2023-03-07
showTableOfContents: true
# series: ["Projects"]
# series_order: 3

cascade:
  showDate: false
  showAuthor: false
  invertPagination: true
---

{{< lead >}}
This is the flutter companion app for the [printer housing project]({{<ref "projects/printer_housing">}}). This app connects to the Raspberry Pi that runs the printer service controller software, allowing you to monitor the current temperature and print progress. Additionally, it enables control over the housing temperature and the preheating of the heatbed and nozzle. Built with Flutter, this app is compatible with both Android and web platforms.
{{< /lead >}}

<div class="backdrop-blur">
  {{< github repo="AndreasUrlberger/Printer4WebFlutterApp" >}}
</div>

## Overview
{{< youtubeLite id=QaElfKA9zng label="Printer4Web Overview">}}

## Homescreen

{{< gallery >}}
  <img src="Printer4Web_Homescreen_light.png" class="grid-w50" />
  <img src="Printer4Web_Homescreen_dark.png" class="grid-w50" />
{{< /gallery >}}

On the homescreen, you can track the print progress and watch a live video feed of the printer. When launched, the app connects to the Raspberry Pi, activates the light, and starts the video stream. You also get an estimate of the remaining print time.

<!-- In the first tab, you can track the print progress and watch a live video feed of the printer. When launched, the app connects to the Raspberry Pi, activates the light, and starts the video stream. It also displays two graphs showing the temperature history inside the housing and the heatbed. Additionally, you can view the current temperatures outside the housing and at the nozzle. -->

## Printer Information

{{< gallery >}}
  <img src="Printer4Web_Printer_Info_light.png" class="grid-w50" />
  <img src="Printer4Web_Printer_Info_dark.png" class="grid-w50" />
{{< /gallery >}}

On the printer information tab, you can view the temperature of the heatbed and nozzle, preheat or cool down the printer, or connect to the PrusaLink website.

## Configuration

{{< gallery >}}
  <img src="Printer4Web_Housing_Info_light.png" class="grid-w50" />
  <img src="Printer4Web_Print_Profiles_light.png" class="grid-w50" />
{{< /gallery >}}

On the configuration tab, you get an overview of the current temperature at the top and bottom of the housing, the outside temperature and the current fan speed. Additionally, you can easily adjust the target temperature by switching between predefined print profiles or creating a custom profile.


## History
As the name implies, this is actually the fourth iteration of the printer companion app. Initially, the app was developed for Android, but I transitioned to Flutter to enable web accessibility, allowing printer access from any device without installation. Over the years, changes in the printer housing, the Prusa Connect API, and evolving requirements prompted several reimplementations. These updates not only kept the app current but also provided opportunities to experiment with new technologies.

---
