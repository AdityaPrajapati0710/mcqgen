from setuptools import find_packages,setup

setup(
    name="mcqgenerator",
    version='0.0.1',
    author="aditya prajapati",
    author_email="ap728991@gmail.com",
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
    
    
)