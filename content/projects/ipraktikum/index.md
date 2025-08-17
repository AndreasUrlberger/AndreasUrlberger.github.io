---
title: "Roomsgen - iPraktikum"
description: "Personalized AI Furniture Recommendation System."
tags: ["Swift", "Python", "iOS", "Deep Learning", "LLM", "Student Project", "AR"]
date: 2025-02-15
showTableOfContents: true
# series: ["Projects"]
# series_order: 2

cascade:
  showDate: false
  showAuthor: false
  invertPagination: true
---


{{< lead >}}
Roomsgen is a mobile application that combines augmented reality and artificial intelligence to assist users in designing their living spaces. By scanning a room and capturing user preferences, the app generates personalized furniture recommendations and visualizes them directly in AR, enabling confident and informed interior design decisions.  
{{< /lead >}}


## iPraktikum

Roomsgen was developed as part of the iPraktikum course at TUM, an industry-driven practical centered around innovation in mobile applications. Each semester, 8–12 companies provide real-world problem statements, and interdisciplinary student teams work closely with them to deliver functional applications under real deadlines.  

The course emphasizes agile software engineering practices, including requirements engineering, usability engineering, object-oriented design, continuous integration, and continuous delivery. Teams also gain hands-on experience with modern development frameworks such as Swift, SwiftUI, and asynchronous programming paradigms.  

Working within this framework, our team collaborated with the industry partner [msg](https://www.msg.group/de/) to design and implement Roomsgen - a system that merges AR-based room scanning with AI-driven design recommendations. The project not only provided valuable technical experience but also simulated professional collaboration with a real client.  


## Goal

The primary goal of Roomsgen was to simplify the interior design process through AI-powered assistance. We aimed to develop an app that could:  

- Accurately capture the layout and dimensions of a room through AR scanning and capture exact locations and dimensions of windows and doors.  
- Collect user style preferences (e.g., styles, materials, color schemes) either manually or through automatic style recognition of the existing furniture.  
- Leverage AI models (LLMs and deep learning architectures) to generate realistic and personalized furniture arrangements.  
- Provide augmented reality visualization so users could preview the proposed design directly in their own space.  

In essence, the project sought to merge usability, cutting-edge AI, and AR to create a seamless end-to-end experience that helps users make confident design decisions before purchasing furniture.  


## Implementation


### Front-End

The front-end of Roomsgen was built using SwiftUI, Apple’s modern declarative UI framework. While much of the implementation followed standard iOS development practices, the main challenge lay in the integration of Apple’s RoomPlan framework. RoomPlan’s AR-based scanning had to be seamlessly connected with our custom pipeline for processing room layouts. The iOS client was responsible for scanning, user interaction, and AR visualization, while all AI-powered recommendations were requested from a server backend.  


### Room Scanning

For capturing the physical environment, we employed RoomPlan, Apple’s ARKit-based room scanning framework. The raw scans were processed into a simplified, top-down representation of the room, aligned with axes for consistency. This representation captured not only the dimensions and layout, but also key structural elements such as doors, windows, and existing furniture. The resulting compact format was then transmitted to the backend, where it served as the basis for dataset queries and AI-driven design recommendations.  


### Dataset Generation

To support training and inference of our AI models, we worked with large-scale 3D indoor scene datasets. We requested access to the 3D-FRONT and 3D-FUTURE datasets from [Alibaba](https://tianchi.aliyun.com/specials/promotion/alibaba-3d-scene-dataset), which contain thousands of high-quality, semantically annotated furniture models and room layouts.  

On the server side, the models were preprocessed and converted into USDZ format, making them compatible with ARKit for visualization once returned to the client. Additionally, we extracted dominant color palettes from each furniture object, which served as features for style matching and user preference alignment. This preprocessing pipeline ensured that the dataset could be directly integrated into both recommendation algorithms and iOS visualization.  


### LLM Design Recommendations

On the backend, we experimented with LayoutGPT, a large language model specialized for spatial reasoning and room layout generation. Given the room dimensions and user style preferences, LayoutGPT produced furniture arrangement proposals that served as a first-pass design.  

Our workflow adopted a multi-stage and multi-modal approach, where text-based reasoning about style compatibility was combined with geometric validation of the proposed layout to ensure realistic and usable designs. The results were then packaged and sent back to the iOS client for AR visualization. This division of labor kept the phone lightweight while allowing for more computationally intensive reasoning on the server.  


### SceneFormer Design Recommendations

Beyond LLM-based suggestions, the backend also integrated SceneFormer, a transformer-based generative model for indoor scene synthesis. SceneFormer predicts objects sequentially, placing items such as beds, tables, or lamps while simultaneously estimating their positions, orientations, and dimensions. By leveraging self-attention, it learns how objects naturally relate to each other (e.g., chairs near tables, lamps near sofas), making its outputs both structurally coherent and visually realistic.  

Since the original model was trained on the now-unavailable SUNCG dataset, we adapted the architecture to train on 3D-FUTURE, ensuring compatibility with our dataset pipeline. Once generated, the arrangements were transmitted back to the iOS app, where they were visualized in AR, enabling users to immediately see the recommendations in their own space.  

## Results

The implementation actually went pretty well, except for way too many nightshifts. In the end we manage to implement all features as planned and on time.

In below video you can see some of the features of the app. Sadly I don't have a better quality version, sorry for that.

{{< youtubeLite id="bjEvUMey0xA" label="Demo of Roomsgen" >}}

In our final presentation we went for a no-fake live-demo of our app, i.e. nothing was pre-recorded or staged, which of course lead to the worst design result we ever got. You can find the recording of the live demo on the iPraktikum's [website](https://aet.cit.tum.de/projects/courses/ipraktikum/24w/msg/).


---
