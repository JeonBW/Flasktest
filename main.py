#-*- encoding: utf-8 -*-
import flask
import plotly
from plotly.graph_objs import Scatter, Layout
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import dash
from dash.dependencies import Input, Output, State
import plotly.express as px
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import time
import json
import dash_bootstrap_components as dbc
import datetime



pop = pd.read_csv("고령인구비율.csv", encoding="euc-kr")


min_date = min(pop["Date"].unique())
max_date = max(pop["Date"].unique())

pop2=pop[pop["Sd Nm"]!="전국"]

# pop3 = pop[pop["Category1"]=="고령인구비율"].groupby(["Date", "Sd Nm"],as_index=False).mean()
# pop3 = pop3[pop3["Sd Nm"]=="전국"][["Sd Nm","Date","Value"]]


pop4 = pop[pop['Date']==max_date][pop['Category1']=='고령인구비율'][pop["Sgg Nm"]=="전체"].reset_index(drop=True)
pop6 = pop[pop['Category1']=='고령인구비율'][pop["Sgg Nm"]=="전체"].reset_index(drop=True)

# pop5 = pop.groupby(pop["Sd Nm"],as_index=False).sum()
# pop5 = pop5[pop5["Sd Nm"]!="전국"]
# pop5["Color"] = "#FFFFF"
pop5=pop6
pop_1 = pop6.copy()


geo = json.load(open("korea_geojson2.geojson", encoding="utf-8"))
for x in geo['features']:
    x['id'] = x["properties"]['CTP_KOR_NM']
for idx, _ in enumerate(geo['features']):
    print(geo['features'][idx]['id'])


#fig = px.line(pop3, x="Date", y=pop3[pop3["Sd Nm"]==s_sdnm]["Value"], markers=True)
#fig.add_annotation(x=max(pop3["Date"]), y=17, showarrow=False, text="전국{}%".format(round(pop3.reset_index()["Value"].tolist()[-1]),3),font=dict(color="#345884", size=12, family="bold"))

print("test")


fig2 = px.choropleth_mapbox(
   pop5,
   geojson=geo,
   locations='Sd Nm',
    #color="Sd Nm",
   color_continuous_scale=px.colors.sequential.Mint,
   # featureidkey="properties.CTP_KOR_NM", # featureidkey를 사용하여 id 값을 갖는 키값 지정
   mapbox_style="white-bg",
   zoom=4.5,
   center = {"lat": 35.757981, "lon": 127.661132},
   opacity=0.6,
    #width= 800,
    height=400,
   labels={'localocccnt':'Sd Cd'},

)
fig2.update_layout(mapbox_layers=[{"below":"traces","sourcetype":"raster","source":["https://api.vworld.kr/req/wmts/1.0.0/FD4FDEAD-76FF-3FF5-A158-F29B2C0A6C7D/Base/{z}/{y}/{x}.png"]}],
                   showlegend = False,
                   mapbox_accesstoken = "pk.eyJ1Ijoid2pzcXVkZG4iLCJhIjoiY2t3Mnc1YXd6MGpmdDJwcDZqa2ZtNW0yayJ9.TEQ51RPJX8z5bZEUyW5h5w",
                   #shapes=[{"x0": 0,"y0": 0,"x1": 1,"y1": 1,}],
                   margin =dict(l=10, t=10, b=10, r=10))

fig_2 = px.choropleth_mapbox(
   pop5,
   geojson=geo,
   locations='Sd Nm',
    #color="Sd Nm",
   color_continuous_scale=px.colors.sequential.Redor,
   # featureidkey="properties.CTP_KOR_NM", # featureidkey를 사용하여 id 값을 갖는 키값 지정
   mapbox_style="carto-positron",
   zoom=4.5,
   center = {"lat": 35.757981, "lon": 127.661132},
   opacity=0.6,
    #width=250,
    height=400,
   labels={'localocccnt':'Sd Cd'}

)
fig_2.update_layout(mapbox_layers=[{"below":"traces","sourcetype":"raster","source":["https://api.vworld.kr/req/wmts/1.0.0/FD4FDEAD-76FF-3FF5-A158-F29B2C0A6C7D/Base/{z}/{y}/{x}.png"]}],
                   showlegend = False,
                   mapbox_accesstoken = "pk.eyJ1Ijoid2pzcXVkZG4iLCJhIjoiY2t3Mnc1YXd6MGpmdDJwcDZqa2ZtNW0yayJ9.TEQ51RPJX8z5bZEUyW5h5w",
                    margin =dict(l=10, t=10, b=10, r=10))

fig_21 = px.choropleth_mapbox(
   pop5,
   geojson=geo,
   locations='Sd Nm',
    #color="Sd Nm",
   color_continuous_scale=px.colors.sequential.Redor,
   # featureidkey="properties.CTP_KOR_NM", # featureidkey를 사용하여 id 값을 갖는 키값 지정
   mapbox_style="carto-positron",
   zoom=4.5,
   center = {"lat": 35.757981, "lon": 127.661132},
   opacity=0.6,
    #width=250,
    height=400,
   labels={'localocccnt':'Sd Cd'}

)
fig_21.update_layout(mapbox_layers=[{"below":"traces","sourcetype":"raster","source":["https://api.vworld.kr/req/wmts/1.0.0/FD4FDEAD-76FF-3FF5-A158-F29B2C0A6C7D/Base/{z}/{y}/{x}.png"]}],
                   showlegend = False,
                   mapbox_accesstoken = "pk.eyJ1Ijoid2pzcXVkZG4iLCJhIjoiY2t3Mnc1YXd6MGpmdDJwcDZqa2ZtNW0yayJ9.TEQ51RPJX8z5bZEUyW5h5w",
                     margin =dict(l=10, t=10, b=10, r=10))

