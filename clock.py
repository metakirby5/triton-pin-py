from apscheduler.schedulers.blocking import BlockingScheduler
from rq import Queue
from .worker import conn
from .tasks import pin

SCHED = BlockingScheduler()
QUEUE = Queue(connection=conn)

@SCHED.scheduled_job('cron', day_of_week='sun', hour=0)
def weekly_pin():
  QUEUE.enqueue(pin)

if __name__ == '__main__':
  SCHED.start()