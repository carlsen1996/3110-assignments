import pandas as pd
import sys
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

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
    plt.xticks(range(len(date)), date[::round(len(date) / 10)], rotation=90, size=7)
    plt.locator_params(axis='x', nbins=10)
    plt.tight_layout()
    
    plt.savefig("static/reports.png")
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
    plt.xticks(range(len(date)), date[::round(len(date) / 10)], rotation=90, size=7)
    plt.locator_params(axis='x', nbins=10)
    plt.tight_layout()
    plt.savefig("static/cumulative.png")
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
    plt.xticks(range(len(date)), date[::round(len(date) / 10)], rotation=90, size=7)
    plt.locator_params(axis='x', nbins=10)
    ax2 = ax1.twinx()
    reported = s["Nye tilfeller"]
    reported = list(reported)
    ax2.set_ylabel("Reported cases")
    ax2.bar(range(len(reported)), reported)
    fig.tight_layout()
    fig.savefig("static/both.png")
    plt.close()

@app.route("/", methods=["POST"])
def update():
    counties = ["AlleFylker.csv", "Agder.csv", "Innlandet.csv", "MoreOgRomsdal.csv", "Nordland.csv", "Oslo.csv", "Rogaland.csv", "TromsOgFinnmark.csv", "Trondelag.csv", "VestfoldOgTelemark.csv", "Vestland.csv", "Viken.csv"]
    county = request.form.get("county")
    s = pd.read_csv(county)
    s.Dato = pd.to_datetime(s.Dato, dayfirst=True)
    plot_cumulative_cases(s)
    plot_reported_cases(s)
    plot_both(s)
    return render_template('home.html', counties=counties)

    



@app.route("/", methods=['GET', 'POST'])
def main():
    
    # counties = ["Alle fylker", "Agder", "Innlandet", "Møre og Romsdal", "Nordland", "Oslo", "Rogaland", "Troms og Finnmark", "Trøndelag", "Vestfold og Telemark", "Vestland", "Viken"]
    counties = ["AlleFylker.csv", "Agder.csv", "Innlandet.csv", "MoreogRomsdal.csv", "Nordland.csv", "Oslo.csv", "Rogaland.csv", "TromsOgFinnmark.csv", "Trondelag.csv", "VestfoldOgTelemark.csv", "Vestland.csv", "Viken.csv"]
    if len(sys.argv) == 1:
        s = pd.read_csv("AlleFylker.csv")
        s.Dato = pd.to_datetime(s.Dato, dayfirst=True)
        plot_both(s)
        plot_cumulative_cases(s)
        plot_reported_cases(s)
        return render_template('home.html', counties=counties)
        
    elif len(sys.argv) >= 2:
        try:
            s = pd.read_csv(sys.argv[1])
            
            if len(sys.argv) == 4:
                s.Dato = pd.to_datetime(s.Dato, dayfirst=True)
                start_date = pd.to_datetime(sys.argv[2], dayfirst=True)
                end_date = pd.to_datetime(sys.argv[3], dayfirst=True)
                u = s[s.Dato.between(start_date, end_date)]
                plot_both(u)
                plot_cumulative_cases(u)
                plot_reported_cases(u)
                return render_template('home.html')
            
        except:
            print("""Try writing:
            Agder.csv
            Innlandet.csv
            MoreOgRomsdal.csv
            Nordland.csv
            Oslo.csv
            Rogaland.csv
            Trondelag.csv
            TromsOgFinnmark.csv
            Trondelag.csv
            VestfoldOgTelemark.csv
            Vestland.csv
            Viken.csv""")
            exit(0)
    
if __name__ == '__main__':
    app.run()
