from celery import shared_task


# This task will be called from the views.py file.
# Example: example_task.delay()
@shared_task
def example_task():
    print("The task just ran.")
    return None
