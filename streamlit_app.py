
import streamlit as st
import pandas as pd
import plotly.express as px



st.set_page_config(page_title='Ivsa National Congress',
                   page_icon=':stethoscope:',
                   layout='wide',
                   initial_sidebar_state='expanded',
                   menu_items={"About": 'We are passionate Veterinarians who wishes to change the world'}
                   )

t1, t2 = st.columns((0.2,1)) 

t1.image('images/ivsanigeria.jpg', width = 180)
t2.title("Ivsa Nigeria National Congress (COAL CITY 2023) Handover Report")
t2.markdown(" **Tel:** 08147244592 **| Website:** https://ivsanigeria.wordpress.com | **Email:** ivsanigeria@gmail.com")

st.write('---')
ivsa = pd.read_excel('IVSA NIGERIA CONGRESS 2023 clean.xlsx')

s1, s2 = st.columns((2, 0.1))
with s1.container():
    ss1,ss2=st.columns((1,0.1))
    ss1.subheader('Brief Overview')
    ss1.markdown("A total of :blue[**153**] Delegates registered for the 2023 National congress at :rainbow[University of Nigeria, Nsukka.]  \nThe congress held from :orange[27th September - 1st October, 2023.] This report provides :green[valuable insights] from the data gotten during and after registration.  From :violet[metrics to graphical representations], this report highlights hidden interpretations from the data. ")
    st.write('---')
    as1,as2, as3, as4 = st.columns((0.5,0.5,0.5,0.5))   
    as1.metric(label='% Who Registered and Attended;', value='95%', delta="more")
    Accomodation = ivsa['roomshare'].value_counts(normalize='True').mul(100).round(1).astype(str) + '%'
    Accomodation_max = ivsa['roomshare'].value_counts(normalize='True').mul(100).round(1).max().astype(str) + '%'
    Accomodation_min = ivsa['roomshare'].value_counts(normalize='True').mul(100).round(1).min().astype(str) + '%'
    as2.metric(label='% Who Obliged To Share a Room;', value=Accomodation_max, delta= 'more')
    as3.metric(label='% Without Food Allergies;', value='79.1%', delta='more')
    Medication_min = ivsa['medication'].value_counts(normalize='True').multiply(100).round(2).min().astype(str) + '%'
    Medication_max = ivsa['medication'].value_counts(normalize='True').multiply(100).round(2).max().astype(str) + '%'
    as4.metric(label='% Without Medications;', value=Medication_max, delta='more')
    st.write('---')


col1, col2 = st.columns(2)
with col1:
    level = ivsa['Study_year']
    fig = px.bar(level, color= level, title='Delegates by Class;', color_continuous_scale='inferno', labels={'value': 'Count', 'Study_year': 'Class_level'})
    st.plotly_chart(fig)
with col2:
    school = ivsa['University '].value_counts().sort_values()
    fig = px.bar(school,  title='Delegates by School;', labels={'value': 'Count',})
    st.plotly_chart(fig)
    

ivsa['ivsa_products'] = ivsa['ivsa_products'].str.replace('pins', 'lapel')
ivsa['ivsa_products'] = ivsa['ivsa_products'].str.replace('notebook', 'jotters')
ivsa['ivsa_products'] = ivsa['ivsa_products'].str.replace('Cap', 'facecap')
 
word_to_search = ['Hoodies','jotters','planners','T-shirts','lapel','face cap','Mugs','Bucket Hat','Tote Bag']
word_count = {}
for word in word_to_search:
    word_count[word] = ivsa['ivsa_products'].str.count(word).sum()
for word, count in word_count.items():
   print(word, count)

sorted_words = dict(sorted(word_count.items(), key=lambda x: x[1], ))
plot = pd.DataFrame.from_dict(sorted_words, orient='index')


st.write('---')
g1,g2, g3 = st.columns((10.9,0.2,10.9))

with g1:
    fig = px.scatter(plot, color=sorted_words,title="Delegates' preferred merch of purchase", size=sorted_words, color_continuous_scale='inferno', labels={ 'index': 'Merch'}) 
    st.plotly_chart(fig)

with g3:
    st.write('')
    st.write('')
    st.write('')
    st.markdown('**Registered Delegates across the registration period (April - September)**')
    ivsa['Timestamp'] = pd.to_datetime(ivsa['Timestamp'])
    time = ivsa[['Study_year', 'Timestamp']].groupby(pd.Grouper(key='Timestamp', freq='M')).count()
    st.area_chart(time, color='#ffaa0088', x_label='Month', y_label='Count')
