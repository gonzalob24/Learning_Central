

#  our data can not be divided in discrete components, for example weighing
#  an object. With perfect precision on weight, the data can take on any value
#  between two points(e.g 5.4 grams,5.423 grams, 5.42322 grams, etc.)

# This means that our n possible values from the discrete uniform distribution 
# is going towards infinity, thus the probability of any individual outcome 
# for a continous distribution is 1/∞ ,technically undefined or zero if we 
# take the limit to infinity. Thus we can only take probability measurements 
# of ranges of values, and not just a specific point. 

# A continous random variable X with a probability density function is a 
# continous uniform random variable when:
 # f(x)=1/(b−a)    a <= x <=b


# This makes sense, since for a discrete uniform distribution the f(x)=1/n 
# but in the continous case we don't have a specific n possibilities, we have 
# a range from the min (a) to the max (b)

# The mean is simply the average of the min and max: (a+b) / 2
# he variance is defined as: σ^2=(b−a)^2 / 12

# Let's say on average, a taxi ride in NYC takes 22 minutes. After taking 
# some time measurements from experiments we gather that all the taxi rides 
# are uniformly distributed between 19 and 27 minutes. What is the probability 
# density function of a taxi ride, or f(x)?

#Let's solve this with python

#Lower bound time
a = 19

#Upper bound time
b = 27

#Then using our probability density function we get
fx = 1.0/(b-a)

#show 
print('The probability density function results in %1.3f' %fx)


#We can also get the variance 
var = ((b-a)**2 )/12

#Show

# So let's ask the question, what's the probability that the taxi ride will 
# last at least 25 minutes?

# This is the same as the PDF of f(27) (the entire space) minus the 
# probability space less than 25 minutes.

#f(27)
fx_1 = 27.0/(b-a)
#f(25)
fx_2 = 25.0/(b-a)

#Our answer is then
ans = fx_1-fx_2

#print
print(' The probability that the taxi ride will last at least 25 minutes is %2.1f%%' %(100*ans))


# Doing this with schipy

# Import the following
from scipy.stats import uniform
import numpy as np
from matplotlib import plt
#Let's set an A and B
A=0
B=5

# Set x as 100 linearly spaced points between A and B
x = np.linspace(A,B,100)

# Use uniform(loc=start point,scale=endpoint)
rv = uniform(loc=A,scale=B)

#Plot the PDF of that uniform distirbution
plt.plot(x,rv.pdf(x))
























