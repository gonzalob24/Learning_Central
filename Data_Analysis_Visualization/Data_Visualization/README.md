# Descriptive Statistics
- Find important elements in data that describe it
- Summarize and find patterns
- Can't make conclusions beyond the data anlyzed

### Inferential Statistics
- Seek to exaplin why the data is that way 

### Probability Sampling
<hr>
- Chance of inclusion are greater than zero
- Object 

### Non-Probability Sampling
<hr>
- No chance of probability
- subjective jusdgement of the researcher in selecting data

### Measures of Central Tendency
<hr>
- Median: Central measure in frequency distribution. 
	- Half of the values are above and half are below the median
	- 50% are above and 50% are below the media
	- Robust, it is not affected by outliers
- Mean: The average of the numbers in dataset.
	- Mean may not actual be a value in dataset 
	- Not robust 
	- suceptible to outliers, becomes skewed
	- Use median or mode for skewed data
- Mode: most frequent
	- typically used with categorical data with descrete values and cannot be ordered
- Geometric Mean: averageing numbers with different scales
- Harmonic mean: 

### IQR -- Measures od Dispersion
<hr>
- Dispersion: 
	- Nonegatie real numebr
- Range: Largest - smallest
	- Increase if the data is very diverse
	- Outliers affect the range
- Quartile 1 (50%): middle number between the smallest number and median
- Qyartile 3 (75%): middle number between the median and larges number
- IQR: difference between Q3 and Q1
	- most robust calculationf for range
	- Good way to account for outliers
	- How spread the data is 
	- focus is on the middle of the data 

### Variance and Standard Deviation -- Measures of Dispersion
<hr>
- Variance
	- Second most important number 
	- nonegative
	- Movements around the mean
	- Sample mean X_hat
	- Mean Deviation = Xi - X_hat
	- Squared mean deviation = (Xi - X_hat)^2 
	- VARIANCE = sum(Xi - X_hat)^2 / (n - 1)
	- Bessel's Correction: improves the estimate of the variance
- Standard Deviation
	- sqrt(variance)
	- Estimate uncertainty of a set of outcomes
	- Measures spread of data around the mean
	- Always positive
	- Sensitive to outliers