dg_pop = pop[pop["Sd Nm"] != "전국"][pop["Sgg Nm"] != "전체"]
dg_1 = dg_pop[dg_pop["Category1"] == "65세이상인구"]
dg_1.pop("Category1")
dg_1.rename(columns={"Value": "65세이상인구"}, inplace=True)
dg_2 = dg_pop[dg_pop["Category1"] == "고령인구비율"]
dg_2.pop("Category1")
dg_2.rename(columns={"Value": "고령인구비율", "Unit": "Unit2"}, inplace=True)
dg_3 = dg_pop[dg_pop["Category1"] == "전체인구"]
dg_3.pop("Category1")
dg_3.rename(columns={"Value": "전체인구", "Unit": "Unit3"}, inplace=True)
dg_merge = pd.merge(dg_1, dg_2, how="inner")
dg_merge = pd.merge(dg_merge, dg_3, how="inner")
pd.to_datetime(dg_merge["Date"])
dg_merge["SD_SGG"] = dg_merge["Sd Nm"] + " " + dg_merge["Sgg Nm"]
dgmin_x = min(dg_merge["65세이상인구"].unique())
dgmax_x = max(dg_merge["65세이상인구"].unique())
dgmin_y = min(dg_merge["고령인구비율"].unique())
dgmax_y = max(dg_merge["고령인구비율"].unique())
animations = go.Figure(px.scatter(dg_merge, x="65세이상인구", y="고령인구비율", animation_frame="Date", animation_group="Sgg Nm",
                                  size="전체인구",
                                  color="Sd Nm", log_x=True, size_max=55,range_x=[2000, 200000], range_y=[5, 50], hover_name="SD_SGG" ))



nav = dbc.Row([
        dbc.Col([
            html.Div([
                html.Div(style={"display": "inline-block", "width": "auto"}, children=[
                    html.H1(["기초통계"], style={'font-weight': "bold", "color": '#2a5783', "margin-bottom": "0px",
                                             "width": "auto", "display": "inline-block"}),
                    html.H4([" - 인구 - 고령인구비율"],
                            style={"color": '#2a5783', "display": "inline-block", "margin-bottom": "0px",
                                   "width": "auto"})]),

                html.Div(style={"display": "inline-block", "float": "right", "bottom": "0px"}, children=[
                    html.Div([": KOSIS"], style={"display": "inline-block", "float": "right"}),
                    html.Div(["출처"], style={'font-weight': "bold", "display": "inline-block", "margin-bottom": "0%",
                                            "float": "right"}),
                    html.Div(style={"clear": "both"}, children=[]),
                    html.Div(style={"display": "table-cell", "vertical-align": "center"}, children=[
                        html.Div(["기준연월"], style={'font-weight': "bold", "display": "inline-block"}),
                        html.Div([":" + f" {min_date}" + "~" + f"{max_date}"], style={"display": "inline-block"})
                    ])])
            ]),
        ])
    ])


card_1 = dbc.Card([
    dbc.CardBody([html.Div(style={"border":"3px solid #f5f5f5", "width":"49.4%", "float":"left", "box-shadow":"7px 7px 3px grey", "border-radius": "0.5em"},children=[
        html.Label(style={'font-weight':"bold","font-size":"20pt"}, children=["지역 선택"]),
        html.Hr(style={"border": "solid 1px"}, children=[]),
#        html.Div([dcc.Dropdown(id = "s_sdnm", value="전국",options=[{'label':c, 'value':c} for c in (pop["Sd Nm"].unique())])]),
        html.Div([dcc.Graph(id="map",figure=fig2)]),
    ]),

    html.Div([" "], style={"float":"left","width":"4%"}),

    html.Div(style={"border":"3px solid #f5f5f5",  "float":"right",  "width":"49.4%", "height":"100%", "box-shadow":"7px 7px 3px grey", "border-radius": "0.5em"},children=[
        html.Label(style={'font-weight':"bold","font-size":"20pt"}, children=["'고령인구비율' 통계현황"]),
        html.Hr(style={"border": "solid 1px"}, children=[]),

        html.Div(style={"clear":"both"},children=[]),

        html.Div(style={"padding":"3%"},children=[]),

        html.Div(style={"border":"2px solid #f5f5f5","float":"left", "width":"48%", "color":"#787878", "height":"110pt", "top": "5%" , "box-shadow":"5px 5px 3px grey", "border-radius": "0.5em"}, children=[
            html.H1(["기준연월"], style={"font-weight":"bold", "text-align":"center"}),
            html.Div([f"{max_date}"], style={"text-align":"center", "font-size":"20pt", "bottom":"-7%", "position":"relative"}, id="date_card")
        ]),
        html.Div(style={"border":"2px solid #f3f6f8","float":"left", "width":"48%", "margin-left":"2%","backgroundColor":"#f3f6f8", "height":"110pt", "top": "5%", "box-shadow":"5px 5px 3px grey", "border-radius": "0.5em"}, children=[
            html.H1(["전국평균"], style={"font-weight":"bold", "text-align":"center"}),
            html.Div(style={"text-align":"center", "bottom":"-7%", "position":"relative","font-size":"20pt"},id = "date_card_2")
        ]),

        html.Div(style={"clear":"both"},children=[]),

        html.Div(style={"padding": "1%"}, children=[]),

        html.Div(style={"border":"2px solid #f5f5f5","float":"left", "width":"48%", "backgroundColor":"#f3f6f8", "height":"110pt", "top": "5%" , "box-shadow":"5px 5px 3px grey", "border-radius": "0.5em"}, children=[
            html.H1([html.Span('최대',style={"color":'#2a5783'}), html.Span(id="date_card_3")], style={"font-weight":"bold", "text-align":"center"}),

            html.Div([f"{pop4.loc[pop4['Value'].idxmax()]['Sd Nm']}"], style={"text-align":"center","bottom":"-3%", "position":"relative","font-size":"15pt"},id = "date_card_4"),
            html.Div([f"{round(pop4.loc[pop4['Value'].idxmax()]['Value'],2)}" '%'],style={"text-align":"center","bottom":"-3%", "position":"relative","font-size":"15pt"},id = "date_card_5")
        ]),

        html.Div(style={"border":"2px solid #f3f6f8","float":"left", "width":"48%", "margin-left":"2%","backgroundColor":"#f3f6f8", "height":"110pt", "top": "5%", "box-shadow":"5px 5px 3px grey", "border-radius": "0.5em"}, children=[
            html.H1([html.Span('최소', style={"color": '#f29131'}), html.Span(id="date_card_6")], style={"font-weight": "bold", "text-align": "center"}),
            html.Div([f"{pop4.loc[pop4['Value'].idxmin()]['Sd Nm']}"],style={"text-align": "center","bottom":"-3%", "position":"relative","font-size":"15pt"},id = "date_card_7"),
            html.Div([f"{round(pop4.loc[pop4['Value'].idxmin()]['Value'],2)}"' %'],style={"text-align": "center","bottom":"-3%", "position":"relative","font-size":"15pt"},id = "date_card_8")
        ])
    ]),

        ])])



