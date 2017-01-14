## 1. Probability basics ##

# Print the first two rows of the data.
print(flags[:2])
most_bars_country = flags['name'].loc[flags['bars'].idxmax()]
highest_population_country = flags['name'].loc[flags['population'].idxmax()]
print(most_bars_country, highest_population_country)

## 2. Calculating probability ##

total_countries = flags.shape[0]
orange_probability = flags[flags['orange'] == 1].shape[0] / total_countries
stripe_probability = flags[flags['stripes'] > 1].shape[0] / total_countries
print(orange_probability, stripe_probability)

## 3. Conjunctive probabilities ##

five_heads = .5 ** 5
ten_heads = .5 ** 10
hundred_heads = .5 ** 100

## 4. Dependent probabilities ##

# Remember that whether a flag has red in it or not is in the `red` column.
numer = flags[flags['red'] == 1].shape[0] 
denom = flags.shape[0]
three_red = (numer/denom)*((numer-1)/(denom-1))*((numer-2)/(denom-2))

## 5. Disjunctive probability ##

start = 1
end = 18000

hundred_prob_list = [i for i in range(start, end + 1) if (i % 100) == 0]
hundred_prob = len(hundred_prob_list) / 18000
print(hundred_prob)

seventy_prob_list = [i for i in range(start, end + 1) if (i % 70) == 0]
seventy_prob = len(seventy_prob_list) / 18000
print(seventy_prob)

## 6. Disjunctive dependent probabilities ##

stripes_or_bars = None
red_or_orange = None

numer = flags[flags['red'] == 1].shape[0] + flags[flags['orange'] == 1].shape[0] - flags[(flags['red'] == 1)&(flags['orange'] == 1)].shape[0]
denom = flags.shape[0]
red_or_orange = numer/denom

numer = flags[flags['stripes'] >= 1].shape[0] + flags[flags['bars'] >= 1].shape[0] - flags[(flags['stripes'] >= 1)&(flags['bars'] >= 1)].shape[0]
denom = flags.shape[0]
stripes_or_bars = numer/denom

## 7. Disjunctive probabilities with multiple conditions ##

heads_or = 1-(0.5 **3)