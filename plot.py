# %%
import seaborn as sns
import pandas as pd
sns.set_style("whitegrid")
import matplotlib.pyplot as plt


# %%
data = pd.DataFrame({
    "llama3.1": {'pass@1': 0.5067073170731707, 'pass@3': 0.6851626016260162, 'pass@10': 0.8048780487804879}, 
    "deepseek-coder-v2": {'pass@1': 0.6847560975609757, 'pass@3': 0.7717479674796748, 'pass@10': 0.8109756097560976}})
data = pd.melt(data, var_name="model", ignore_index=False)
data["metric"] = data.index
print(data)

print(data)
g = sns.catplot(data=data, x="metric", y="value", col="model", kind="bar", height=4.5, aspect=.6)
g.set(ylim=(0.4, 0.9))
g.set_axis_labels("", "HumanEval score")
g.set_titles("{col_name}")


# %%
data = pd.DataFrame({
    "llama3.1 - default": {'pass@1': 0.5067073170731707, 'pass@3': 0.6851626016260162, 'pass@10': 0.8048780487804879}, 
    "llama3.1 - self-selection": {'pass@1': 0.5256097560975609, 'pass@3': 0.7132621951219512, 'pass@10': 0.8292682926829268},
    "llama3.1 - self-critique": {'pass@1': 0.46, 'pass@3': 0.6332621951219512, 'pass@10': 0.7592682926829268}})
data = pd.melt(data, var_name="model", ignore_index=False)
data["metric"] = data.index
print(data)

print(data)
g = sns.catplot(data=data, x="metric", y="value", col="model", kind="bar", height=4.5, aspect=.6)
g.set(ylim=(0.4, 0.9))
g.set_axis_labels("", "HumanEval score")
g.set_titles("{col_name}")

# %%
