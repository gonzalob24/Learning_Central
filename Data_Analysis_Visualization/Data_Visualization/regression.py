

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

from numpy.random import randn
from scipy import stats

tips = sns.load_dataset('tips')
tips.head()

#  tips vs ttotal bill
sns.lmplot('total_bill', 'tip', tips)

## I can specify the order of the polinomial
sns.lmplot('total_bill', 'tip', tips, order=4, 
           scatter_kws={'marker':'.', 'color':'indianred'},
           line_kws={'linewidth':1, 'color':'blue'})

# no regresion line
sns.lmplot('total_bill', 'tip', tips, fit_reg=False)

tips['tip_pect'] = 100 * (tips['tip']/tips['total_bill'])
tips.head()

# plot discrete variables
sns.lmplot('size', 'tip_pect', tips)

# look into what jitter is
sns.lmplot('size', 'tip_pect', tips, x_jitter=0.1)

sns.lmplot('size', 'tip_pect', tips, x_estimator=np.mean)

sns.lmplot('total_bill', 'tip_pect', tips, hue='sex', markers=['x', 'o'])

sns.lmplot('total_bill', 'tip_pect', tips, hue='day')

sns.lmplot('total_bill', 'tip_pect', tips, lowess=True, line_kws={'color':'black'})


# lmplot uses regplot-- regression plot
# lmplot was bilt unti of regplot

sns.regplot('total_bill', 'tip_pect', tips)
fig, (axis1, axis2) = plt.subplots(1, 2, sharey=True)

sns.regplot('total_bill','tip_pect', tips, ax=axis1)
sns.violinplot(tips['size'], tips['tip_pect'], ax=axis2)












