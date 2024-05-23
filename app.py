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



if selected=="Project Proposal":
    st.title(f"{selected}")
    st.write("National Rail, a company that provides business services to passenger train operators in England, Scotland, and Wales asked us to create an exploratory dashboard that helps them:")
    st.markdown("- Identify the most popular routes")
    st.markdown("- Determine peak travel times")
    st.markdown("- Analyze revenue from different ticket types & classes.")
    st.markdown("- Diagnose on-time performance and contributing factors.")
    st.markdown('<div style="background-color: #EDEDED; font-weight: bold;">Please click above options to explore further</div>', unsafe_allow_html=True)
    st.write("dataset link: https://mavenanalytics.io/challenges/maven-rail-challenge/32")
    st.write("(Source: Carlos Pacheco, via Tableau Public), (License: Public Domain)")
    
if selected=="Popular Routes":  
    st.title(f"The Top 10 popular routes")
    st.markdown('<div style="background-color: #EDEDED; font-weight: bold;">1. Birmingham New Street is top Arrival Station</div>', unsafe_allow_html=True)
    st.markdown('<div style="background-color: #EDEDED; font-weight: bold;">2. Manchester Piccadilly is the top Departure station</div>', unsafe_allow_html=True)
    st.markdown('<div style="background-color: #EDEDED; font-weight: bold;">3. Liverpool Lime Street to Manchester Piccadilly is the top Route </div>', unsafe_allow_html=True)
    
    fig = px.bar(data_frame = outputs['Routes'].head(10), x='Route', y='Route_Mapping', title="Most Popular Routes - Top 10",  labels={'Route_Mapping':'Passenger Count'})
    st.plotly_chart(fig, use_container_width=True)

if selected=="Peak Travel Times":  
    st.title(f"Peak Travel Times")
    st.markdown('<div style="background-color: #EDEDED; font-weight: bold;">1. Travellers Prefer to travel in the morning the most and Early morning as the least</div>', unsafe_allow_html=True)
    st.markdown('<div style="background-color: #EDEDED; font-weight: bold;">2. In March & January months more people are travelling</div>', unsafe_allow_html=True)
    st.markdown('<div style="background-color: #EDEDED; font-weight: bold;">3. Evening 6 & Morning 6 are the busiest travelling hours </div>', unsafe_allow_html=True)
    
    
    fig = px.bar(data_frame = outputs['peak travel times'].reset_index(), x = 'index', y= 'Travel_Time_Segment',title="Peak travel times",  labels={'index':'Passenger Count', 'Travel_Time_Segment': 'Passenger Count'})
    st.plotly_chart(fig, use_container_width=True)
    
    color_list = ['royalblue', 'dodgerblue', 'darkblue', 'lightskyblue']
    fig = px.bar(data_frame = outputs['Peak Travel Hours'].sort_index().reset_index(), y= 'index', x = 'Departure_Time', \
             title="Travelling Hours",  labels={'index':'Hour', 'Departure_Time': 'Passenger Count'}, \
             orientation='h',color = 'Travel_Time_Segments', template='plotly', color_discrete_sequence=color_list)
    fig.update_layout(yaxis={'dtick': 1})
    st.plotly_chart(fig, use_container_width=True)

if selected=="Revenue by Ticket Class & Type":  
    st.title(f"Revenue From Different TicketTypes & Classes")
    
    fig1 = px.pie(outputs['revenue_by_class'], values='sum', names='Ticket_Class', title='Revenue By Class', labels={'sum': 'Passenger Count'})

    fig2 = px.pie(outputs['revenue_by_type'], values='sum', names='Ticket_Type', title='Revenue By Type', labels={'sum': 'Passenger Count'})
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.plotly_chart(fig2, use_container_width=True)

    color_list = ['royalblue', 'dodgerblue', 'darkblue']
    fig = px.bar(outputs['revenue_by_class_and_type'], x="Ticket_Class", y="sum", color="Ticket_Type"\
            ,title="Revenue by Class & Type", labels = {'sum':'Revenue'}, template='plotly', color_discrete_sequence=color_list)
    st.plotly_chart(fig,use_container_width=True)
    
    st.markdown('<div style="background-color: #EDEDED">1. Revenue for Standard class is high compared to First Class, and as well as the number of passenger who bought the ticket & around 50% of the passengers in both Ticket Classes are Railcard holders. So it wont be a factor for low prices in First Class transactions</div>', unsafe_allow_html=True)
    st.markdown('<div style="background-color: #EDEDED">2. The revenue for Advance & Off Peak booking is high compared to Anytime - This is interesting because Both have discounts/offer for the price but not for Anytime category. The reason for high revenue could be the no of passenger count in each Ticket Type. Also There are `66%` of the passangers are having Railcard from Anytime category so this could be one of the factors for low revenue from Anytime category </div>', unsafe_allow_html=True)
    st.markdown('<div style="background-color: #EDEDED">3. The Standard Class with Advance Type Bookings are high compared to other</div>', unsafe_allow_html=True)

    
if selected=="On-time performance":  
    st.title(f"Diagnose On-Time Performance And Contributing Factors")

    st.markdown('<div style="background-color: #EDEDED;font-weight: bold">1. Most of the trains are On-Time with 90.67 percent only 5.34 percent are delayed and rest of the percentage are from cancelled trains</div>', unsafe_allow_html=True)
    st.markdown('<div style="background-color: #EDEDED;font-weight: bold">2. Contributing factors: Techinical Issue and Signal Failures are the top reasons for delay of the trains </div>', unsafe_allow_html=True)
    st.markdown('<div style="background-color: #EDEDED;font-weight: bold">3. Liverpool Lime Street to Manchester Piccadilly and London Euston to Liverpool Lime Street routes are havings highest train delays delays</div>', unsafe_allow_html=True)

    
    fig1 = px.pie(outputs['On-Time Performance'].reset_index(), values='Journey_Status', names='index', title='On-Time Performance',\
                                            labels = {'index':'Journey Status', 'Journey_Status':'Count(in %)'})

    fig2 = px.bar(data_frame = outputs['Reason_for_Delay'][1:].reset_index(), x = 'index', y= 'Reason_for_Delay',\
             title="Reason for Delay",  labels={'index':'Reason_for_Delay', 'Reason_for_Delay': 'Count'})
    

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.plotly_chart(fig2, use_container_width=True)


    fig3 = px.bar(data_frame = outputs['routemap-delay'].head(10), x = 'Route_Mapping', y= 'Count',\
                        title="Top 10 Routes with highest delays")
    st.plotly_chart(fig3, use_container_width=True)

    fig4 = px.imshow(outputs['routemap-delay_crosstab'], aspect="auto", color_continuous_scale="Blues_r", title = 'Routemaps with Reason for delays')
    st.plotly_chart(fig4, use_container_width=True)
    



    
    