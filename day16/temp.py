import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame(df, columns=columns)
sns.boxplot(x='Region', y='Price', data=df, ax=ax3)
ax3.set_title("北京各大区二手房房屋总价", fontsize=15)
ax3.set_xlabel("区域")
ax3.set_ylabel("房屋总价")
plt.show()