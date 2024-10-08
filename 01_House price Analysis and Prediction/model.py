import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

dataset = pd.read_excel("01_House price Analysis and Prediction/HousePricePrediction.xlsx")

print(dataset.shape)

#categorize the figtures depending on their datatype(obj, int, float, obj)
obj = dataset.dtypes == "object"
obj_cols = list(obj[obj].index)
print(f"categorical variables: {len(obj_cols)}")
for obj_col in obj_cols:
    print(obj_col)

int_ = dataset.dtypes == "int"
int_cols = list(int_[int_].index)
print(f"int variables: {len(int_cols)}")
for int_col in int_cols:
    print(int_col)

float_ = dataset.dtypes == "float"
float_cols = list(float_[float_].index)
print(f"float variables: {len(float_cols)}")
for float_col in float_cols:
    print(float_col)

#select only numerical features for correlation analyst
numerical_dataset = dataset.select_dtypes("number")

#creat heat map
plt.figure(figsize=(12,6))
sns.heatmap(numerical_dataset.corr(), cmap='BrBG', fmt='.2f', linewidths= 2, annot= True)

#save heat map
plt.savefig("01_House price Analysis and Prediction/heatmap.png", dpi=300)

#draw bar plot
uniqe_val = []
for obj_col in obj_cols:
    uniqe_val.append(dataset[obj_col].unique().size)
plt.figure(figsize=(10,6))
plt.title("Unique value of categorical feature")
plt.xticks(rotation=90)
sns.barplot(x=obj_cols,y=uniqe_val)

#save bar plot
plt.savefig("01_House price Analysis and Prediction/uniqe value of categorical feature")