---
title: "Tank Game"
description: "Fun little tank game with ricocheting bullets."
tags: ["C++", "Unreal Engine", "Game Dev"]
date: 2019-05-23
showTableOfContents: true
# series: ["Projects"]
# series_order: 1

cascade:
  showDate: false
  showAuthor: false
  invertPagination: true
---

{{< lead >}}
Inspired by the tank mini-game from "Wii Play", in this game the player controls a toy tank and fights against AI tanks in a small toy arena. One of the unique features of this game is that bullets can ricochet multiple times off walls. This allows for some interesting strategies and makes the game, as well as the development, more challenging. Most tanks have some special features that differentiate them from the others, like a higher bullet speed, more ricochets, or the ability to lay mines. In its current state the game is playable, but development is for now on hold due to a lack of 3D models and artisitc talent. 
{{< /lead >}}

<div class="backdrop-blur">
  {{< github repo="AndreasUrlberger/Panzerspiel" >}}
</div>

## Single Ricochet

<!-- TODO: Maybe try to get round corners for the youtube embeddings. -->
{{< youtubeLite id="SPT_SosbWIY" label="Single Ricochet Calculation" >}}

In the original game, there were only 90-degree angles, which made the ricochet calculations a little easier. In my game, I wanted to have more freedom in the level design and allow for different obstacle shapes. Because of this, I had to come up with a way to calculate the ricochets off arbitrary walls. For single ricochets, this was not too difficult, I would still do it differently, though, if I were to implement it today. In the video above, you can see those edges highlighted, which can be shot at in order to hit the target tank. You can also see, that at the time of the video, I ignored the case in which edges are partially obstructed by other obstacles. 

## Double Ricochet

{{< youtubeLite id="sz0fQOdMMW8" label="Double Ricochet Calculation" >}}
The calculation of the double ricochets is a bit more sophisticated as there are n<sup>2</sup> many combinations for n edges. This makes using ray-casts for trajectory checking unfeasible pretty quickly. For this reason, I used a multistage filtering process, where I iteratively removed unreachable edges based on various simple criterions until only a handful possible ones are left, for which a final ray-cast approach became quite performant. In the above video, you can see that this algorithm is working for 40 cubes, that is, 160 edges or 25600 edge combinations, in a fraction of a millisecond. Same as for the single ricochet approach, I would definitely change some things, if I were to do it again.

## Live Menu Screen

{{< youtubeLite id="VSqUWynSc70" label="Live Menu Screen" >}}
In this video you can see a prototype of the live menu screen. The idea was to have a menu overlay while the AI is fighting against each other in the background. As you may notice, the AI would require a lot more work and parameter tuning so that they do not instantly kill each other or the player.

## AI Failures

{{< youtubeLite id="PUL68_1q01I" label="AI Failures" >}}
The AI was probably the most challenging part of this project, sadly I never even remotely finished it before I stopped working on this project. The AI was supposed to use a more complex state machine and some kind of a 'fear-and-aggression' system, which would influence the decision making. Being in the majority would reduce the fear, being outnumbered and being shot at would increase it. The AI would then decide to either attack or fall back based on this fear level. 

In the video however, you can see one of the many failures that I encountered while working on the AI, this one regarding the pathfinding algorithm 🙃.


---
