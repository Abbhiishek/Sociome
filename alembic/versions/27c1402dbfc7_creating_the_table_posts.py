"""creating the table posts

Revision ID: 27c1402dbfc7
Revises: 
Create Date: 2022-02-20 18:11:10.338088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27c1402dbfc7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts' , sa.Column('post_id' , sa.Integer(), primary_key=True, nullable=False)
    , sa.Column('content' , sa.String(), nullable=False))
    
    
    
    # sa.Column('post_id' ,sa.Integer(), primary_key=True, nullable=False),
    # sa.Column('content' ,sa.String(), nullable=False)),
    # sa.Column('image' ,sa.String()    ),
    # sa.Column('published' , sa.Boolean(), server_default='TRUE', nullable=False),
    # sa.Column('created_at' ,sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
    # sa.Column('author' ,sa.String() , sa.ForeignKey("users.fullname",ondelete="CASCADE"), nullable=False),
    # sa.Column('author_details' ,sa.relationship("User"))

    pass


def downgrade():
    op.drop_table('posts')
    pass
