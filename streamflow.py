import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




def load_streamflow(filename):
    """Read the streamflow CSV. Return the dates and a 2D array of flows (cfs), one column per gauge."""
    # your array creation and slicing code goes here
    data = np.genfromtxt(filename, delimiter=',', dtype=str, skip_header=1)

    dates = data[:, 0].astype('datetime64[m]')
    y_1 = data[:, 1].astype(float)
    y_2 = data[:, 2].astype(float)
    y_3 = data[:, 3].astype(float)
    y_4 = data[:, 4].astype(float)
    y_5 = data[:, 5].astype(float)
    flows = np.column_stack([y_1, y_2, y_3, y_4, y_5])
    return dates, flows


def plot_streamflow(dates, flows, sites):
    """Plot the flow at each gauge, with the same title, labels, and formatting as the Matplotlib HW."""
    # your plotting code goes here
    plt.plot(dates, flows[:, 0], color='purple', label=sites[0])
    plt.plot(dates, flows[:, 1], color='teal', label=sites[1])
    plt.plot(dates, flows[:, 2], color='green', label=sites[2])
    plt.plot(dates, flows[:, 3], color='orange', label=sites[3])
    plt.plot(dates, flows[:, 4], color='orangered', label=sites[4])
    plt.title('Provo River Streamflow Data (2021)')
    plt.xlabel('Date')
    plt.ylabel('Flowrate (cfs)')
    plt.xticks(rotation=45)
    plt.legend(title='Site Numbers')
    plt.grid(True)
    plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")
    plt.show()



# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(dates, flows, sites)

def summarize(dates, flows, sites):
    # Max is equal to 131.0 
    # Avarage is equal to 57.0
    df = pd.DataFrame(flows, columns=sites, index=dates)
    summary = pd.DataFrame({
        'Gauge': df.columns,
        'Max (cfs)': df.max().values,
        'Date of max': df.idxmax().dt.strftime('%Y-%m-%d %H:%M').values,
        'Min (cfs)': df.min().values,
        'Avg (cfs)': np.round(df.mean().values, 1)
    })
    print(summary) 
    summary.to_csv('streamflow_summary.csv', index=False)
summary = summarize(dates, flows, sites)