card_2 = dbc.Card([
    dbc.CardBody([
        html.Div(style={"border":"3px solid #f5f5f5", "width":"49.4%", "float":"left", "box-shadow":"7px 7px 3px grey", "border-radius": "0.5em"},children=[
        html.Label(style={'font-weight':"bold","font-size":"20pt"}, children=["지역 선택"]),
        html.Hr(style={"border": "solid 1px"}, children=[]),
        html.Div([dcc.Graph(id="map_2",figure=fig_2,style={"width":"48%","float":"left"})]),
        html.Div([dcc.Graph(id="map__2",figure=fig_21,style={"width":"48%","float":"left"})]),

    ]),

    html.Div([" "], style={"float":"left","width":"4%"}),

    html.Div(style={"border":"3px solid #f5f5f5",  "float":"right",  "width":"49.4%", "height":"100%", "box-shadow":"7px 7px 3px grey", "border-radius": "0.5em"},children=[
        html.Label(style={'font-weight':"bold","font-size":"20pt"}, children=["'고령인구비율' 통계현황"]),
        html.Hr(style={"border": "solid 1px"}, children=[]),

        html.Div(style={"clear":"both"},children=[]),

        html.Div(style={"padding":"3%"},children=[]),

        html.Div(style={"border":"2px solid #f5f5f5","float":"left", "width":"48%", "color":"#787878", "height":"110pt", "top": "5%" , "box-shadow":"5px 5px 3px grey", "border-radius": "0.5em"}, children=[
            html.H1(["기준연월"], style={"font-weight":"bold", "text-align":"center"}),
            html.Div([f"{max_date}"], style={"text-align":"center", "font-size":"20pt", "bottom":"-7%", "position":"relative"}, id="date_card2")
        ]),
        html.Div(style={"border":"2px solid #f3f6f8","float":"left", "width":"48%", "margin-left":"2%","backgroundColor":"#f3f6f8", "height":"110pt", "top": "5%", "box-shadow":"5px 5px 3px grey", "border-radius": "0.5em"}, children=[
            html.H1(["전국평균"], style={"font-weight":"bold", "text-align":"center"}),
            html.Div(style={"text-align":"center", "bottom":"-7%", "position":"relative","font-size":"20pt"}, id ="date_card2_2")
        ]),

        html.Div(style={"clear":"both"},children=[]),

        html.Div(style={"padding": "1%"}, children=[]),

        html.Div(style={"border":"2px solid #f5f5f5","float":"left", "width":"48%", "backgroundColor":"#f3f6f8", "height":"110pt", "top": "5%" , "box-shadow":"5px 5px 3px grey", "border-radius": "0.5em"}, children=[
            html.H1([html.Span('최대',style={"color":'#2a5783'}), html.Span(id="date_card2_3")], style={"font-weight":"bold", "text-align":"center"}),
            html.Div([f"{pop4.loc[pop4['Value'].idxmax()]['Sd Nm']}"], style={"text-align":"center","bottom":"-3%", "position":"relative","font-size":"15pt"}, id="date_card2_4"),
            html.Div([f"{round(pop4.loc[pop4['Value'].idxmax()]['Value'],2)}" '%'],style={"text-align":"center","bottom":"-3%", "position":"relative","font-size":"15pt"},id="date_card2_5")
        ]),

        html.Div(style={"border":"2px solid #f3f6f8","float":"left", "width":"48%", "margin-left":"2%","backgroundColor":"#f3f6f8", "height":"110pt", "top": "5%", "box-shadow":"5px 5px 3px grey", "border-radius": "0.5em"}, children=[
            html.H1([html.Span('최소', style={"color": '#f29131'}), html.Span(id="date_card2_6")], style={"font-weight": "bold", "text-align": "center"}),
            html.Div([f"{pop4.loc[pop4['Value'].idxmin()]['Sd Nm']}"],style={"text-align": "center","bottom":"-3%", "position":"relative","font-size":"15pt"},id="date_card2_7"),
            html.Div([f"{round(pop4.loc[pop4['Value'].idxmin()]['Value'],2)}"' %'],style={"text-align": "center","bottom":"-3%", "position":"relative","font-size":"15pt"}, id="date_card2_8")
        ])
    ]),

        ])])

card_3 = dbc.Card([
    dbc.CardBody(style = {"box-shadow":"7px 7px 3px grey", "border-radius": "0.5em"}, children=[
        dbc.Col([
                html.Label("'고령인구비율' 연월별 현황",style={'font-weight': "bold", "font-size":"20pt"}),
                html.Label("*연월선택시 해당 연월의 값으로 변경", style={"float":"right", "display": "inline-block", "font-size":"10pt"})]),
            dbc.Row(dcc.Graph(id="line_chart_2"))
    ])
])


card_4 = dbc.Card([
    dbc.CardBody(style = {"box-shadow":"7px 7px 3px grey", "border-radius": "0.5em"}, children=[
        dbc.Col([
            html.Label("'고령인구비율' 연월별 현황", style={ 'font-weight': "bold", "font-size":"20pt"}),
            html.Label("*연월선택시 해당 연월의 값으로 변경", style={"float": "right", "display": "inline-block", "font-size":"10pt" })]),
        dbc.Row([dcc.Graph(id="line_chart_3")])
    ])
])



card_5 = dbc.Card([
    dbc.CardBody(style = {"box-shadow":"7px 7px 3px grey", "border-radius": "0.5em"}, children=[
        html.H4("애니메이션 테스트"),
        html.P("65-고령",id="selection"),
        dcc.Loading(dcc.Graph(figure=animations),type="cube")
])])


tab1 = dbc.Card(
        dbc.CardBody(style = {"box-shadow":"7px 7px 3px grey", "border-radius": "0.5em"}, children=[
html.Button("모든 선택 취소", id="reset", style={ "border":"2px solid #2a5783","backgroundColor":"white", "font-weight":"bold" }),
            dbc.Row(card_1),
            html.Br(),
            card_3,
            html.Br(),
            card_5
            ])
    )


