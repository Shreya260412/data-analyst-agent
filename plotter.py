import matplotlib.pyplot as plt
import base64
from io import BytesIO

def plot_and_encode(df):
    fig, ax = plt.subplots()
    ax.scatter(df['Rank'], df['Worldwide gross'])
    m, b = np.polyfit(df['Rank'], df['Worldwide gross'], 1)
    ax.plot(df['Rank'], m*df['Rank'] + b, linestyle='dotted', color='red')

    ax.set_xlabel("Rank")
    ax.set_ylabel("Worldwide gross")
    ax.set_title("Rank vs Worldwide gross")

    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=150)
    plt.close(fig)
    img_str = base64.b64encode(buf.getvalue()).decode("utf-8")
    return f"data:image/png;base64,{img_str}"
