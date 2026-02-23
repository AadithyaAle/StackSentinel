from setuptools import setup, find_packages

setup(
    name='stacksentinel',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'boto3',
        'psutil',
        'flask',
        'rich',
        'pyttsx3',
        'pyngrok',
        'distro',
        'GPUtil',
    ],
    entry_points={
        'console_scripts': [
            'stacksentinel=main:cli_entry_point',
            'stacksentinel-ui=server:start_server',
        ],
    },
    author='Aadithya Ale',
    description='An Autonomous AI Infrastructure Agent',
)