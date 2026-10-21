import asyncio
from bleak import BleakClient
import colorsys

DEVICE_ADDRESS = "D94A91E0-582F-D309-9FB2-C9E21F381D8B"
CHAR_UUID = "0000fff3-0000-1000-8000-00805f9b34fb"
steps = 300


def get_color_command(r, g, b):
    return bytearray([0x7E, 0x00, 0x05, 0x03, r, g, b, 0x00, 0xEF])



async def main():
    async with BleakClient(DEVICE_ADDRESS) as client:


        r = 255
        g = int(255*0.25)
        # g = 0
        b = int(255*0.15)

        # for i in range(100):
        #     b_ = int((i/100) * b)
        #     await client.write_gatt_char(CHAR_UUID, get_color_command(r, g, b_), response=False)
        #     print(i)
        #     await asyncio.sleep(0.3)

        await client.write_gatt_char(CHAR_UUID, get_color_command(r, g, b), response=False)
        await asyncio.sleep(0.3)

        
        # print("Connected successfully!")

        # while True:
        #     for i in range(steps):
        #         hue = i / steps
        #         r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)  
        #         r, g, b = int(r * 255), int(g * 255), int(b * 255)

                # await client.write_gatt_char(CHAR_UUID, get_color_command(r,g,b), response=False)


        



asyncio.run(main())

# Run the async loop