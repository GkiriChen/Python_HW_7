from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='0.5',
      description='Home_Work_GoIT',
      url='https://github.com/GkiriChen/Python_HW_7.git',
      author='Gennadiy Kirichenko',
      author_email='kirichenko.gennadiy@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      include_package_data=True,
      entry_points={'console_scripts': ['clean-folder=clean_folder.clean:main']}
)

