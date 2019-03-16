import www.orm as orm
import asyncio
from www.models import User, Blog, Comment


async def test(loop):
    await orm.create_pool(loop=loop, host='127.0.0.1', user='root', password='123456', db='awesome')
    u = User(name='c', email='c@example.com', passwd='123456', image='about:blank')
    await u.save()
    await orm.destory_pool()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()
    # loop.run_forever()

