from database import db
from models.Comment import Comment
from sqlalchemy.orm import joinedload

class CommentDAO:

    def get_comments_by_page_id(self, page_id):
         return Comment.query.filter_by(page_id=page_id).options(joinedload(Comment.user)).all()

    def add_comment(self, comment):
         db.session.add(comment)
         db.session.commit()

    def delete_comment(self, comment):
         db.session.delete(comment)
         db.session.commit()