# octoprint-stream-overlay
A source file for an OBS Studio browser source that pulls Octoprint info and a webcam stream into a single page.

## Installation
1. Place overlay.html into 'oprint/lib/python2.7/site-packages/octoprint/static/overlay.html' of your Octoprint directory.
2. https://$OCTOPRINT/static/overlay.html?baseurl=https://$OCTOPRINT/ to verify that it works.
3. Add the above URL to a Browser source in OBS Studio. Make sure to set the browser size to 1920x1080.

## Thumbnails
For the thumbnail generation, you need to enable thumbnail in your PrusaSlicer profile for your printer.
1. Open PrusaSlicer.
2. Go to Help -> Show Configuration Folder
3. Open "printer"
4. Open your custom printer profile
5. Add "thumbnails = thumbnails = 16x16,220x124,480x360" near line 68
6. Install the "PrusaSlicer Thumbnails" plugin for Octoprint https://github.com/jneilliii/OctoPrint-PrusaSlicerThumbnails

## Caveats
This overlay was written to be exactly 1920x1080 canvas size in OBS Studio. 

The camera feed is explicitly 4:3 for the taller FOV mode of the Raspberry Pi Cam V2.
I'm running my raspi cam V2 at 1640x1232 30FPS, which has the full FOV of the sensor.
The camera image is scaled to 1440px wide, which results in some of the vertical image being scaled past the viewport.
https://picamera.readthedocs.io/en/release-1.12/fov.html

The information sidebar is 480px wide. The thumbnail image is 4:3 at 480x360.
