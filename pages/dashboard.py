import pickle
import plotly.express as px
import plotly.io as pio
import streamlit as st
from streamlit_option_menu import option_menu

outputs = pickle.load(open('outputs.pkl', 'rb'))

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
#fig2 = px.bar(data_frame = outputs['peak travel times'].reset_index(), x = 'index', y= 'Travel_Time_Segment',title="Peak travel times",  labels={'index':'Passenger Count', 'Travel_Time_Segment': 'Passenger Count'})
color_list = ['royalblue', 'dodgerblue', 'darkblue', 'lightskyblue']
fig2 = px.bar(data_frame = outputs['Peak Travel Hours'].sort_index().reset_index(), y= 'index', x = 'Departure_Time', \
            title="Travelling Hours",  labels={'index':'Hour', 'Departure_Time': 'Passenger Count'}, \
            orientation='h',color = 'Travel_Time_Segments', template='plotly', color_discrete_sequence=color_list)
fig2.update_layout(yaxis={'dtick': 1})



# Dashboard Main Panel
col1,col2 = st.columns(2, gap='small')
with col1:
    st.plotly_chart(fig1, use_container_width=True)

#with col2:
  #  st.plotly_chart(fig2, use_container_width=True)

with col2:
    st.plotly_chart(fig2, use_container_width=True)

fig3 = px.pie(outputs['revenue_by_class'], values='sum', names='Ticket_Class', title='Revenue By Class', labels={'sum': 'Passenger Count'})

fig4 = px.pie(outputs['revenue_by_type'], values='sum', names='Ticket_Type', title='Revenue By Type', labels={'sum': 'Passenger Count'})
color_list = ['royalblue', 'dodgerblue', 'darkblue']
fig5 = px.bar(outputs['revenue_by_class_and_type'], x="Ticket_Class", y="sum", color="Ticket_Type"\
        ,title="Revenue by Class & Type", labels = {'sum':'Revenue'}, template='plotly', color_discrete_sequence=color_list)
col1, col2,col3 = st.columns(3)
with col1:
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    st.plotly_chart(fig4, use_container_width=True)

with col3:
    st.plotly_chart(fig5, use_container_width=True)


fig6 = px.pie(outputs['On-Time Performance'].reset_index(), values='Journey_Status', names='index', title='On-Time Performance',\
                                        labels = {'index':'Journey Status', 'Journey_Status':'Count(in %)'})

fig7 = px.bar(data_frame = outputs['Reason_for_Delay'][1:].reset_index(), x = 'index', y= 'Reason_for_Delay',\
            title="Reason for Delay",  labels={'index':'Reason_for_Delay', 'Reason_for_Delay': 'Count'})

fig8 = px.imshow(outputs['routemap-delay_crosstab'], aspect="auto", color_continuous_scale="Blues_r", title = 'Routemaps with Reason for delays')

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig6, use_container_width=True)

with col2:
    st.plotly_chart(fig7, use_container_width=True)

st.plotly_chart(fig8, use_container_width=True)

    