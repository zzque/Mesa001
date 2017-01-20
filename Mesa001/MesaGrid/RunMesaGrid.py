from MesaGrid import *

model = MoneyModel(50, 10, 10)
for i in range(10):
    model.step()

# The below is needed for both notebooks and scripts
import matplotlib.pyplot as plt
import numpy as np

agent_counts = np.zeros((model.grid.width, model.grid.height))
for cell in model.grid.coord_iter():
    cell_content, x, y = cell
    agent_count = len(cell_content)
    agent_counts[x][y] = agent_count
plt.imshow(agent_counts, interpolation='nearest')
plt.colorbar()
plt.show()