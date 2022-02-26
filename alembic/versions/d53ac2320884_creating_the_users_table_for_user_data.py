"""creating the users table for user data

Revision ID: d53ac2320884
Revises: 95b959a425bc
Create Date: 2022-02-20 18:16:50.805822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd53ac2320884'
down_revision = '95b959a425bc'
branch_labels = None
depends_on = None



def upgrade():
    op.create_table('users', 
                    sa.Column('user_id', sa.Integer(), nullable=False,primary_key=True),
                    sa.Column('email', sa.String(), nullable=False , unique=True), 
                    sa.Column('password', sa.String(), nullable=False), 
                    sa.Column('username', sa.String(), nullable=False , unique=True), 
                    sa.Column('fullname', sa.String(), nullable=False), 
                    sa.Column('profile_pic', sa.String(), nullable=False), 
                    sa.Column('bio', sa.String(), nullable=False), 
                    sa.Column('github_link', sa.String(), nullable=False), 
                    sa.Column('joined_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()'))
                    )
    pass

#     user_id = Column (Integer, primary_key=True, nullable=False)
#     email = Column (String , nullable=False, unique=True)
#     password = Column(String, nullable=False)
#     username = Column(String, nullable=False, unique=True)
#     fullname = Column(String)
#     profile_pic = Column(String)
#     bio = Column(String)
#     github_link = Column(String)
#     joined_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


def downgrade():
    op.drop_table('users')
    pass