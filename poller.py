from time import sleep

from cron_task import task

if __name__ == "__main__":
    task()
    sleep(5 * 60)
