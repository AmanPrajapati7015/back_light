import numpy as np
import mss
import asyncio
from bleak import BleakClient


DEVICE_ADDRESS = "D94A91E0-582F-D309-9FB2-C9E21F381D8B"
CHAR_UUID = "0000fff3-0000-1000-8000-00805f9b34fb"
greenFactor = 0.25
blueFactor = 0.15


def fast_avg_rgb():
    with mss.mss() as sct:
        # print(sct.monitors)
        monitor = sct.monitors[2]  # full screen
        sct_img = sct.grab(monitor)
        img = np.array(sct_img, dtype=np.uint8)
        b, g, r, _ = img.mean(axis=(0, 1))
        return int(r), int(g*greenFactor), int(b*blueFactor)


def get_color_command(r, g, b):
    return bytearray([0x7E, 0x00, 0x05, 0x03, r, g, b, 0x00, 0xEF])



async def main():
    async with BleakClient(DEVICE_ADDRESS) as client:
            print("Connected successfully!")
            while True:
                r, g, b = fast_avg_rgb()
                await client.write_gatt_char(CHAR_UUID, get_color_command(r,g, b), response=False)
                await asyncio.sleep(0.1)
            


asyncio.run(main())
