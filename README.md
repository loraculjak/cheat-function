## cheat() function
1. [General Info](#general-info)
2. [Technologies](#technologies)


### General Info
***
Cheat() function takes one argument specifying which exercise of any previous Python assignment the user of this package wants to cheat on. Given the exercise number, cheat()function tells the user the correct solution. The cheat function works for 4 exercises (Q3.2P.5, Q3.2P.4, Q3.2P.3, Q3.2P.2).

## Technologies
***
* [Technology name]: Version 3.9 

## Usage
You start with writing cheat(), and then you write the task you want the solution for. Available tasks are: Q3.2P.5, Q3.2P.4, Q3.2P.3, Q3.2P.2.

```
#Select the task you want the soultion:

  cheat("Q3.2P.4")

#Output:
  plt.subplot(1, 2, 1)
  heatmap = sns.heatmap(data.corr())

  plt.subplot(1, 2, 2)
  kdeplot = sns.kdeplot(x=data.alcohol, y=data.color_intensity)
  plt.tight_layout()
```
