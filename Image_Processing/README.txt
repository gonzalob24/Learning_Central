Installed: pip install --user opencv-python

will also need numpy

------------------------------------------------------


Before working with images I needed to install the image module. 
However the python library image module is no longe
being supported, its a dead project. So I had to install Pillow 
(PIL fork). You may find this information useful
https://pillow.readthedocs.io/en/stable/installation.html. 

Before installing make sure that you have pip installed
I am using a macOS Mojave and it Python 2.7 is installed. I tried 
installing pip and I would get an error message. 
" DEPRECATION: Python 2.7 will reach the end of its life on January 
1st, 2020. Please upgrade your Python as Python 2.7 
won't be maintained after that date. A future version of pip will 
drop support for Python 2.7."

So I installed pip3:  
# pip3 install Pillow.
This runs with Python3. You dont need to install Python Imaging Library 
PIL since we will be using Pillow.

once installed you can start using it with
# from PIL import Image
