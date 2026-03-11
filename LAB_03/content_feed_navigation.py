class StoryNode:
    def __init__(self, story_id, user_id, content_preview, timestamp):
        self.story_id = story_id
        self.user_id = user_id
        self.content_preview = content_preview
        self.timestamp = timestamp
        self.views = 0
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.size = 0

    def add_story(self, node):
        if self.head is None:
            self.head = self.tail = self.current = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1

    def move_forward(self):
        if self.current and self.current.next:
            self.current = self.current.next
        return self.current

    def move_backward(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
        return self.current

    def jump_to(self, story_id):
        temp = self.head
        while temp:
            if temp.story_id == story_id:
                self.current = temp
                return temp
            temp = temp.next
        return None

    def track_view(self):
        if self.current:
            self.current.views += 1

    def most_viewed(self):
        temp = self.head
        max_story = temp
        while temp:
            if temp.views > max_story.views:
                max_story = temp
            temp = temp.next
        return max_story

feed = DoublyLinkedList()

feed.add_story(StoryNode(1, 101, "Morning Coffee", "10:00"))
feed.add_story(StoryNode(2, 102, "Workout Complete", "11:00"))
feed.add_story(StoryNode(3, 103, "Sunset Photo", "18:00"))

feed.jump_to(2)
feed.track_view()
feed.track_view()

feed.jump_to(3)
feed.track_view()

print("Most viewed:", feed.most_viewed().content_preview)