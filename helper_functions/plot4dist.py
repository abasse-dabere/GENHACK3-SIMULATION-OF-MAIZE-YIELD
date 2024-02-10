import matplotlib.pyplot as plt
import seaborn as sns

def plot4dist(x, prefix="YIELD"):
    """
    Plot the distribution of x
    :param x:(shape: (n, 4)
    :return: None
    """
    for i in range(4):
        sns.kdeplot(x[:, i], fill=True, label=f"{prefix}_{i+1}")
    plt.xlabel(prefix)
    plt.legend()