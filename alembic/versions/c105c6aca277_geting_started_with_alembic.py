"""geting started with Alembic!

Revision ID: c105c6aca277
Revises: 
Create Date: 2022-02-20 13:00:45.166496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c105c6aca277'
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
