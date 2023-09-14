labels = ["Statement of Problem", "Hypothesis", "Variables", "Procedure", "Qualitative Data", "Quantitative Data", "Graph", "Calculations", "Analysis", "Sources of Error", "Conclusion", "Applications", "Bibliography"]
prompts = [
    "This is an open ended question rather than a yes/no question. A simple way to write this is: 'How does [Independent Variable] affect [Dependent Variable]?'",
    "If the ___ [IV] is {increased, decreased}, then the ___ [DV] will ___ [Increase? Decrease?] because ... [provide rationale and/or the proposed mechanism. This mechanism will require a sentence or two to explain it. State the mechanism AND explain how it works!]",
    "",
    "The procedure is a numbered list of the steps in the experiment and includes labeled diagram(s) of how the experiment was performed.",
    "Describe changes that cannot be quantified or qualitative aspects of measuring that affect the quantitative data.",
    "",
    "",
    "Be sure to show sample calculations for any non-trivial calculations. You do not have to show simple calculations (like 'mean.') If you are in doubt go ahead and show your calculations. You will never lose points for showing calculations (unless they are incorrect) and you may gain credit for showing calculations. If your calculations lead to data that will be put into a graph, make a separate table for the 'processed data.'",
    "(1) Describe patterns in your data. What does it show (if anything?) Explain what your data says. Do not ascribe causes, but do describe correlations. (“Cause-effect” relationship can be attributed AFTER relationship is established but it cannot be asserted UNTIL there is a clear relationship.)\n(2) Quote your data (use specific numbers) to show the pattern (described above). Be explicit. This will seem weird at first but gives the narrative a solid, scientific bite.\n(3) Conclude by stating if the IV is directly, inversely, or not clearly related to the DV.",
    "Focus on experimental sources of errors like things that have to do with temperature, for example. The container may have insulated the fluid and prevented heat loss. Identify things that could change the outcome of the experiment. Then, explain how the errors are believed to affect the data: increase from normal, decrease from normal; don't just say, '... affected the data.'",
    "Respond to your hypothesis based on your data, beginning with a restatement of your hypothesis (without the mechanism component.) DO NOT EVER say that your hypothesis was right or wrong. After one experiment, a hypothesis can either be supported or disproven by the data. Explain why you came to that conclusion with your data as support.",
    "If your experiment demonstrated a clear pattern, what use could that be put to?",
    "Real experiments are done to confirm previous work or to extend previous research. For this reason experiments often include citations from other experiments. The citations are included in the report and the references, the bibliography, is included as the very last page of the report."
]
template = dict(zip(labels, prompts))
headers = ["Description of variable", "Magnitude used in experiment", "How you will ensure consistency"]
first_col = ["Type of variable", "Independent variable", "Dependent variable", "Standard of Comparison", "Controlled variable(s)"]

def inp(safe = []):
    result = None
    while result is None:
        try:
            result = input()
            if result in safe:
                return result
            result = int(result)
        except ValueError:
            result = None
            continue
    return result

def get_report_dict(load_report = {}):
    report = load_report
    for l in labels:
        report[l] = None

    done = False
    cur = 0
    while not done:
        print("Next:", labels[cur])
        command = input("$")
        if command == "to":
            for i, l in enumerate(labels):
                print(i, ":", l)
            where = inp() % len(labels)
            cur = where
            continue
        elif command == "view":
            for i, l in enumerate(labels):
                print(i, ":", l)
            where = inp() % len(labels)
            print(report[list(report.keys())[where]])
            continue
        elif command == "save":
            done = True
            continue

        l = labels[cur]
        report[l] = None
        print("---", l, "---")
        if l == "Variables":
            data = [headers]
            print("Number of controlled variables: ")
            controlled = inp()
            variables = ["Independent Variable", "Dependent Variable"] + ["CV " + str(i + 1) for i in range(controlled)]
            for v in variables:
                print("---", v, "---")
                row = []
                for h in data[0]:
                    row.append(input(h + ": "))
                data.append(row)

        elif l == "Quantitative Data":
            print("Number of columns: ")
            cols = inp()
            data = [[]]
            print("--- Column Headers (Remember dimensions and units) ---")
            for i in range(cols):
                print("Header for column", str(i + 1) + ": ")
                data[0].append(input())
            print("--- Number of rows (0 for continous until \"stop\") ---")
            rows = inp()
            if rows == 0:
                complete = False
                i = 0
                while not complete:
                    row = []
                    print("--- Row", i, "---")
                    for j in range(cols):
                        print(data[0][j])
                        val = inp(["stop"])
                        if val != "stop":
                            row.append(val)
                        else:
                            complete = True
                            break
                    data.append(row)
                    i += 1            
            else:
                for i in range(rows):
                    row = []
                    print("--- Row", i, "---")
                    for j in range(cols):
                        print(data[0][j])
                        row.append(inp())
                    data.append(row)
        elif l == "Graph":
            data = "**Graph**"
        else:
            print(prompts[cur])
            data = input()

        report[l] = data
        cur += 1
        cur %= len(labels)
    return report

def main():
    report = get_report_dict()
    print(report)

if __name__ == "__main__":
    main()