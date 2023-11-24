import asyncio
from SyncInAsync import SyncInAsync

async def main():
    AsyncImages = SyncInAsync()


    # -- METHOD 1:
    #create an Async IO Task
    task = AsyncImages.Wrap(func = GenerateImage, AD_IMG_DATA = {'OFFER': [['https://tr.rbxcdn.com/358b33371dada05e1cd5b14a654aa59a/420/420/Hat/Png', 'https://tr.rbxcdn.com/6a5c38ecedfcefc5e79f292080797596/420/420/Hat/Png'], 10, 35009], 'REQUEST': [['https://tr.rbxcdn.com/8f62abaf50334be5ea1d08040ba35152/420/420/Hat/Png'], 12, 50000]})

    # other stuff here
  
    await task
  
    # other stuff here
    print(AsyncImages.result)


    # -- METHOD 2:
    result = await AsyncImages.Call(func = GenerateImage, AD_IMG_DATA = {'OFFER': [['https://tr.rbxcdn.com/358b33371dada05e1cd5b14a654aa59a/420/420/Hat/Png', 'https://tr.rbxcdn.com/6a5c38ecedfcefc5e79f292080797596/420/420/Hat/Png'], 10, 35009], 'REQUEST': [['https://tr.rbxcdn.com/8f62abaf50334be5ea1d08040ba35152/420/420/Hat/Png'], 12, 50000]})

    print(result)
    # OR
    print(AsyncImages.result)


asyncio.run(main())
