
import time
import asyncio
from collections import namedtuple
from apis.order import *
from apis.cancel_order import *
import sys


def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)

Service = namedtuple('Service', ('class_name', 'method'))

SERVICES = (
    Service("GetOrders", "Orders"),
    Service("GetCancelOrders", "Orders"),
)


async def fetch_data(service):
    start = time.time()
    print('Fetching data from {}'.format(service.class_name))
    try:
        json_response =  await getattr(str_to_class(service.class_name), service.method)()
    except:
        return '{} is unresponsive'.format(service.class_name)

    return '{} finished with result: {}, took: {:.2f} seconds'.format(
        service.class_name, json_response, time.time() - start)


async def main():
    futures = [fetch_data(service) for service in SERVICES]
    done, _ = await asyncio.wait(futures)

    for future in done:
        print(future.result())


asyncio.run(main())