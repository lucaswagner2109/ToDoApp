from app import app, db 

from app.models import User

import sqlalchemy as sa
import sqlalchemy.orm as so

# For testing inside terminal, use 'flask shell' 
@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User}