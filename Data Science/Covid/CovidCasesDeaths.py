import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import json
import os

# Goals:
# Show rate of growth (delta_c) of covid over time
# Determine relationship between delta_c and r0
# Show covid mortality over time and over demographics
# Show above metrics by state
#
# LT:
# Cross with population density
# Create model of Covid without any policies in place
# Measure effects of major policies on growth rate

states = ["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MS", "MT","NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY"]
class StateAnalysis():
    def __init__(self):
        pwd = os.getcwd()
        tmp = pd.read_csv(pwd + "\\covidstate.csv")[["submission_date", "state", "new_case", "new_death"]]
        self.data = tmp.loc[tmp["state"].isin(states)]
        #index : ["submission_date", "state", "tot_cases", "conf_cases", "prob_cases", "new_case", "pnew_case", "tot_death", "conf_death", "prob_death", "new_death", "pnew_death", "created_at", "consent_cases", "consent_deaths"]

    def _check(self):
        d = self.data
        print(d.columns)
        print(d.head())
        print(d.tail())
        print(d.describe())
        print(d.dtypes)

    def clean(self):
        # not_states = ["RMI", "VI", "NYC", "FSM", "PW", "GU", "AS", "PR", "MP"]
        clean = self.data
        clean["submission_date"] = pd.to_datetime(clean["submission_date"], format = r"%m/%d/%Y")
        self.data = clean.sort_values(by = ["state", "submission_date"]).reset_index(drop = True)

    def wk_avg(self, metric):
        col = []
        for i in range(self.data.shape[0] - 3):
            if i in [0, 1, 2]:
                col.append(0)
                continue
            else:
                s = 0
                for j in range(i - 3, i + 4):
                    s += self.data.at[j, metric]
                col.append(s / 7)
        col += [0] * 3
        self.data[metric + "_7"] = col

    def total(self):
        data_per_day = {}
        for _, r in self.data.iterrows():
            if not r.submission_date in data_per_day:
                data_per_day[r.submission_date] = [r.new_case, r.new_death]
            else:
                data_per_day[r.submission_date][0] += r.new_case
                data_per_day[r.submission_date][1] += r.new_death
        rf = pd.DataFrame(columns = ["submission_date", "state", "new_case", "new_death"])
        for k in data_per_day:
            row = {
                "submission_date": k,
                "state": "US",
                "new_case": data_per_day[k][0],
                "new_death": data_per_day[k][1]
            }
            rf = rf.append(row, ignore_index = True)
        self.data = pd.concat([self.data, rf], ignore_index = True)
        self.clean()

    def mortality(self):
        mortality = []
        for _, r in self.data.iterrows():
            if r.new_case != 0:
                mortality.append(r.new_death / r.new_case)
            else:
                mortality.append(0)
        self.data["mortality"] = mortality

    def avgs(self):
        cols = ["new_case", "new_death", "mortality"]
        for c in cols:
            self.wk_avg(c)

    def delta(self):
        delta_c = []
        delta_d = []
        first = True
        for i in range(self.data.shape[0]):
            current = self.data.at[i, "state"]
            if first:
                first = False
                on = current
                delta_c.append(0)
                delta_d.append(0)
                continue
            else:
                pcase = self.data.at[i - 1, "new_case_7"]
                pdeath = self.data.at[i - 1, "new_death_7"]
                case = self.data.at[i, "new_case_7"]
                death = self.data.at[i, "new_death_7"]
                delta_c.append(pcase - case)
                delta_d.append(pdeath - death)
            if on != current:
                first = True
            
        self.data["delta_c"] = delta_c
        self.data["delta_d"] = delta_d
    
    def read(self):
        self.clean()
        self.total()
        self.mortality()
        self.avgs()
        self.delta()
    
    def _variants(self):
        with open("variant.json") as f:
            variants = json.load(f)
        vf = pd.DataFrame(variants["USA"])
        vf["week"] = pd.to_datetime(vf["week"])
        fill = {}
        current = [0] * 22
        index = list(self.data["submission_date"])
        
        for i, d1 in enumerate(index):
            for d2 in vf["week"]:
                if d1 == d2:
                    current = vf.loc[vf["week"] == d2]
            fill[i] = current
        print(fill)
        vf = pd.DataFrame(fill, columns = vf.columns).set_index("week")
        print(vf.head())
        print(vf.tail())
        return vf
        
        
    def plot(self, **kwargs):
        plt.close("all")
        for k, v in kwargs.items():
            if k == "states":
                states = v
            elif k == "metrics":
                metrics = v
            else:
                print("invalid kwarg")
                return
        for s in states:
            for m in metrics:
                data = self.data[self.data["state"] == s][["submission_date", m]].set_index("submission_date")
                plt.plot(data, label = f"{s} : {m}")
        # vf = self._variants()
        # plt.plot(vf)
        plt.legend(loc = "upper left")
        plt.grid(True, which = "both", axis = "both")
        plt.show()

    def get(self):
        # self.data = self.data.loc[self.data["state"] == "US"]
        print(tabulate(self.data, headers = "keys", tablefmt = "psql"))

def main():
    s = StateAnalysis()
    s.read()
    s.plot(states = ["US"], metrics = ["mortality_7"])

if __name__ == "__main__":
    main()