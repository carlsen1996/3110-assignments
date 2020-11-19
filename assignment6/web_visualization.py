import pandas as pd
import sys
import matplotlib.pyplot as plt

def plot_reported_cases(s):
    reported = s["Nye tilfeller"]
    date = s["Dato"]
    date = list(date)
    for i in range(len(date)):
        date[i] = date[i].date()
    plt.xlabel("Date")
    reported = list(reported)
    plt.ylabel("Reported cases")
    plt.bar(range(len(reported)), reported)
    plt.xticks(range(len(date)), date[::round(len(date) / 10)], rotation=90, size=5)
    plt.locator_params(axis='x', nbins=10)
    plt.tight_layout()
    plt.show()
    plt.close()
    
def plot_cumulative_cases(s):
    cumulative = s["Kumulativt antall"]
    date = s["Dato"]
    cumulative = list(cumulative)
    date = list(date)
    for i in range(len(date)):
        date[i] = date[i].date()
    fig, ax1 = plt.subplots()
    plt.xlabel("Date")
    plt.ylabel("Cumulative cases")
    plt.plot(range(len(date)), cumulative, linestyle='-')
    plt.xticks(range(len(date)), date[::round(len(date) / 10)], rotation=90, size=5)
    plt.locator_params(axis='x', nbins=10)
    plt.tight_layout()
    plt.show()
    plt.close()
    

def plot_both(s):
    cumulative = s["Kumulativt antall"]
    date = s["Dato"]
    cumulative = list(cumulative)
    date = list(date)
    for i in range(len(date)):
        date[i] = date[i].date()
    fig, ax1 = plt.subplots()
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Cumulative cases")
    ax1.plot(range(len(date)), cumulative, linestyle='-')
    plt.xticks(range(len(date)), date[::round(len(date) / 10)], rotation=90, size=5)
    plt.locator_params(axis='x', nbins=10)
    ax2 = ax1.twinx()
    reported = s["Nye tilfeller"]
    reported = list(reported)
    ax2.set_ylabel("Reported cases")
    ax2.bar(range(len(reported)), reported)
    fig.tight_layout()
    plt.show()
    plt.close()

def main():
    if len(sys.argv) == 1:
        s = pd.read_csv("AlleFylker.csv")
        s.Dato = pd.to_datetime(s.Dato, dayfirst=True)
        plot_both(s)
        
    elif len(sys.argv) >= 2:
        # try:
        s = pd.read_csv(sys.argv[1])
        
        if len(sys.argv) == 4:
            s.Dato = pd.to_datetime(s.Dato, dayfirst=True)
            start_date = pd.to_datetime(sys.argv[2], dayfirst=True)
            end_date = pd.to_datetime(sys.argv[3], dayfirst=True)
            u = s[s.Dato.between(start_date, end_date)]
            plot_both(u)
            plot_cumulative_cases(u)
            plot_reported_cases(u)
            
        # except:
        #     print("""Try writing:
        #     Agder.csv
        #     Innlandet.csv
        #     MoreOgRomsdal.csv
        #     Nordland.csv
        #     Oslo.csv
        #     Rogaland.csv
        #     Trondelag.csv
        #     TromsOgFinnmark.csv
        #     Trondelag.csv
        #     VestfoldOgTelemark.csv
        #     Vestland.csv
        #     Viken.csv""")
        #     exit(0)
    
if __name__ == '__main__':
    main()