tab2 = dbc.Card(
        dbc.CardBody(style = {"box-shadow":"7px 7px 3px grey", "border-radius": "0.5em"}, children=[
html.Button("모든 선택 취소", id="reset_2", style={ "border":"2px solid #2a5783", "backgroundColor":"white","font-weight":"bold"}),
            dbc.Row(card_2),
            html.Br(),
            card_4
            # dbc.Col([
            #     html.Label("'고령인구비율' 연월별 현황", style={"float": "left",'font-weight': "bold"}),
            #     html.Label("*연월선택시 해당 연월의 값으로 변경", style={"float": "right", "display": "inline-block", })]),
            # dbc.Row([dcc.Graph(id="line_chart_3")])
            ])
    )






server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])
#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.title = "고령화 인구"
server = app.server

colors = {
    'background': 'white',
    'back' : "#f3f6f8",
    'text': '#2a5783'
}

app.layout = dbc.Container([
    nav,
    html.Br(),
    dbc.Tabs([
        dbc.Tab(tab1, label="단일"),
        dbc.Tab(tab2, label="비교"),
        #dbc.Tab(tab2, label="비교")
    ])
],fluid=True)

@app.callback([Output('line_chart_2','figure'),
               Output('date_card','children'),
               Output('date_card_2','children'),
               Output('date_card_3','children'),
               Output('date_card_4','children'),
               Output('date_card_5','children'),
               Output('date_card_6','children'),
               Output('date_card_7','children'),
               Output('date_card_8','children'),],
              [Input('map','clickData'),
               Input('line_chart_2','clickData')])
