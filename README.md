# Experimental instant camera

## Printer

Connect the thermal nano printer as follows:

| printer | RPi    |
|---------|--------|
| VH      | 5V     |
| TX      | 15 (optional) |
| RX      | 14     |
| GND     | GND    |

In `raspi-config` set Serial to True. Use `/dev/serial0` to access the printer. 
You can test it with:

```bash
stty -F /dev/serial0 9600 
echo -e "Hello world.\\n\\n\\n" > /dev/serial0
```

## Camera

See `test_opencv_camera.py` for a working example with PiCamera and OpenCV.

