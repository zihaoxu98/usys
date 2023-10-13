from setuptools import setup, find_packages

setup(
    name='usys',
    version='0.1',
    packages=find_packages(),
    install_requires=['numpy'],
    author='Zihao Xu',
    author_email='zihao.xu@columbia.edu',
    description='A package for unit system',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/xzh19980906/usys',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)