def update_map(map_dt, clickData, pop_date=None):
    ctx = dash.callback_context
    if clickData is None:
        a = max(pop["Date"].unique())
        if not ctx.triggered:
            pop_date = pop[pop['Date'] == a][pop['Category1'] == '고령인구비율'][pop["Sgg Nm"] == "전체"].reset_index(drop=True)
            map_dt = "전국"
            sd_sgg = " 시도"
            pop_1 = pop[pop["Category1"] == "고령인구비율"]
            pop_2 = pop_1[pop_1["Sgg Nm"] == "전체"]
            pop_3 = pop_1[pop_1["Sgg Nm"] == "전국"]
            pop_4 = pd.concat([pop_2, pop_3])
            pop_map = pop_4[pop_4["Sd Nm"] == "전국"][["Sd Nm", "Date", "Value"]]
            fig_7 = px.line(pop_map, x=pop_map["Date"], y=pop_map["Value"], markers=True)
            Sd_1 = round(pop_map.reset_index()["Value"].tolist()[-1], 2)
            fig_7.add_annotation(x=max(pop_map["Date"]), y=Sd_1, showarrow=False, text=f"{map_dt}{Sd_1}%",
                                     font=dict(color="#345884", size=12, family="bold"))
            fig_7.layout.plot_bgcolor = "white"
            fig_7.update_layout(yaxis_title=None, xaxis_title=None)
            #fig_7.layout.paper_bgcolor = "white"

            return fig_7, \
                   a, \
                   f"{round(pop[pop['Date'] == a][pop['Sd Nm'] == '전국'][pop['Category1'] == '고령인구비율']['Value'].iloc[0], 2)}" + " %", \
                   sd_sgg, \
                   f"{pop_date.loc[pop_date['Value'].idxmax()]['Sd Nm']}", \
                   f"{round(pop_date.loc[pop_date['Value'].idxmax()]['Value'], 2)}" '%', \
                   sd_sgg,\
                   f"{pop_date.loc[pop_date['Value'].idxmin()]['Sd Nm']}", \
                   f"{round(pop_date.loc[pop_date['Value'].idxmin()]['Value'], 2)}"' %'

        elif ctx.triggered and "clickData" in ctx.triggered[0]["prop_id"]:
            try :
                map_dt = ctx.inputs["map.clickData"]["points"][0]["location"]
                sd_sgg = " 시군구"
            except :
                map_dt = "전국"
                sd_sgg = " 시도"
            pop_date = pop[pop['Date'] == a][pop['Category1'] == '고령인구비율'][pop["Sd Nm"]==map_dt][pop["Sgg Nm"] != "전체"].reset_index(drop=True)
            pop_1 = pop[pop["Category1"] == "고령인구비율"]
            pop_2 = pop_1[pop_1["Sgg Nm"] == "전체"]
            pop_3 = pop_1[pop_1["Sgg Nm"] == "전국"]
            pop_4 = pd.concat([pop_2, pop_3])
            pop_map2 = pop_4[pop_4["Sd Nm"] == map_dt][["Sd Nm", "Date", "Value"]]
            fig_7 = px.line(pop_map2, x=pop_map2["Date"], y=pop_map2["Value"], markers=True)
            Sd_1 = round(pop_map2.reset_index()["Value"].tolist()[-1], 2)
            fig_7.add_annotation(x=max(pop_map2["Date"]), y=Sd_1, showarrow=False, text=f"{map_dt}{Sd_1}%",
                                 font=dict(color="#345884", size=12, family="bold"))
            fig_7.layout.plot_bgcolor = "white"
            fig_7.update_layout(yaxis_title=None, xaxis_title=None)

            #fig_7.layout.paper_bgcolor = "white"
            return fig_7, \
                   a, \
                   f"{round(pop[pop['Date'] == a][pop['Sd Nm'] == '전국'][pop['Category1'] == '고령인구비율']['Value'].iloc[0], 2)}" + " %", \
                   sd_sgg, \
                   f"{pop_date.loc[pop_date['Value'].idxmax()]['Sgg Nm']}", \
                   f"{round(pop_date.loc[pop_date['Value'].idxmax()]['Value'], 2)}" '%', \
                   sd_sgg,\
                   f"{pop_date.loc[pop_date['Value'].idxmin()]['Sgg Nm']}", \
                   f"{round(pop_date.loc[pop_date['Value'].idxmin()]['Value'], 2)}"' %'

    elif clickData is not None:
        a = clickData
        try :
            a = a["points"][0]["x"]
        except KeyError:
            a  = max(pop["Date"].unique())
        if not ctx.triggered:
            pop_date = pop[pop['Date'] == a][pop['Category1'] == '고령인구비율'][pop["Sgg Nm"] == "전체"].reset_index(drop=True)
            map_dt = "전국"
            sd_sgg = " 시도"
            pop_1 = pop[pop["Category1"] == "고령인구비율"]
            pop_2 = pop_1[pop_1["Sgg Nm"] == "전체"]
            pop_3 = pop_1[pop_1["Sgg Nm"] == "전국"]
            pop_4 = pd.concat([pop_2, pop_3])
            pop_map = pop_4[pop_4["Sd Nm"] == "전국"][["Sd Nm", "Date", "Value"]]
            fig_7 = px.line(pop_map, x=pop_map["Date"], y=pop_map["Value"], markers=True)
            Sd_1 = round(pop_map.reset_index()["Value"].tolist()[-1], 2)
            fig_7.add_annotation(x=max(pop_map["Date"]), y=Sd_1, showarrow=False, text=f"{map_dt}{Sd_1}%",
                                 font=dict(color="#345884", size=12, family="bold"))
            fig_7.layout.plot_bgcolor = "white"
            fig_7.update_layout(yaxis_title=None, xaxis_title=None)

            #fig_7.layout.paper_bgcolor = "white"

            return fig_7, \
                   a, \
                   f"{round(pop[pop['Date'] == a][pop['Sd Nm'] == '전국'][pop['Category1'] == '고령인구비율']['Value'].iloc[0], 2)}" + " %", \
                   sd_sgg, \
                   f"{pop_date.loc[pop_date['Value'].idxmax()]['Sd Nm']}", \
                   f"{round(pop_date.loc[pop_date['Value'].idxmax()]['Value'], 2)}" '%', \
                   sd_sgg,\
                   f"{pop_date.loc[pop_date['Value'].idxmin()]['Sd Nm']}", \
                   f"{round(pop_date.loc[pop_date['Value'].idxmin()]['Value'], 2)}"' %'
        elif ctx.triggered and "clickData" in ctx.triggered[0]["prop_id"]:
            sd_sgg = " 시군구"
            try :
                map_dt = ctx.inputs["map.clickData"]["points"][0]["location"]
                pop_date = pop[pop['Date'] == a][pop['Category1'] == '고령인구비율'][pop["Sd " \
                                                                                   "Nm"] == map_dt][pop["Sgg Nm"] != "전체"].reset_index(drop=True)
                max_sd = f"{pop_date.loc[pop_date['Value'].idxmax()]['Sgg Nm']}"
                min_sd = f"{pop_date.loc[pop_date['Value'].idxmin()]['Sgg Nm']}"
                pop_1 = pop[pop["Category1"] == "고령인구비율"]
                pop_2 = pop_1[pop_1["Sgg Nm"] == "전체"]
                pop_3 = pop_1[pop_1["Sgg Nm"] == "전국"]
                pop_4 = pd.concat([pop_2, pop_3])
                pop_map2 = pop_4[pop_4["Sd Nm"] == map_dt][["Sd Nm", "Date", "Value"]]
                fig_7 = px.line(pop_map2, x=pop_map2["Date"], y=pop_map2["Value"], markers=True)
                Sd_1 = round(pop_map2.reset_index()["Value"].tolist()[-1], 2)
                fig_7.add_annotation(x=max(pop_map2["Date"]), y=Sd_1, showarrow=False, text=f"{map_dt}{Sd_1}%",
                                     font=dict(color="#345884", size=12, family="bold"))
                fig_7.layout.plot_bgcolor = "white"
                fig_7.update_layout(yaxis_title=None, xaxis_title=None)

            except TypeError:
                map_dt = "전국"
                pop_date = pop[pop['Date'] == a][pop['Category1'] == '고령인구비율'][pop["Sgg Nm"] == "전체"].reset_index(drop=True)
                sd_sgg = " 시도"
                max_sd = f"{pop_date.loc[pop_date['Value'].idxmax()]['Sd Nm']}"
                min_sd = f"{pop_date.loc[pop_date['Value'].idxmin()]['Sd Nm']}"
                pop_1 = pop[pop["Category1"] == "고령인구비율"]
                pop_2 = pop_1[pop_1["Sgg Nm"] == "전체"]
                pop_3 = pop_1[pop_1["Sgg Nm"] == "전국"]
                pop_4 = pd.concat([pop_2, pop_3])
                pop_map = pop_4[pop_4["Sd Nm"] == "전국"][["Sd Nm", "Date", "Value"]]
                fig_7 = px.line(pop_map, x=pop_map["Date"], y=pop_map["Value"], markers=True)
                Sd_1 = round(pop_map.reset_index()["Value"].tolist()[-1], 2)
                fig_7.add_annotation(x=max(pop_map["Date"]), y=Sd_1, showarrow=False, text=f"{map_dt}{Sd_1}%",
                                     font=dict(color="#345884", size=12, family="bold"))
                fig_7.layout.plot_bgcolor = "white"
                fig_7.update_layout(yaxis_title=None, xaxis_title=None)



            return fig_7, \
                   a, \
                   f"{round(pop[pop['Date'] == a][pop['Sd Nm'] == '전국'][pop['Category1'] == '고령인구비율']['Value'].iloc[0], 2)}" + " %", \
                   sd_sgg, \
                   max_sd, \
                   f"{round(pop_date.loc[pop_date['Value'].idxmax()]['Value'], 2)}" '%', \
                   sd_sgg,\
                   min_sd, \
                   f"{round(pop_date.loc[pop_date['Value'].idxmin()]['Value'], 2)}"' %'


@app.callback([Output('map', 'clickData'),
               Output('line_chart_2', 'clickData')],
Input('reset', 'n_clicks'))

def reset_clickData(n_clicks):
    sgg_cd = " 시도"
    ctx = dash.callback_context
    a = max(pop["Date"].unique())
    pop_date = pop[pop['Date'] == a][pop['Category1'] == '고령인구비율'][pop["Sgg Nm"] == "전체"].reset_index(drop=True)
    map_dt = "전국"
    pop_1 = pop[pop["Category1"] == "고령인구비율"]
    pop_2 = pop_1[pop_1["Sgg Nm"] == "전체"]
    pop_3 = pop_1[pop_1["Sgg Nm"] == "전국"]
    pop_4 = pd.concat([pop_2, pop_3])
    pop_map = pop_4[pop_4["Sd Nm"] == "전국"][["Sd Nm", "Date", "Value"]]
    fig_7 = px.line(pop_map, x=pop_map["Date"], y=pop_map["Value"], markers=True)
    Sd_1 = round(pop_map.reset_index()["Value"].tolist()[-1], 2)
    fig_7.add_annotation(x=max(pop_map["Date"]), y=Sd_1, showarrow=False, text=f"{map_dt}{Sd_1}%",
                         font=dict(color="#345884", size=12, family="bold"))
    fig_7.layout.plot_bgcolor = "white"
    fig_7.update_layout(yaxis_title=None, xaxis_title=None)

    return None,\
           fig_7

