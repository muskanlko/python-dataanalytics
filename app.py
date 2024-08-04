import streamlit as st
import pandas as pd
import plotly.express as px

# ui configuration
st.set_page_config(
    page_title='Pokemon App',
    page_icon='🐰',
    layout='wide',
)


# load data
@st.cache_data
def load_data():
    return pd.read_csv('pokemon.csv',index_col='#')

# ui intergration
with st.spinner('loading dataset...'):
    df=load_data()
    st.balloons()

st.title('pokemon data analytics')
st.subheader('A simple data app to analyze pokemon data')

st.sidebar.title('Menu')
choice=st.sidebar.radio('Options',['View Data',"Visualize Data"])

if choice=='View Data':
    st.header('View Dataset')
    st.dataframe(df)
else:
    st.header('Visualization')
    cat_cols=df.select_dtypes(include='object').columns.tolist()
    num_cols=df.select_dtype(exclude='object').columns.tolist()
    cat_cols.remove('name')
    num_cols.remove('generation')
    num_cols.remove('legendary')
    cat_cols.append('generation')
    cat_cols.append('legendary')

    snum_col=st.sidebar.selectbox('select a numeric column',num_cols)
    scat_col=st.sidebar.selectbox('select a categorical column',cat_cols)

    c1,c2=st.columns(2)
    #visualize numerical column
    fig1=px.histogram(df,
                      x=snum_col,
                      title=f'distribution of {snum_col}'
    )
    # visualization categorical column
    fig2=px.pie(df,
                names=scat_col,
                title=f"distribution of {scat_col}",
                hole=0.3
)
c1.plotly_chart(fig1)
c2.plotly_chart(fig2)

fig3=px.box(df,x=scat_col,y=snum_col,title=f'{snum_col}by{scat_col}')
st.plotly_chart(fig3)

fig4=px.sunburst(
    df,
    path=['generation','type 1'],
    title=f'pokemon type distribution'
)
st.plotly_chart(fig4)
# to run this program, open terminal and run the following command
# streamlit run app.py
