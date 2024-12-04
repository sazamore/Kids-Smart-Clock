# Kids-Smart-Clock
It's a smart clock...for kids.
This repository is for skilled programmers to reproduce this product. It is a code repository, not a step-by-step instructional. It does not include OS installation or troubleshooting.

## System
Intended for a Raspberry Pi 4 and later. Prototype has:
* Raspberry Pi 4                                              $35
* Monitor: 8" Portable Monitor (JINSWY)                       $50
* Camera: Raspberry Pi Camera Module 3 Wide PiNOIR            $35
* Wi-Fi adaptor (TBD)
* AC Power Adaptor (TBD)

## Required libraries
* --Pillow--
* Pygame (for display)
* google-auth (for Google Photos access)
* google-auth-oauthlib
* google-auth-httplib2
* opencv (for movement, face detection)
* [eSpeak](https://www.dexterindustries.com/howto/make-your-raspberry-pi-speak/) (Text To Speech enging)

## APIs
* National Weather Service
* [HTTP API](https://rhasspy.readthedocs.io/en/latest/reference/#http-api) (for [Rhasspy](https://rhasspy.readthedocs.io/en/latest/) voice commands)
* [SoundCloud](https://developers.soundcloud.com/docs/api/guide) (for white noise generation)

## Display
Displays background image and clockface with weather and current temperature. 
Will show upcoming weather (next 12 hr period) uponn request. 
Will cycle through Google Photos album; will change albums on request.
Will dim and shut off based on time and light levels from camera. (Goal: LEDs on back/bottom of clock)
Menu is controlled via pushbuttons on monitor.

## Code
[REPL.it Graphic Testbed](https://replit.com/@theedoctaz/FlusteredQuaintSpool#main.py) (currently Time & Weather)
Next:
- Google Photos integration
- Main script
- Monitor button programming (Menu?)
- SoundCloud script (search and loop through ambient noise albums like [this one](https://soundcloud.com/soundeffectszone/sets/new-york-city-soundscape))
- Rhasspy integration
- OpenCV lighting detection