#=================tab 구분선===========================================


@app.callback([Output('line_chart_3','figure'),
               Output('date_card2','children'),
               Output('date_card2_2','children'),
               Output('date_card2_3','children'),
               Output('date_card2_4','children'),
               Output('date_card2_5','children'),
               Output('date_card2_6','children'),
               Output('date_card2_7','children'),
               Output('date_card2_8','children')],
              [Input('map_2','clickData'),
               Input('map__2','clickData'),
               Input('line_chart_3','clickData')])


def update_map( map_dt, map_dt2, clickData):
    ctx = dash.callback_context
    if clickData is None:
        a = max(pop["Date"].unique())

        if not ctx.triggered:
            map_dt = "전국"
            map_dt2 = "전국"
            sd_sgg_2 = " 시도"
            pop_date = pop[pop['Date'] == a][pop['Category1'] == '고령인구비율'][pop["Sgg Nm"] == "전체"].reset_index(drop=True)
            pop_1 = pop[pop["Category1"] == "고령인구비율"]
            pop_2 = pop_1[pop_1["Sgg Nm"] == "전체"]
            pop_3 = pop_1[pop_1["Sgg Nm"] == "전국"]
            pop_4 = pd.concat([pop_2, pop_3])
            pop_map = pop_4[pop_4["Sd Nm"] == map_dt][["Sd Nm", "Date", "Value"]]
            pop_map4= pop_4[pop_4["Sd Nm"] == map_dt2][["Sd Nm", "Date", "Value"]]
            fig_7 = go.Figure({"layout":{"uirevision" : True, "margin":dict(t=60)}})
            fig_7.add_trace(go.Scatter(x=pop_map["Date"], y=pop_map["Value"],mode='lines+markers',showlegend=False))
            fig_7.add_trace(go.Scatter(x=pop_map4["Date"], y=pop_map4["Value"],mode='lines+markers',showlegend=False))
            #fig_7 = px.line(pop_map, x=pop_map["Date"], y=pop_map["Value"], markers=True)
            Sd_1 = round(pop_map.reset_index()["Value"].tolist()[-1], 2)
            fig_7.add_annotation(x=max(pop_map["Date"]), y=Sd_1, showarrow=False, text=f"{map_dt}{Sd_1}%",
                                 font=dict(color="#345884", size=12, family="bold"))
            Sd_2 = round(pop_map4.reset_index()["Value"].tolist()[-1],2)
            fig_7.add_annotation(x=max(pop_map4["Date"]), y=Sd_2, showarrow=False, text=f"{map_dt2}{Sd_2}%",font=dict(color="#345884", size=12, family="bold"))
            fig_7.layout.plot_bgcolor = "white"
            #fig_7.layout.paper_bgcolor = "white"

            # fig.add_annotation(x=max(pop3["Date"]), y=17, showarrow=False, text="전국{}%".format(round(pop3.reset_index()["Value"].tolist()[-1]),3),font=dict(color="#345884", size=12, family="bold"))
            return fig_7,\
                   a, \
                   f"{round(pop[pop['Date'] == a][pop['Sd Nm'] == '전국'][pop['Category1'] == '고령인구비율']['Value'].iloc[0], 2)}" + " %", \
                   sd_sgg_2, \
                   f"{pop_date.loc[pop_date['Value'].idxmax()]['Sd Nm']}", \
                   f"{round(pop_date.loc[pop_date['Value'].idxmax()]['Value'], 2)}" '%', \
                   sd_sgg_2,\
                   f"{pop_date.loc[pop_date['Value'].idxmin()]['Sd Nm']}", \
                   f"{round(pop_date.loc[pop_date['Value'].idxmin()]['Value'], 2)}"' %'


        elif ctx.triggered and "clickData" in ctx.triggered[0]["prop_id"] :
            map_dt = "전국"
            map_dt2 = "전국"
            try:
                map_dt = ctx.inputs["map_2.clickData"]["points"][0]["location"]
            except TypeError:
                map_dt="전국"
            try:
                map_dt2 = ctx.inputs["map__2.clickData"]["points"][0]["location"]
            except TypeError:
                map_dt2="전국"
            pop_date = pop[pop['Date'] == a][pop['Category1'] == '고령인구비율'][pop["Sd Nm"] == map_dt][pop["Sgg Nm"] != "전체"].reset_index(drop=True)
            max_date2_1 = f"{pop_date.loc[pop_date['Value'].idxmax()]['Sgg Nm']}"
            max_date2_2 = f"{round(pop_date.loc[pop_date['Value'].idxmax()]['Value'], 2)}" '%',
            min_date2_1 = f"{pop_date.loc[pop_date['Value'].idxmin()]['Sgg Nm']}"
            min_date2_2 = f"{round(pop_date.loc[pop_date['Value'].idxmin()]['Value'], 2)}" '%',
            if map_dt == "전국":
                sd_sgg_2 = " 시도"
                pop_date_2 = pop[pop['Date'] == a][pop['Category1'] == '고령인구비율'][pop["Sgg Nm"] == "전체"].reset_index(drop=True)
                max_date2_1 = f"{pop_date_2.loc[pop_date_2['Value'].idxmax()]['Sd Nm']}"
                max_date2_2 = f"{round(pop_date_2.loc[pop_date_2['Value'].idxmax()]['Value'], 2)}" '%'

                min_date2_1 = f"{pop_date_2.loc[pop_date_2['Value'].idxmin()]['Sd Nm']}"
                min_date2_2 = f"{round(pop_date_2.loc[pop_date_2['Value'].idxmin()]['Value'], 2)}"' %'
            sd_sgg_2 = " 시군구"
            if map_dt == "전국":
                sd_sgg_2 = " 시도"
                pop_date = pop[pop['Date'] == a][pop['Category1'] == '고령인구비율'][pop["Sgg Nm"] == "전체"].reset_index(drop=True)
            pop_1 = pop[pop["Category1"] == "고령인구비율"]
            pop_2 = pop_1[pop_1["Sgg Nm"] == "전체"]
            pop_3 = pop_1[pop_1["Sgg Nm"] == "전국"]
            pop_4 = pd.concat([pop_2, pop_3])
            pop_map2 = pop_4[pop_4["Sd Nm"] == map_dt][["Sd Nm", "Date", "Value"]]
            pop_map3 = pop_4[pop_4["Sd Nm"] == map_dt2][["Sd Nm", "Date", "Value"]]
            fig_7 = go.Figure({"layout":{"uirevision" : True, "margin":dict(t=60)}})
            fig_7.add_trace(go.Scatter(x=pop_map2["Date"], y=pop_map2["Value"],mode='lines+markers',showlegend=False))
            fig_7.add_trace(go.Scatter(x=pop_map3["Date"], y=pop_map3["Value"],mode='lines+markers',showlegend=False))
            #fig_7 = px.line(pop_map2, x=pop_map2["Date"], y=pop_map2["Value"], markers=True)
            Sd_1 = round(pop_map2.reset_index()["Value"].tolist()[-1],2)
            fig_7.add_annotation(x=max(pop_map2["Date"]), y=Sd_1, showarrow=False, text=f"{map_dt}{Sd_1}%",font=dict(color="#345884", size=12, family="bold"))
            Sd_2 = round(pop_map3.reset_index()["Value"].tolist()[-1],2)
            fig_7.add_annotation(x=max(pop_map3["Date"]), y=Sd_2, showarrow=False, text=f"{map_dt2}{Sd_2}%",font=dict(color="#345884", size=12, family="bold"))

            fig_7.layout.plot_bgcolor = "white"
            #fig_7.layout.paper_bgcolor = "white"

            #fig.add_annotation(x=max(pop3["Date"]), y=17, showarrow=False, text="전국{}%".format(round(pop3.reset_index()["Value"].tolist()[-1]),3),font=dict(color="#345884", size=12, family="bold"))
            return fig_7,\
                   a, \
                   f"{round(pop[pop['Date'] == a][pop['Sd Nm'] == '전국'][pop['Category1'] == '고령인구비율']['Value'].iloc[0], 2)}" + " %", \
                   sd_sgg_2, \
                   max_date2_1, \
                   max_date2_2, \
                   sd_sgg_2, \
                   min_date2_1, \
                   min_date2_2

    elif clickData is not None:
        a = clickData
        try :
            a = a["points"][0]["x"]
        except KeyError:
            a  = max(pop["Date"].unique())
        if not ctx.triggered:
            map_dt = "전국"
            map_dt2 = "전국"
            sd_sgg_2 = " 시도"
            pop_date = pop[pop['Date'] == a][pop['Category1'] == '고령인구비율'][pop["Sgg Nm"] == "전체"].reset_index(drop=True)
            pop_1 = pop[pop["Category1"] == "고령인구비율"]
            pop_2 = pop_1[pop_1["Sgg Nm"] == "전체"]
            pop_3 = pop_1[pop_1["Sgg Nm"] == "전국"]
            pop_4 = pd.concat([pop_2, pop_3])
            pop_map = pop_4[pop_4["Sd Nm"] == map_dt][["Sd Nm", "Date", "Value"]]
            pop_map4 = pop_4[pop_4["Sd Nm"] == map_dt2][["Sd Nm", "Date", "Value"]]
            fig_7 = go.Figure({"layout":{"uirevision" : True, "margin":dict(t=60)}})
            fig_7.add_trace(
                go.Scatter(x=pop_map["Date"], y=pop_map["Value"], mode='lines+markers', showlegend=False))
            fig_7.add_trace(
                go.Scatter(x=pop_map4["Date"], y=pop_map4["Value"], mode='lines+markers', showlegend=False))
            # fig_7 = px.line(pop_map, x=pop_map["Date"], y=pop_map["Value"], markers=True)
            Sd_1 = round(pop_map.reset_index()["Value"].tolist()[-1], 2)
            fig_7.add_annotation(x=max(pop_map["Date"]), y=Sd_1, showarrow=False, text=f"{map_dt}{Sd_1}%",
                                 font=dict(color="#345884", size=12, family="bold"))
            Sd_2 = round(pop_map4.reset_index()["Value"].tolist()[-1], 2)
            fig_7.add_annotation(x=max(pop_map4["Date"]), y=Sd_2, showarrow=False, text=f"{map_dt2}{Sd_2}%",
                                 font=dict(color="#345884", size=12, family="bold"))

            fig_7.layout.plot_bgcolor = "white"
            #fig_7.layout.paper_bgcolor = "white"

            # fig.add_annotation(x=max(pop3["Date"]), y=17, showarrow=False, text="전국{}%".format(round(pop3.reset_index()["Value"].tolist()[-1]),3),font=dict(color="#345884", size=12, family="bold"))
            return fig_7, \
                   a, \
                   f"{round(pop[pop['Date'] == a][pop['Sd Nm'] == '전국'][pop['Category1'] == '고령인구비율']['Value'].iloc[0], 2)}" + " %", \
                   sd_sgg_2, \
                   f"{pop_date.loc[pop_date['Value'].idxmax()]['Sd Nm']}", \
                   f"{round(pop_date.loc[pop_date['Value'].idxmax()]['Value'], 2)}" '%', \
                   sd_sgg_2, \
                   f"{pop_date.loc[pop_date['Value'].idxmin()]['Sd Nm']}", \
                   f"{round(pop_date.loc[pop_date['Value'].idxmin()]['Value'], 2)}"' %'


        elif ctx.triggered and "clickData" in ctx.triggered[0]["prop_id"]:
            map_dt = "전국"
            map_dt2 = "전국"
            try:
                map_dt = ctx.inputs["map_2.clickData"]["points"][0]["location"]
            except TypeError:
                map_dt = "전국"
                #sd_sgg_2 = " 시도"
            try:
                map_dt2 = ctx.inputs["map__2.clickData"]["points"][0]["location"]
            except TypeError:
                map_dt2 = "전국"
                #sd_sgg_2 = " 시군구"
            pop_date = pop[pop['Date'] == a][pop['Category1'] == '고령인구비율'][pop["Sd Nm"] == map_dt][pop["Sgg Nm"] != "전체"].reset_index(drop=True)
            sd_sgg_2 = " 시군구"
            max_date2_1 = f"{pop_date.loc[pop_date['Value'].idxmax()]['Sgg Nm']}"
            max_date2_2 = f"{round(pop_date.loc[pop_date['Value'].idxmax()]['Value'], 2)}" '%',
            min_date2_1 = f"{pop_date.loc[pop_date['Value'].idxmin()]['Sgg Nm']}"
            min_date2_2 = f"{round(pop_date.loc[pop_date['Value'].idxmin()]['Value'], 2)}" '%',
            if map_dt == "전국":
                sd_sgg_2 = " 시도"
                pop_date_2 = pop[pop['Date'] == a][pop['Category1'] == '고령인구비율'][pop["Sgg Nm"] == "전체"].reset_index(drop=True)
                max_date2_1 = f"{pop_date_2.loc[pop_date_2['Value'].idxmax()]['Sd Nm']}"
                max_date2_2 = f"{round(pop_date_2.loc[pop_date_2['Value'].idxmax()]['Value'], 2)}" '%'

                min_date2_1 = f"{pop_date_2.loc[pop_date_2['Value'].idxmin()]['Sd Nm']}"
                min_date2_2 = f"{round(pop_date_2.loc[pop_date_2['Value'].idxmin()]['Value'], 2)}"' %'

            pop_1 = pop[pop["Category1"] == "고령인구비율"]
            pop_2 = pop_1[pop_1["Sgg Nm"] == "전체"]
            pop_3 = pop_1[pop_1["Sgg Nm"] == "전국"]
            pop_4 = pd.concat([pop_2, pop_3])
            pop_map2 = pop_4[pop_4["Sd Nm"] == map_dt][["Sd Nm", "Date", "Value"]]
            pop_map3 = pop_4[pop_4["Sd Nm"] == map_dt2][["Sd Nm", "Date", "Value"]]
            fig_7 = go.Figure({"layout":{"uirevision" : True, "margin":dict(t=60)}})
            fig_7.add_trace(
                go.Scatter(x=pop_map2["Date"], y=pop_map2["Value"], mode='lines+markers', showlegend=False))
            fig_7.add_trace(
                go.Scatter(x=pop_map3["Date"], y=pop_map3["Value"], mode='lines+markers', showlegend=False))
            # fig_7 = px.line(pop_map2, x=pop_map2["Date"], y=pop_map2["Value"], markers=True)
            Sd_1 = round(pop_map2.reset_index()["Value"].tolist()[-1], 2)
            fig_7.add_annotation(x=max(pop_map2["Date"]), y=Sd_1, showarrow=False, text=f"{map_dt}{Sd_1}%",
                                 font=dict(color="#345884", size=12, family="bold"))
            Sd_2 = round(pop_map3.reset_index()["Value"].tolist()[-1], 2)
            fig_7.add_annotation(x=max(pop_map3["Date"]), y=Sd_2, showarrow=False, text=f"{map_dt2}{Sd_2}%",
                                 font=dict(color="#345884", size=12, family="bold"))
            fig_7.layout.plot_bgcolor = "white"
            #fig_7.layout.paper_bgcolor = "white"

            # fig.add_annotation(x=max(pop3["Date"]), y=17, showarrow=False, text="전국{}%".format(round(pop3.reset_index()["Value"].tolist()[-1]),3),font=dict(color="#345884", size=12, family="bold"))
            return fig_7, \
                   a, \
                   f"{round(pop[pop['Date'] == a][pop['Sd Nm'] == '전국'][pop['Category1'] == '고령인구비율']['Value'].iloc[0], 2)}" + " %", \
                   sd_sgg_2, \
                   max_date2_1, \
                   max_date2_2, \
                   sd_sgg_2, \
                   min_date2_1, \
                   min_date2_2

