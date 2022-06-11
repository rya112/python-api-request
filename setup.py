from setuptools import find_packages, setup

setup(
    name='python-api-request',
    version='0.0.1',
    install_requires=['dotenv_values', 'requests'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/rya112/python-api-request',
    license='MIT',
    author='Ricardo Akatsuka',
    author_email='rya112@email.com',
    description='Python API Request Project'
)
