from MesaGini import *

model = MoneyModel(50, 10, 10)
for i in range(100):
    model.step()

# The below is needed for both notebooks and scripts
import matplotlib.pyplot as plt
import numpy as np

# To get the series of Gini coefficients as a pandas DataFrame:
gini = model.datacollector.get_model_vars_dataframe()
gini.plot()
plt.show()

# Similarly, we can get the agent-wealth data:
#You’ll see that the DataFrame’s index is pairings of model step and agent ID. 
#You can analyze it the way you would any other DataFrame. For example, to get a histogram of agent wealth at the model’s end:

agent_wealth = model.datacollector.get_agent_vars_dataframe()
end_wealth = agent_wealth.xs(99, level="Step")["Wealth"]
end_wealth.hist(bins=range(agent_wealth.Wealth.max()+1))
plt.show()

#plot the wealth of a given agent (in this example, agent 14):
one_agent_wealth = agent_wealth.xs(14, level="AgentID")
one_agent_wealth.Wealth.plot()
plt.show()