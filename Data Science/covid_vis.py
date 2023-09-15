import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from sympy import total_degree
from covid_reader import gen_data
from CovidCasesDeaths import states
from variants_reader import data

MULTIPLE_METRICS = True

st.set_page_config(layout="wide")
scatter_column, settings_column = st.columns((4, 1))
scatter_column.title("Covid Visualization")
settings_column.title("Settings")

df = gen_data()

if MULTIPLE_METRICS:
    metrics = settings_column.multiselect("Select Metrics", options=list(df.columns)[2:])
    states = settings_column.multiselect("Select States", options=sorted(states + ["US"]))
    state_df = df[df["state"].isin(states)][["state", "submission_date"] + metrics]
    scatter_column.plotly_chart(px.line(data_frame=state_df, x="submission_date", y=metrics, color="state", height=800, line_shape="spline", render_mode="svg"), use_container_width=True)
else:
    metric = settings_column.selectbox("Select Metric", options=list(df.columns)[2:])
    states = settings_column.multiselect("Select States", options=sorted(states + ["US"]))
    state_df = df[df["state"].isin(states)][["state", "submission_date", metric]]
    scatter_column.plotly_chart(px.line(data_frame=state_df, x="submission_date", y=metric, color="state", height=800, line_shape="spline", render_mode="svg"), use_container_width=True)

vdf, vnames = data()

variants = settings_column.multiselect("Select Variants", options=vnames[1:], default=['20I (Alpha, V1)','21A (Delta)', '21I (Delta)', '21J (Delta)', '21F (Iota)','21C (Epsilon)'])


fig = px.area(data_frame=vdf[vdf["variant"].isin(variants)], x="week", y="value", color="variant", height=800)
# Make it so dates past variants will be discluded vvv

us_cases = settings_column.checkbox("US Cases Overlay")
if us_cases:
    fig2 = px.line(data_frame=df[df["state"] == "US"], x="submission_date", y="new_case_7")
    fig.add_trace(fig2.data[0])

total_sequences = settings_column.checkbox("Total Sequences Overlay")
if total_sequences:
    fig2 = px.line(data_frame=vdf[vdf["variant"] == 'total_sequences'], x="week", y="value")
    fig.add_trace(fig2.data[0])

scatter_column.plotly_chart(fig, use_container_width=True)