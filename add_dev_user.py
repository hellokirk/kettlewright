#!/usr/bin/env python3
"""
Quick script to add a development user to the database
"""
import os
import sys
from datetime import datetime, UTC

# Add the app directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from app import create_app, db
from app.models import User

def add_dev_user():
    app = create_app()
    
    with app.app_context():
        # Check if dev user already exists
        existing_user = User.query.filter_by(username='dev').first()
        if existing_user:
            print("Dev user already exists!")
            print(f"Username: dev")
            print(f"Email: dev@example.com")
            print(f"Password: dev123")
            return
        
        # Create new dev user
        dev_user = User(
            username='dev',
            email='dev@example.com',
            confirmed=True,  # Skip email confirmation
            created_at=datetime.now(UTC),
            last_login=None
        )
        dev_user.password = 'dev123'  # This will use the password setter
        
        db.session.add(dev_user)
        db.session.commit()
        
        print("Development user created successfully!")
        print(f"Username: dev")
        print(f"Email: dev@example.com") 
        print(f"Password: dev123")

if __name__ == '__main__':
    add_dev_user()