from setuptools import setup

setup(name='jupyter_cpp_kernel',
    version='0.0.3',
    description='c++ kernel for Jupyter',
    author='ChunweiYan',
    author_email='yanchunwei@outlook.com',
    license='MIT',
    classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
    url='https://github.com/ntwuxc/jupyter-cpp-kernel/',
    download_url='https://github.com/ntwuxc/jupyter-cpp-kernel/tarball/0.0.3',
    packages=['jupyter_cpp_kernel'],
    scripts=['jupyter_cpp_kernel/install_cpp_kernel'],
    keywords=['jupyter', 'notebook', 'kernel', 'c++', 'cpp']
)