@app.callback([Output('map_2','clickData'),
               Output('map__2','clickData'),
               Output('line_chart_3','clickData')],
               [Input('reset_2',"n_clicks")])

def reset_2_clickData(n_clicks):
    a = max(pop["Date"].unique())
    map_dt = "전국"
    map_dt2 = "전국"
    sd_sgg_2 = " 시도"
    pop_date = pop[pop['Date'] == a][pop['Category1'] == '고령인구비율'][pop["Sgg Nm"] == "전체"].reset_index(drop=True)
    pop_1 = pop[pop["Category1"] == "고령인구비율"]
    pop_2 = pop_1[pop_1["Sgg Nm"] == "전체"]
    pop_3 = pop_1[pop_1["Sgg Nm"] == "전국"]
    pop_4 = pd.concat([pop_2, pop_3])
    pop_map = pop_4[pop_4["Sd Nm"] == map_dt][["Sd Nm", "Date", "Value"]]
    pop_map4 = pop_4[pop_4["Sd Nm"] == map_dt2][["Sd Nm", "Date", "Value"]]
    fig_7 = go.Figure({"layout": {"uirevision": True, "margin": dict(t=60)}})
    fig_7.add_trace(go.Scatter(x=pop_map["Date"], y=pop_map["Value"], mode='lines+markers', showlegend=False))
    fig_7.add_trace(go.Scatter(x=pop_map4["Date"], y=pop_map4["Value"], mode='lines+markers', showlegend=False))
    # fig_7 = px.line(pop_map, x=pop_map["Date"], y=pop_map["Value"], markers=True)
    Sd_1 = round(pop_map.reset_index()["Value"].tolist()[-1], 2)
    fig_7.add_annotation(x=max(pop_map["Date"]), y=Sd_1, showarrow=False, text=f"{map_dt}{Sd_1}%",
                         font=dict(color="#345884", size=12, family="bold"))
    Sd_2 = round(pop_map4.reset_index()["Value"].tolist()[-1], 2)
    fig_7.add_annotation(x=max(pop_map4["Date"]), y=Sd_2, showarrow=False, text=f"{map_dt2}{Sd_2}%",
                         font=dict(color="#345884", size=12, family="bold"))
    fig_7.layout.plot_bgcolor = "white"

    return None,\
           None,\
           fig_7



if __name__ == "__main__":
    app.run_server(debug=True)



