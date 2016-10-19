from setuptools import setup


setup(name='mpu6050-raspberrypi',
      version='1.0.2',
      setup_requires=['setuptools-markdown'],
      description='A package to handle the i2c communication between a '
                  'Raspberry Pi and a MPU-6050',
      long_description_markdown_filename='README.md',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Topic :: Software Development :: Libraries',
          'Programming Language :: Python :: 2.7',
      ],
      keywords='mpu6050 raspberrypi driver',
      url='https://github.com/Tijndagamer/mpu6050',
      author='MrTijn/Tijndagamer',
      author_email='tijndagamer25@gmail.com',
      license='MIT',
      packages=['mpu6050'],
      install_requires=['smbus'],
      scripts=['bin/mpu6050-example'],
      zip_safe=False)
