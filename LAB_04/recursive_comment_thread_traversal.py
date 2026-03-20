class CommentNode:
    def __init__(self, comment_id, user_id, content, timestamp, likes=0):
        self.comment_id = comment_id
        self.user_id = user_id
        self.content = content
        self.timestamp = timestamp
        self.likes = likes
        self.replies = []

def add_reply(parent, reply_node):
    parent.replies.append(reply_node)

def count_comments(node):
    total = 1
    for reply in node.replies:
        total += count_comments(reply)
    return total

def search_by_user(node, user):
    result = []
    if node.user_id == user:
        result.append(node)

    for reply in node.replies:
        result.extend(search_by_user(reply, user))

    return result

def delete_comment(parent, comment_id):
    for reply in parent.replies:
        if reply.comment_id == comment_id:
            parent.replies.remove(reply)
            return True
        if delete_comment(reply, comment_id):
            return True
    return False

def display_thread(node, level=0):
    print("  " * level + f"{node.user_id}: {node.content}")
    for reply in node.replies:
        display_thread(reply, level + 1)

root = CommentNode(1, "Alice", "Great post!", "10:00")
reply1 = CommentNode(2, "Bob", "I agree!", "10:05")
reply2 = CommentNode(3, "Charlie", "Nice!", "10:10")

add_reply(root, reply1)
add_reply(root, reply2)

display_thread(root)

print("Total comments:", count_comments(root))