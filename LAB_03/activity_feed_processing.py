from collections import deque

class ActivityStack:
    def __init__(self):
        self.stack = []

    def push(self, activity):
        self.stack.append(activity)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

    def peek(self):
        if self.stack:
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display_recent(self, n):
        return self.stack[-n:]

class NotificationQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, notification):
        self.queue.append(notification)

    def dequeue(self):
        if self.queue:
            return self.queue.popleft()
        return None

    def front(self):
        if self.queue:
            return self.queue[0]
        return None

    def size(self):
        return len(self.queue)

    def display_pending(self):
        return list(self.queue)

    def priority_enqueue(self, notification):
        self.queue.appendleft(notification)

class FeedProcessor:
    def __init__(self):
        self.recent_activities = ActivityStack()
        self.notification_queue = NotificationQueue()
        self.processed_log = deque()

    def process_incoming(self):
        notif = self.notification_queue.dequeue()
        if notif:
            self.recent_activities.push(notif)

    def batch_process(self, k):
        for _ in range(k):
            self.process_incoming()

    def clear_history(self):
        while not self.recent_activities.is_empty():
            self.processed_log.append(self.recent_activities.pop())

    def get_stats(self):
        return {
            "recent_stack": self.recent_activities.size(),
            "notification_queue": self.notification_queue.size(),
            "processed_log": len(self.processed_log)
        }

processor = FeedProcessor()

processor.notification_queue.enqueue("New follower")
processor.notification_queue.enqueue("New like")
processor.notification_queue.enqueue("New comment")

processor.process_incoming()

print(processor.recent_activities.stack)
print(processor.notification_queue.display_pending())

