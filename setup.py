# This Python haveno client extends the features of Haveno, supporting mobile devices and more.
# Copyright (C) 2024 KewbitXMR (https://kewbit.org)
#
# Contact Email: kewbitxmr@protonmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from setuptools import setup, find_packages

setup(
    name='haveno-client',  # Package name
    version='0.1.0',
    description='A client for interacting with the Haveno daemon.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/KewbitXMR/python-haveno-client',  # Replace with the actual URL
    author='Kewbit',
    author_email='kewbitxmr@protonmail.com',
    license='MIT',
    packages=find_packages(),  # Automatically find package directories
    install_requires=[
        'grpcio',
        'grpcio-tools',
        'socks'
    ],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)