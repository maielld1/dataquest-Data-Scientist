## 1. The Spark DataFrame: An Introduction ##

with open('census_2010.json') as f:
    for x in range(0,4):
        print(f.readline())

## 3. Schema ##

sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.printSchema()

## 4. Pandas vs Spark DataFrames ##

df.show(5)

## 5. Row Objects ##

first_five = df.head(5)
for x in first_five:
    print(x.age)

## 6. Selecting Columns ##

df[['age']].show()
df[['age', 'males', 'females']].show()

## 7. Filtering Rows ##

fifty_plus = df[df['age']>5]
fifty_plus.show()

## 8. Using Column Comparisons as Filters ##

x = df[df['females']<df['males']]
x.show()

## 9. Converting Spark DataFrames to pandas DataFrames ##

pandas_df = df.toPandas()
pandas_df['total'].hist()