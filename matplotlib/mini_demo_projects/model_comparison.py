import numpy as np
import matplotlib.pyplot as plt
 
 # -- 1 prepare some fake data for demonstration --
np.random.seed(42) # makes random numbers predictable (for demo purpose)
actual_values = np.random.rand(20)*10 # generate 20 random numbers between 0 and 10

model_a_predictions = actual_values + np.random.randn(20)*2
model_b_predictions = actual_values + np.random.randn(20)*0.8

# -- 2 set up plotting area --
fig , ax = plt.subplots(1,2,figsize=(10,4),sharex=True,sharey=True)
fig.suptitle("Model prediction comparison: actual vs predicted",fontsize=14)

# --3 plot for model A --
ax_a = ax[0]
ax_a.scatter(actual_values,model_a_predictions,color="blue",label="Model A Predictions",alpha=0.7)
ax_a.plot([0,10],[0,10],'k--',label="Perfect Prediction")
ax_a.set_title('Model A Performance (More Error)')
ax_a.set_xlabel("Actual Values")
ax_a.set_ylabel("Predicted Values")
ax_a.legend() 
ax_a.grid(True,linestyle=':',alpha=0.6)

# -- 4 plot for model B --
ax_b = ax[1]
ax_b.scatter(actual_values,model_b_predictions,color="green",label="Model B Predictions",alpha=0.7)
ax_b.plot([0,10],[0,10],'k--',label="Perfect Prediction")
ax_b.set_title('Model B Performance (Less Error)')
ax_b.set_xlabel('Actual Values')
ax_b.legend()
ax_b.grid(True,linestyle=':',alpha=0.6)

# -- 5 Final Display --
plt.tight_layout(rect=[0,0.03,1,0.95])
plt.show()
