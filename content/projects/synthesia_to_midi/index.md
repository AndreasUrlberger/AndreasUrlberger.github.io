---
title: "Synthesia to MIDI"
description: "Fun little tank game with ricocheting bullets."
tags: ["Kotlin", "OpenCV", "Computer Vision"]
date: 2021-11-25
showTableOfContents: true
# series: ["Projects"]
# series_order: 7

cascade:
  showDate: false
  showAuthor: false
  invertPagination: true
---

{{< lead >}}
Converts Synthesia YouTube piano tutorials to MIDI files using classical computer vision techniques. While the tool works well, it requires significant configuration for each video. Additionally, it can integrate hand positions from imported hand poses to add hand information to the MIDI files.
{{< /lead >}}

<div class="backdrop-blur">
  {{< github repo="AndreasUrlberger/YoutubeTutToSheet" >}}
</div>

## Project Overview

On YouTube, many piano arrangements of popular songs are either created entirely by Synthesia or have a Synthesia-like visualization added to them. Since sheet music is not always available or can be expensive, I developed a tool to convert these Synthesia videos into MIDI files. These MIDI files can then be used to create sheet music almost automatically. This project is intended for educational and personal use, as not to infringe on any copyright laws.

## Implementation Details
For this project, I utilized classical computer vision techniques to detect the piano keys and notes being played. The implementation involves the following steps:

1. **Video Loading and Frame Extraction:** Load the video and extract individual frames.

2. **Distortion Removal:** Correct camera projection distortion to straighten curved keys. This step might require manual parameter estimation depending on the video.

3. **Frame Merging:** Merge frames into a single image by cropping out unnecessary parts, such as hands, keyboard, and effects. Use vertical cross-correlation to estimate shifts between images, apply outlier rejection, and merge the images based on these shifts.

4. **Image Preprocessing:** To detect the keys effectively, the image needs preprocessing. Several methods were tested, including using different color channels and spaces, applying filters, and performing morphological operations. Ultimately, the best results were achieved by adjusting the weighted combination of color channels based on the keys' predominant color.

5. **Key Splitting:** Split the image into thin vertical strips for easier individual key detection. This step considers the varying widths of piano keys, making it necessary to split the image accurately rather than equally.

6. **Note Detection:** Detect notes by applying a threshold to the image, finding contours, and filtering them based on size and shape. Extract the notes from these contours.

7. **Optional Hand Pose Integration:** Import hand poses (if available) and map them to corresponding keys on the piano. Determine the closest finger for each note and add this information to the MIDI file, which helps notation software split the notes between hands properly.

8. **MIDI Conversion:** Convert the detected notes to MIDI by mapping their positions to corresponding piano keys. Estimate the duration of notes based on their length in the image, considering the song's tempo and time signature, which need to be set manually. Create the MIDI file using the Java Sound API.

9. **MIDI Import:** Import the MIDI file into music notation software like MuseScore for editing and printing. Depending on the song's complexity, the MIDI file might require manual adjustments.

## Note Detection
![Note Detection](note_detection.png)
This image shows what the note detection looks like. The notes are highlighted in green for the left hand and in blue for the right hand. The green and blue lines indicate where the hands are recognized at that time. You can also see the noise on the right side of the image, stemming from the visual effects that are added to the video. 


## Results and Future Work
The tool works well but requires considerable configuration for each video. It struggles with videos that have many effects, changing key colors, or inconsistent tempo. To address these limitations, I am currently developing a deep learning approach to predict notes directly from audio data rather than video. This method should ideally require less configuration, generalize better, and just generally be more useful, especially if the pianist created the arrangement by ear and thus does not have a MIDI recording to use for the Synthesia video.

---
