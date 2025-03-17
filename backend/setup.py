from setuptools import setup, find_packages

setup(
    name="sellis-backend",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Flask==3.0.3",
        "Flask-Cors==5.0.0",
        "flasgger==0.9.7.1",
        "python-dotenv==1.0.1",
        "requests==2.32.3",
        "gunicorn==23.0.0",  # Production WSGI server
    ],
    python_requires=">=3.8",
) 