from project.core import db


class Comment(db.Model):
    pass

class Message(db.Model):
    pass

class Like(db.Model):
    pass

class Share(db.Model):
    pass


__all__ = ['Comment', 'Message', 'Like', 'Share']
