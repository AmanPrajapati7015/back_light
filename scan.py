import asyncio
from bleak import BleakScanner

async def discover_led():
    print("Scanning for Bluetooth devices...")
    devices = await BleakScanner.discover()
    for d in devices:
        # if d.name and "ELK" in d.name:
        print(f"{d.name}: {d.address}")

if __name__ == "__main__":
    asyncio.run(discover_led())