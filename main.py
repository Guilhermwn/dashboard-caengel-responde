from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px


# cwd: Path = report.cwd()
report: Path = Path('relatorio_de_produção_2024_1.xlsx')
horas: dict = dict()
xls = pd.ExcelFile(report)
xls_sheets = xls.sheet_names

for sheet in xls_sheets:
    excel_data = pd.read_excel(report, sheet_name=sheet, header=1)
    excel_data = excel_data['total de horas'][0]
    excel_data = (excel_data.days*24) + (excel_data.seconds//3600) + ((excel_data.seconds//60) % 60)/60
    horas[sheet] = excel_data

df = pd.DataFrame.from_dict(horas, orient='index', columns=['horas'])
df.reset_index(inplace=True)
df.columns = ['MEMBRO', 'HORAS TRABALHADAS']
df = df.sort_values(df.columns[1], ascending=False, ignore_index=True)
df.index = range(1, len(df) + 1)

st.header('Ranking - Caengel Responde 2024.1')
st.dataframe(df, use_container_width=1)

fig = px.bar(df, x='MEMBRO', y='HORAS TRABALHADAS')
st.plotly_chart(fig)