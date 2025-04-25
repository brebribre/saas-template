from setuptools import setup, find_packages

setup(
    name="backend",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.104.0",
        "uvicorn==0.23.2",
        "python-dotenv==1.0.1",
        "requests==2.32.3",
        "gunicorn==23.0.0",  # Production WSGI server
        "pydantic==2.4.2",
    ],
    python_requires=">=3.8",
) 