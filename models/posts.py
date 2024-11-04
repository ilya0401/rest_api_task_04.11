from pydantic import BaseModel

class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str

    def __str__(self):
        return f'User(id={self.id}, userId={self.userId}, title={self.title}, body={self.body})'
