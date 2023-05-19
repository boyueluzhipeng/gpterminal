from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gpterminal",
    version="0.1.9",
    author="Your Name",
    author_email="your.email@example.com",
    description="A CLI tool to interact with GPT-3/GPT-4, answer Git questions, and execute commands",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/gpterminal",
    packages=find_packages(),
    install_requires=[
        'click',
        'requests',
        'rich',
        'pathlib',
        'openai',
        'tiktoken',
        'prompt_toolkit'
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "gt=cli.cli:gpterminal",
            "gs=cli.gs:gpterminal"
        ],
    },
)