import pickle
import plotly.express as px
import plotly.io as pio
import streamlit as st
from streamlit_option_menu import option_menu

outputs = pickle.load(open('outputs.pkl', 'rb'))

#Menu creation
selected = option_menu(None, ["Project Proposal", "Popular Routes", "Peak Travel Times", "Revenue by Ticket Class & Type","On-time performance"], 
    icons=['person-workspace', 'train-front', 'clock', 'bar-chart-line', 'hourglass-split'], 
    menu_icon="cast", default_index=0, orientation="horizontal")


# Defining the custom template
custom_template = {
    'layout': {
        'plot_bgcolor': '#EDEDED',
        'paper_bgcolor': '#EDEDED',
        'colorway': ['#203864'],
        'xaxis': 
        {
            'tickangle': 45,          
            'automargin': True 
        },
        'yaxis':
        {
            'automargin':True
        }
    
}}

pio.templates['custom_template'] = custom_template
pio.templates.default = 'custom_template'
st.title(f"Dashboard")

fig1 = px.bar(data_frame = outputs['Routes'].head(10), x='Route', y='Route_Mapping', title="Most Popular Routes - Top 10",  labels={'Route_Mapping':'Passenger Count'})
fig2 = px.bar(data_frame = outputs['peak travel times'].reset_index(), x = 'index', y= 'Travel_Time_Segment',title="Peak travel times",  labels={'index':'Passenger Count', 'Travel_Time_Segment': 'Passenger Count'})
color_list = ['royalblue', 'dodgerblue', 'darkblue', 'lightskyblue']
fig3 = px.bar(data_frame = outputs['Peak Travel Hours'].sort_index().reset_index(), y= 'index', x = 'Departure_Time', \
            title="Travelling Hours",  labels={'index':'Hour', 'Departure_Time': 'Passenger Count'}, \
            orientation='h',color = 'Travel_Time_Segments', template='plotly', color_discrete_sequence=color_list)
fig3.update_layout(yaxis={'dtick': 1})

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig1, use_container_width=False)

with col2:
    st.plotly_chart(fig2, use_container_width=False)







    
    