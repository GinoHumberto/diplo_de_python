# -------------------------------- #
#       Introducción básico        #
# -------------------------------- #

# import seaborn as sns
# import matplotlib.pyplot as plt

# tips = sns.load_dataset("tips") # DataFrame con datos de propinas, tips es la variable y con sns.load_dataset traemos el data set de seaborn
# sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", style="sex")
# plt.title("Relacion total de la cuenta vs propina")
# plt.show()


import seaborn as sns
import seaborn.objects as so

tips = sns.load_dataset("tips")

(
    so.Plot(tips, x="total_bill", y="tip", color="time")
        .add(so.Dots(alpha=0.7))
        .add(so.Line(), so.PolyFit(order=1)) # Recta de regresion
        .theme(sns.plotting_context("notebook"))
).show()