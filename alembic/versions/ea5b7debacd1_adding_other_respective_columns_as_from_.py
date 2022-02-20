"""Adding other respective columns as from models.py

Revision ID: ea5b7debacd1
Revises: 2a17efe43c2b
Create Date: 2022-02-20 15:53:35.095791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea5b7debacd1'
down_revision = '2a17efe43c2b'
branch_labels = None
depends_on = None



def upgrade():
    op.add_column('posts',sa.Column('image' ,sa.String()))
    op.add_column('posts',sa.Column('published' , sa.Boolean(), server_default='TRUE', nullable=False))
    op.add_column('posts',sa.Column('created_at' ,sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))
    # sa.Column('post_id' ,sa.Integer(), primary_key=True, nullable=False),
    # sa.Column('content' ,sa.String(), nullable=False)),
    # sa.Column('image' ,sa.String()    ),
    # sa.Column('published' , sa.Boolean(), server_default='TRUE', nullable=False),
    # sa.Column('created_at' ,sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
    # sa.Column('author' ,sa.String() , sa.ForeignKey("users.fullname",ondelete="CASCADE"), nullable=False),
    # sa.Column('author_details' ,sa.relationship("User"))
    pass


def downgrade():
    op.drop_column('posts', 'image')
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass

