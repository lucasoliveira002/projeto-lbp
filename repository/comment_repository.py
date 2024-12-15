# repository/comment_repository.py
from dao.comment_dao import CommentDAO
from models.Comment import Comment
from sqlalchemy.orm import joinedload

class CommentRepository:
    def __init__(self):
        self.comment_dao = CommentDAO()

    def get_comments_by_page_id(self, page_id):
        return self.comment_dao.get_comments_by_page_id(page_id)
    
    def add_comment(self, user_id, conteudo, page_id):
        comment = Comment(user_id=user_id, conteudo=conteudo, page_id=page_id)
        self.comment_dao.add_comment(comment)
        return comment

    def delete_comment(self, comment):
         self.comment_dao.delete_comment(comment)