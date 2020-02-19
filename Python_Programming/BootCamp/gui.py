from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from IPython.display import display

def func(x):
    return x**2



@interact(x=True, y=fixed(1.0))
def g(x, y):
    return (x, y)

interact(func, x=widgets.IntSlider(min=-100, max=100, step=1, value=0))
# interact(func, x=(-100, 100, 1))

w = widgets.IntSlider()
display(w)
