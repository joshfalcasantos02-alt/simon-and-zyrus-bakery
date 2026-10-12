import os
import sys
import subprocess
import webbrowser
import time

def main():
    print("=" * 60)
    print(" 🥖 Starting Simon & Zyrus Bakery - Django Inventory System")
    print("=" * 60)
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bakery.settings')
    
    # Run migrations if needed
    print("Checking database migrations...")
    subprocess.run([sys.executable, 'manage.py', 'migrate'], check=True)
    
    print("\nStarting Django Development Server at http://127.0.0.1:8000 ...")
    print("Main App: http://127.0.0.1:8000/")
    print("Admin Portal: http://127.0.0.1:8000/admin/ (User: admin / Pass: admin123)")
    print("XAMPP phpMyAdmin: http://localhost/phpmyadmin/ (Database: bakery_db)\n")
    
    try:
        subprocess.run([sys.executable, 'manage.py', 'runserver', '127.0.0.1:8000'])
    except KeyboardInterrupt:
        print("\nStopping bakery server...")

if __name__ == '__main__':
    main()
