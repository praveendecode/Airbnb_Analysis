from  streamlit import *
from streamlit_extras import *
from streamlit_lottie import *
from streamlit_option_menu import *
import pandas as pd 
from streamlit_extras.colored_header import colored_header
from streamlit_extras.metric_cards import style_metric_cards
import plotly.express as px
from streamlit_extras.keyboard_url import keyboard_to_url
from streamlit_lottie import st_lottie
import json as js
import pymongo as pm



class airbnb:

    def dashboard(self):
                            
        st.set_page_config(page_title='airBnB Project By Praveen', layout="wide")

        
                                                                                         # PROGRAMS INITIATED
        with st.sidebar:     # Navbar
                        selected = option_menu(
                                                   menu_title="airbnb",
                                                   options=['Intro','Descriptive Statistics',"Insights","Tableau dashboard",'Feedback'],
                                                   icons = ['mic-fill','cash-stack','phone-flip','geo-alt-fill','clock-fill','globe-central-south-asia','envelope-paper-heart-fill'],
                                                   menu_icon='alexa',
                                                   default_index=0,
                                               )
                        
                            #  Pandas 
                        df = pd.read_csv("Airbnbfinal_data.csv")
                        df['id'] = df['id'].apply(lambda x : str(x))
                        df['host_iD'] = df['host_iD'].apply(lambda x : str(x))
                        continous_features = df.select_dtypes(include=['int64','float64']).columns
                        cat_deatures = df.select_dtypes(include=['object']).columns
        
        def lottie(filepath):
                        with open(filepath, 'r') as file:
                            return js.load(file)

                        
        if selected =='Descriptive Statistics':
                
                
                st.markdown("<style>div.block-container{padding-top:3rem;}</style>", unsafe_allow_html=True)

                                
                explore = option_menu(
                            menu_title="",
                            options=['Click', 'Features','Summary'],
                            icons=['arrow-right-circle-fill', 'eye-fill'],
                            menu_icon='',
                            default_index=0,
                            orientation='horizontal')
                
                
                
               
 
                
                if explore == 'Features':
                        

                        col1,col2,col3 = st.columns([12.5,10,10])

                        col2.write("")
                        col2.write("")
                        col2.write("")

                        col2.markdown( "<h1 style='font-size: 90px;'><span style='color: cyan;'>Load</span> <span style='color: white;'</span> <span style='color: white;'>Dataset</span></h1>",unsafe_allow_html=True)


                      
                        col2.write("")
                        col1,col2,col3 = st.columns([10,10,9])

                        col2.write("")
                        uploaded_file = col2.file_uploader("   ", type=["csv", "txt", "jpg", "png", "pdf"])

                        if uploaded_file is not None:
                                # Save the uploaded file
                                with open('uploaded_data.csv', "wb") as f:
                                    f.write(uploaded_file.read())
                                df_100 = pd.read_csv('uploaded_data.csv')

                        
                        col2.write("")
                        col2.write("")
                        col2.write("")
                        # col2.write("")
                        # col2.write("")
                        col1,col2,col3 = st.columns([12,10,10])
                        col2.write("")
                        col2.write("")
                        col2.write("")
                        col2.write("")

                        col2.markdown( "<h1 style='font-size: 70px;'><span style='color: cyan;'>Know </span> <span style='color: white;'>The</span> <span style='color: cyan;'>Features</span></h1>",unsafe_allow_html=True)



                        
                        col2.write("")
                        col2.write("")
                        col1,col2,col3 = st.columns([18,10,10])

                        # Continous and categorical values
                        df['id'] = df['id'].apply(lambda x : str(x))
                        df['host_iD'] = df['host_iD'].apply(lambda x : str(x))
                        continous_features = df.select_dtypes(include=['int64','float64']).columns
                        cat_deatures = df.select_dtypes(include=['object']).columns 
                
                        if col2.button('Know features'):
                                 
                            col1,col2,col3,col4 = st.columns([2,10,10,2])

                            col2.write("")
                            col2.write("")
                            col2.write("")
                            
                            with col2 :
                                st.markdown( f"<h1 style='font-size: 50px;'><span style='color: cyan;'>Continous</span><span style='color: White;'> Features</span> </h1>",unsafe_allow_html=True)
                                colored_header(
                                label="",
                                description="",
                                color_name="blue-green-70", )

                                   
                                for i in continous_features:
                                        st.markdown( f"<h1 style='font-size: 25px;'><span style='color: white;'> {i} </span> </h1>",unsafe_allow_html=True)
                            col3.write("")
                            col3.write("")
                            col3.write("")
                            with col3 :
                                st.markdown( f"<h1 style='font-size: 50px;'><span style='color: cyan;'>Categorical </span><span style='color: White;'> Features</span> </h1>",unsafe_allow_html=True)
                                colored_header(
                                label="",
                                description="",
                                color_name="blue-green-70", )

                                   
                                for i in cat_deatures:
                                        st.markdown( f"<h1 style='font-size: 25px;'><span style='color: white;'> {i} </span> </h1>",unsafe_allow_html=True)

                elif explore == "Summary":

                       
                    col1,col2,col3 = st.columns([7,10,5])
                    col2.write("")
                    col2.write("")
                    col2.write("")
                    col2.write("")
                    col2.write("")
                    col2.write("")
                    col2.markdown( f"<h1 style='font-size: 100px;'><span style='color: cyan;'> Summary </span><span style='color: white;'> Statistics </span> </h1>",unsafe_allow_html=True)
                    col2.write("")
                    col2.write("")
                    col2.write("")
                    col2.write("")
                    col2.write("")
                    col2.write("")
                    col1,col2,col3 = st.columns([9,10,5])
                    col2.markdown( f"<h1 style='font-size: 40px;'><span style='color: cyan;'> Select </span><span style='color: white;'> Feature Type </span> </h1>",unsafe_allow_html=True)

                    col1,col2,col3 = st.columns([9,10,5])
                    select = col2.selectbox('',['Continous Features','Categorical Features'])
                    # col2.write("")
                    # col2.write("")
                    col2.write("")
                    col2.write("")

                    if select == 'Continous Features':
                        col2.markdown( f"<h1 style='font-size: 60px;'><span style='color: cyan;'> Continous </span><span style='color: white;'> Features </span> </h1>",unsafe_allow_html=True)

                        col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Select </span><span style='color: white;'> Feature </span> </h1>",unsafe_allow_html=True)

                        option = col2.selectbox('',continous_features)
                        if col2.button('Show'):

                            x = df[option].describe()

                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Selected Feature : </span><span style='color: white;'> {option}</span> </h1>",unsafe_allow_html=True)
                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Count : </span><span style='color: white;'>{x[0]} </span> </h1>",unsafe_allow_html=True)
                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Mean : </span><span style='color: white;'> {x[1]} </span> </h1>",unsafe_allow_html=True)
                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Std :  </span><span style='color: white;'> {x[2]}</span> </h1>",unsafe_allow_html=True)
                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Min  : </span><span style='color: white;'>  {x[3]}</span> </h1>",unsafe_allow_html=True)
                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> 25 % : </span><span style='color: white;'> {x[4]}</span> </h1>",unsafe_allow_html=True)
                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> 50 % : </span><span style='color: white;'>  {x[5]}</span> </h1>",unsafe_allow_html=True)
                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> 75 % : </span><span style='color: white;'>  {x[6]}</span> </h1>",unsafe_allow_html=True)
                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Max  : </span><span style='color: white;'>  {x[7]}</span> </h1>",unsafe_allow_html=True)
                            col1,col2,col3 = st.columns([7,10,5])
                            col2.write("")
                            col2.write("")
                            col2.write("")
                            col2.write("")
                            col2.write("")
                            col2.write("")
                            col2.markdown( f"<h1 style='font-size: 100px;'><span style='color: cyan;'> Feature </span><span style='color: white;'>  Distribution </span> </h1>",unsafe_allow_html=True)
                            col2.write("")
                            col2.write("")
                            col2.write("")
                            col2.markdown( f"<h1 style='font-size: 40px;'><span style='color: cyan;'> {option} </span><span style='color: white;'> Feature  Distribution </span> </h1>",unsafe_allow_html=True)

                            
                            fig = px.histogram(df[f'{option}'], nbins=20)
                            fig.update_layout(
                                plot_bgcolor='#0E1117',
                                paper_bgcolor='#0E1117',
                                xaxis_title_font=dict(color='#0DF0D4'),
                                yaxis_title_font=dict(color='#0DF0D4')
                            )
                            fig.update_traces(hoverlabel=dict(bgcolor="#0E1117"),
                                                hoverlabel_font_color="#0DF0D4")
                            fig.update_xaxes(title_text="Availability Types")

                            fig.update_yaxes(title_text="Days  Count")

                            fig.update_traces(marker_color='#1BD4BD')
                            
                            st.plotly_chart(fig, theme=None, use_container_width=True)
                



                    elif select == 'Categorical Features':
                        col2.markdown( f"<h1 style='font-size: 60px;'><span style='color: cyan;'> Categorical  </span><span style='color: white;'> Features </span> </h1>",unsafe_allow_html=True)

                        col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Select </span><span style='color: white;'> Feature </span> </h1>",unsafe_allow_html=True)

                        option = col2.selectbox('',cat_deatures)

                        if col2.button('Show'):

                            x = df[option].describe()

                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Selected Feature : </span><span style='color: white;'> {option}</span> </h1>",unsafe_allow_html=True)
                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Count : </span><span style='color: white;'>{x[0]} </span> </h1>",unsafe_allow_html=True)
                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Unique : </span><span style='color: white;'> {x[1]} </span> </h1>",unsafe_allow_html=True)
                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Top :  </span><span style='color: white;'> {x[2]}</span> </h1>",unsafe_allow_html=True)
                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Feq  : </span><span style='color: white;'>  {x[3]}</span> </h1>",unsafe_allow_html=True)
                
                    
                elif explore == 'Click':

                    col1,col2,col3 = st.columns([5,10,5])
                    col2.write("")
                    col2.write("")
                    def lottie(filepath):
                        with open(filepath, 'r') as file:
                            return js.load(file)

                    col1, col2, col3 = st.columns([1, 10, 1])
                    with col2:
                        file = lottie("stats2.json")
                        st_lottie(
                            file,
                            speed=1,
                            reverse=False,
                            loop=True,
                            quality='low',
                            height=1000,
                            width=1700,
                            key=None
                        )
        


        elif selected == 'Insights':
                st.markdown("<style>div.block-container{padding-top:3rem;}</style>", unsafe_allow_html=True)

                # Metrics 

                col1,col2,col3,col4,col5 = st.columns([10,10,10,10,10])

                col1.metric(label="Total Host Count", value=f'{len(df.host_name.unique())}',delta=int(len(df.host_name.unique())/100))
                col2.metric(label="Total Room Types", value=f'{len(df.room_type.unique())}',delta=int(len(df.room_type.unique())))
                col3.metric(label="Total Listings Available", value=f'{len(df.name.unique())}',delta=int(len(df.name.unique())/10))
                col4.metric(label="Total Amount Earned", value=f'{df.price.sum()}',delta=int(df.price.sum()/100))
                col5.metric(label="Total Host Neighbourhood", value=f'{len(df.host_neighbourhood.unique())}',delta=int(len(df.host_neighbourhood.unique())/10))

                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                # Filters :
                col1,col2,col3,col4 ,col5,col6,col7= st.columns([10,10,10,10,10,10,10])

                with col2.expander("FILTER"):

                    st.write("")
                    room_type = st.selectbox('CHOOSE ROOM TYPE',df.room_type.unique())

                with col4.expander("FILTER"):

                    st.write("")
                    place = st.selectbox('CHOOSE HOST NEIGHBOURHOOD',df.host_neighbourhood.unique())

                with col6.expander("FILTER"):

                    st.write("")
                    property_type = st.selectbox('CHOOSE Property Type',df.property_type.unique())

                
            

                # Availaibility
                col1,col2 = st.columns([10,10])
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.markdown( f"<h1 style='font-size: 70px;'><span style='color: cyan;'> Availability  </span><span style='color: white;'> Analysis </h1>",unsafe_allow_html=True)

                col1,col2,col3 = st.columns([10,20,5])
                col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Availability  days </span><span style='color: white;'>  based on</span> <span style='color: white;'> {room_type} and {property_type} and {place} </span></h1>",unsafe_allow_html=True)
                col1,col2 = st.columns([10,10])

                value = df.query(f"room_type=='{room_type}' and property_type == '{property_type}' and host_neighbourhood=='{place}'")[['availability_30', 'availability_60', 'availability_90', 'availability_365']].sum()
                name=['availability_30','availability_60','availability_90','availability_365']

                fig = px.bar( x=name, y=value)
                fig.update_layout(title_x=1)
                fig.update_layout(
                    plot_bgcolor='#0E1117',
                    paper_bgcolor='#0E1117',
                    xaxis_title_font=dict(color='#0DF0D4'),
                    yaxis_title_font=dict(color='#0DF0D4')
                )
                fig.update_traces(hoverlabel=dict(bgcolor="#0E1117"),
                                    hoverlabel_font_color="#0DF0D4")
                fig.update_xaxes(title_text="Availability Types")

                fig.update_yaxes(title_text="Days  Count")

                fig.update_traces(marker_color='#1BD4BD')
                
                st.plotly_chart(fig, theme=None, use_container_width=True)
                
               

                # Host Analysis

                col1,col2 = st.columns([10,10])
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
              
                col1.markdown( f"<h1 style='font-size: 70px;'><span style='color: cyan;'> Host  </span><span style='color: white;'> Analysis </h1>",unsafe_allow_html=True)
                 # Filters :
                col1,col2,col3= st.columns([10,10,10])
                
                
                
                # 1

                col1,col2,col3= st.columns([13,10,15])
                col2.write("")
                with col2.expander("FILTER"):

                    st.write("")
                    place = st.selectbox('HOST NEIGHBOURHOOD',df.host_neighbourhood.unique())
                col1,col2,col3 = st.columns([10,20,5])
                col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Top  10  Hosts </span><span style='color: white;'>  based on </span> <span style='color: white;'> Host Neighbourhood : {place} </span></h1>",unsafe_allow_html=True)
                
                col1,col2 = st.columns([10,10])

                filter = df.query(f"host_neighbourhood=='{place}'").groupby('host_name')['host_total_listings_count'].sum().nlargest(10)
                name = filter.index.tolist()
                value = filter.values.tolist()
                fig = px.bar( x=name, y=value)
                fig.update_layout(title_x=1)
                fig.update_layout(
                    plot_bgcolor='#0E1117',
                    paper_bgcolor='#0E1117',
                    xaxis_title_font=dict(color='#0DF0D4'),
                    yaxis_title_font=dict(color='#0DF0D4')
                )
                fig.update_traces(hoverlabel=dict(bgcolor="#0E1117"),
                                    hoverlabel_font_color="#0DF0D4")
                fig.update_xaxes(title_text="Host Name")

                fig.update_yaxes(title_text="Listings Count")

                fig.update_traces(marker_color='#1BD4BD')
                
                st.plotly_chart(fig, theme=None, use_container_width=True)
                col1.write("")
                col1.write("")
                col1.write("")
                 # 2
                col1,col2,col3= st.columns([13,10,15])
                with col2.expander("FILTER"):

                    st.write("")
                    room_type = st.selectbox('ROOM TYPE',df.room_type.unique())
                col1,col2,col3 = st.columns([10,20,5])
                col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Top  10  Hosts </span><span style='color: white;'>  based on </span> <span style='color: white;'> Room Type : {room_type} </span></h1>",unsafe_allow_html=True)
               
                col1,col2 = st.columns([10,10])

                filter = df.query(f"room_type=='{room_type}'").groupby('host_name')['host_total_listings_count'].sum().nlargest(10)
                name = filter.index.tolist()
                value = filter.values.tolist()
                fig = px.bar( x=name, y=value)
                fig.update_layout(title_x=1)
                fig.update_layout(
                    plot_bgcolor='#0E1117',
                    paper_bgcolor='#0E1117',
                    xaxis_title_font=dict(color='#0DF0D4'),
                    yaxis_title_font=dict(color='#0DF0D4')
                )
                fig.update_traces(hoverlabel=dict(bgcolor="#0E1117"),
                                    hoverlabel_font_color="#0DF0D4")
                fig.update_xaxes(title_text="Host Name")

                fig.update_yaxes(title_text="Listings Count")

                fig.update_traces(marker_color='#1BD4BD')
                
                st.plotly_chart(fig, theme=None, use_container_width=True)

                # Room_type Analysis
                col1,col2 = st.columns([10,10])
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.markdown( f"<h1 style='font-size: 70px;'><span style='color: cyan;'> Room Type  </span><span style='color: white;'> Analysis </h1>",unsafe_allow_html=True)
                col1.write("")
                col1.write("")
                col1,col2,col3= st.columns([13,10,15])
                with col2.expander("FILTER"):

                    st.write("")
                    room_type = st.selectbox('Room Type',df.room_type.unique())

                    option = st.selectbox('Choose Option',['Minimun','Maximum'])



                col1,col2,col3 = st.columns([7,20,5])

                if option == 'Minimun':

                    col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Top 10  </span><span style='color: white;'> minimun price host neighbourhoods based on Room Type :</span> <span style='color: cyan;'> {room_type}</span></h1>",unsafe_allow_html=True)
                    filter = df.query(f"room_type== '{room_type}'").groupby('host_neighbourhood')['price'].mean().nsmallest(10)

                    name = filter.index.tolist()

                    value = filter.values.tolist()
                    fig = px.bar( x=name, y=value)
                    fig.update_layout(title_x=1)
                    fig.update_layout(
                        plot_bgcolor='#0E1117',
                        paper_bgcolor='#0E1117',
                        xaxis_title_font=dict(color='#0DF0D4'),
                        yaxis_title_font=dict(color='#0DF0D4')
                    )
                    fig.update_traces(hoverlabel=dict(bgcolor="#0E1117"),
                                        hoverlabel_font_color="#0DF0D4")
                    fig.update_xaxes(title_text="Host Name")

                    fig.update_yaxes(title_text="Listings Count")

                    fig.update_traces(marker_color='#1BD4BD')
                    
                    st.plotly_chart(fig, theme=None, use_container_width=True)

                elif option == 'Maximum':

                    col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Top 10  </span><span style='color: white;'> Maximun price host neighbourhoods based on Room Type :</span> <span style='color: cyan;'> {room_type}</span></h1>",unsafe_allow_html=True)
                    filter = df.query(f"room_type== '{room_type}'").groupby('host_neighbourhood')['price'].mean().nlargest(10)

                    name = filter.index.tolist()

                    value = filter.values.tolist()
                    fig = px.bar( x=name, y=value)
                    fig.update_layout(title_x=1)
                    fig.update_layout(
                        plot_bgcolor='#0E1117',
                        paper_bgcolor='#0E1117',
                        xaxis_title_font=dict(color='#0DF0D4'),
                        yaxis_title_font=dict(color='#0DF0D4')
                    )
                    fig.update_traces(hoverlabel=dict(bgcolor="#0E1117"),
                                        hoverlabel_font_color="#0DF0D4")
                    fig.update_xaxes(title_text="Host Name")

                    fig.update_yaxes(title_text="Listings Count")

                    fig.update_traces(marker_color='#1BD4BD')
                    
                    st.plotly_chart(fig, theme=None, use_container_width=True)
                     
                col2.write("")
                col2.write("")
                col2.write("")
                col2.write("")
                col2.write("")
                col1,col2,col3= st.columns([13,10,15])
                with col2.expander("FILTER"):

                    st.write("")
                    room_type = st.selectbox('Choose Room Type',df.room_type.unique())




                col1,col2,col3 = st.columns([7,20,5])
                col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Top 10  </span><span style='color: white;'> maximun review host neighbourhoods based on Room Type :</span> <span style='color: cyan;'> {room_type}</span></h1>",unsafe_allow_html=True)
                filter = df.query(f"room_type== '{room_type}'").groupby('host_neighbourhood')['number_of_Reviews'].sum().nlargest(10)

                name = filter.index.tolist()

                value = filter.values.tolist()
                fig = px.bar( x=name, y=value)
                fig.update_layout(title_x=1)
                fig.update_layout(
                    plot_bgcolor='#0E1117',
                    paper_bgcolor='#0E1117',
                    xaxis_title_font=dict(color='#0DF0D4'),
                    yaxis_title_font=dict(color='#0DF0D4')
                )
                fig.update_traces(hoverlabel=dict(bgcolor="#0E1117"),
                                    hoverlabel_font_color="#0DF0D4")
                fig.update_xaxes(title_text="Host Name")

                fig.update_yaxes(title_text="Review Count")

                fig.update_traces(marker_color='#1BD4BD')
                
                st.plotly_chart(fig, theme=None, use_container_width=True)

                # Price  Analysis
                col1,col2 = st.columns([10,10])
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.markdown( f"<h1 style='font-size: 70px;'><span style='color: cyan;'> Price  </span><span style='color: white;'> Analysis </h1>",unsafe_allow_html=True)
                col1.write("")
                col1.write("")

                df_1 = df.copy()
                df_1.columns = ['id', 'name', 'description', 'Property Type', 'Room Type',
                            'minimum_nights', 'maximum_nights', 'number_of_Reviews', 'amenities',
                            'price', 'host_iD', 'Host', 'Host Neighbourhood',
                            'host_total_listings_count', 'longitide', 'latitude', 'availability_30',
                            'availability_60', 'availability_90', 'availability_365', 'rating'] 
                col1,col2,col3,col4,col5 = st.columns([10,10,10,10,10])
                with col2.expander("FILTER"):

                    st.write("")
                    choose_10 = st.selectbox('CHOOSE OPTION',['Top 10', "Bottom 10"])

                with col4.expander("FILTER"):

                    st.write("")
                    field = st.selectbox('CHOOSE FIELD',['Host',"Host Neighbourhood","Property Type","Room Type"])

                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1,col2,col3 = st.columns([15,20,5])
                col2.markdown( f"<h1 style='font-size: 35px;'><span style='color: cyan;'> {choose_10} </span><span style='color: white;'> {field}  based on </span> <span style='color: cyan;'> Price </span></h1>",unsafe_allow_html=True)
                
                if choose_10 == 'Top 10':
                    host_filter = df_1.groupby(f'{field}')['price'].sum().nlargest(10)

                    name = host_filter.index.tolist()

                    value = host_filter.values.tolist()
                    fig = px.bar( x=name, y=value)
                    fig.update_layout(title_x=1)
                    fig.update_layout(
                        plot_bgcolor='#0E1117',
                        paper_bgcolor='#0E1117',
                        xaxis_title_font=dict(color='#0DF0D4'),
                        yaxis_title_font=dict(color='#0DF0D4')
                    )
                    fig.update_traces(hoverlabel=dict(bgcolor="#0E1117"),
                                        hoverlabel_font_color="#0DF0D4")
                    fig.update_xaxes(title_text="Host Name")

                    fig.update_yaxes(title_text="Review Count")

                    fig.update_traces(marker_color='#1BD4BD')
                    
                    st.plotly_chart(fig, theme=None, use_container_width=True)

                elif choose_10 == "Bottom 10":
                    host_filter = df_1.groupby(f'{field}')['price'].sum().nsmallest(10)

                    name = host_filter.index.tolist()

                    value = host_filter.values.tolist()
                    fig = px.bar( x=name, y=value)
                    fig.update_layout(title_x=1)
                    fig.update_layout(
                        plot_bgcolor='#0E1117',
                        paper_bgcolor='#0E1117',
                        xaxis_title_font=dict(color='#0DF0D4'),
                        yaxis_title_font=dict(color='#0DF0D4')
                    )
                    fig.update_traces(hoverlabel=dict(bgcolor="#0E1117"),
                                        hoverlabel_font_color="#0DF0D4")
                    fig.update_xaxes(title_text="Host Name")

                    fig.update_yaxes(title_text="Review Count")

                    fig.update_traces(marker_color='#1BD4BD')
                    
                    st.plotly_chart(fig, theme=None, use_container_width=True)


                style_metric_cards(
                                    border_left_color='#08EED2',
                                    background_color='#0E1117', border_color="#0E1117")
                    
                colored_header(
                                label="",
                                description="",
                                color_name="blue-green-70", )
        
        elif selected == 'Tableau dashboard':
                st.markdown("<style>div.block-container{padding-top:0rem;}</style>", unsafe_allow_html=True)

                col1,col2,col3 = st.columns([5,10,5])
                col2.write("")
                col2.write("")
                def lottie(filepath):
                    with open(filepath, 'r') as file:
                        return js.load(file)

                col1, col2, col3 = st.columns([1, 10, 1])
                with col2:
                    file = lottie("d1.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        height=900,
                        width=1700,
                        key=None
                    )
                col1,col2,col3 = st.columns([7,10,5])
                col2.markdown( "<h1 style='font-size: 40px;'><span style='color: white;'>Press </span> <span style='color: cyan;'>'P'</span> <span style='color: white;'>To See Tableau Dashboard</span></h1>",unsafe_allow_html=True)
                keyboard_to_url(key="P", url="https://public.tableau.com/shared/8N6QHKD7D?:display_count=n&:origin=viz_share_link")
       
        elif selected == 'Intro':
            st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)



            # Start Intro
            col1, col2 = st.columns([11, 7])
        
            with col1:
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")

                st.markdown(
                    "<h1 style='font-size: 79px;'><span style='color:white;'>Howdy ,</span> <span style='color: white;'>I'm </span><span style='color: cyan;'> Praveen</span> </h1>",
                    unsafe_allow_html=True)


            with col2:
                file = lottie("intro1.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=700,
                    key=None
                )

            st.write("")
            st.write('')
            st.write("")
            st.write('')
            st.write("")
            st.write("")
            st.write('')
            st.write("")
            with col1:
                file = lottie("sound.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=240,
                    width=600,
                    key=None
                )

            col1,col2,col3 = st.columns([3.4,10,2])
            with col2:
                st.markdown(
                    "<h1 style='font-size: 100px;'><span style='color:white;'>Data</span> <span style='color: cyan;'> Scientist </span> <span style='color:white;'></span> <span style='color: white ;'> From </span> <span style='color: cyan;'> India </span></h1>",
                    unsafe_allow_html=True)
                
            col1,col2,col3 = st.columns([8,10,2])
            col2.markdown(
                    "<h1 style='font-size: 27px;'>  <span style='color: cyan;'>To Know About Me  </span> <span style='color: cyan;'>Press 'P'  </span></h1>",
                    unsafe_allow_html=True)
            keyboard_to_url(key="P", url="https://www.linkedin.com/in/praveen-n-2b4004223/")


            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col1,col2,col3 = st.columns([10,10,2])
            with col1:
                st.markdown(
                    "<h1 style='font-size: 100px;'><span style='color:white;'>About </span><span style='color:Cyan;'> airbnb Project </span> </h1>",
                    unsafe_allow_html=True)
            col1,col2,col3 = st.columns([2,10,2])
            with col2:
                file = lottie("bike.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=900,
                    width=1300,
                    key=None
                )
                
       
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col1,col2,col3 = st.columns([19,10,1])
            col2.write("")
            col2.write("")
            col2.write("")
            with col1:
                st.markdown(
                    "<h1 style='font-size: 90px;'><span style='color:cyan;'> Data  </span><span style='color:white;'> Collection </span><span style='color:cyan;'> </span> </h1>",
                    unsafe_allow_html=True)
            col1,col2,col3 = st.columns([5,10,2])
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            with col2:
                file = lottie("Mongo.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=800,
                    width=900,
                    key=None
                )
            col2.write("")
            col2.write("")
            col2.write("")
            col1,col2,col3 = st.columns([19,10,1])
            col2.write("")
            col2.write("")
            col2.write("")
            with col1:
                st.markdown(
                    "<h1 style='font-size: 90px;'><span style='color:cyan;'> Data </span><span style='color:white;'> Preprocessing </span><span style='color:cyan;'>  </span> </h1>",
                    unsafe_allow_html=True)
            col1,col2,col3 = st.columns([5,10,2])
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            with col2:
                file = lottie("cyan_boy_lap2.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=700,
                    width=1000,
                    key=None
                )
            col2.write("")
            col2.write("")
            col2.write("")
            col1,col2,col3 = st.columns([19,10,1])
            col2.write("")
            col2.write("")
            col2.write("")
            with col1:
                st.markdown(
                    "<h1 style='font-size: 90px;'><span style='color:cyan;'> Exploratory </span><span style='color:white;'> Data  </span><span style='color:cyan;'> Analysis </span> </h1>",
                    unsafe_allow_html=True)
            col1,col2,col3 = st.columns([5,10,2])
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            with col2:
                file = lottie("data_exploaration.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=900,
                    width=1000,
                    key=None
                )



            col2.write("")
            col2.write("")
            col2.write("")
            col1,col2,col3 = st.columns([19,10,1])
            with col1:
                st.markdown(
                    "<h1 style='font-size: 100px;'><span style='color:cyan;'> Dashboard </span><span style='color:white;'>  </span><span style='color:white;'> Process </span> </h1>",
                    unsafe_allow_html=True)
            col1,col2,col3 = st.columns([5,10,2])
           
            with col2:
                file = lottie("d3.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=900,
                    width=1100,
                    key=None
                )
            colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70"
                )
        
        elif selected == "Feedback":
            praveen_1 = pm.MongoClient(
                'mongodb://praveen:praveenroot@ac-cd7ptzz-shard-00-00.lsdge0t.mongodb.net:27017,ac-cd7ptzz-shard-00-01.lsdge0t.mongodb.net:27017,ac-cd7ptzz-shard-00-02.lsdge0t.mongodb.net:27017/?ssl=true&replicaSet=atlas-ac7cyd-shard-0&authSource=admin&retryWrites=true&w=majority')
            db = praveen_1['Feedback_airbnb']
            collection = db['comment']

            st.markdown("<style>div.block-container{padding-top:2rem;}</style>", unsafe_allow_html=True)

            col1, col2, col3, = st.columns([3, 8, 3])

            with col2:
                selected_1 = option_menu(
                    menu_title="OPINION BOX",
                    options=['CHOOSE OPTION', 'Your Feedback', "Explore User Thoughts"],
                    icons=['arrow-down-circle-fill', 'envelope-plus-fill', 'people-fill'],
                    default_index=0)
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")

            if selected_1 == 'CHOOSE OPTION':
                # animation

                def lottie(filepath):
                    with open(filepath, 'r') as file:
                        return js.load(file)

                col1, col2, col3, col4 = st.columns([15, 15, 15, 15])
                with col2:
                    file = lottie("angry_emoji.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=300,
                        width=300,
                        key=None
                    )
                with col1:
                    file = lottie("smile_emoji.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=300,
                        width=300,
                        key=None
                    )
                with col3:
                    file = lottie("calm_emoji.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=300,
                        width=300,
                        key=None
                    )
                with col4:
                    file = lottie("love_emoji.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=300,
                        width=300,
                        key=None
                    )


            elif selected_1 == 'Your Feedback':

                def lottie(filepath):
                    with open(filepath, 'r') as file:
                        return js.load(file)

                col1, col2, col3 = st.columns([10, 30, 5])
                col2.markdown(
                    "<h1 style='font-size: 90px;'><span style='color:white;'>Your</span> <span style='color:cyan;'>Feedback</span> <span style='color: white;'>Here </span> </h1>",
                    unsafe_allow_html=True)
                # animation

                st.write("")

                st.write("")

                st.write("")
                col1, col2, col3 = st.columns([15, 30, 5])
                with col2:
                    file = lottie("star_before_fb.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=500,
                        width=600,
                        key=None
                    )

                col1, col2, col3, = st.columns([3, 8, 3])

                with col2:
                    col2.markdown(
                        "<h1 style='font-size: 30px;'><span style='color:white;'>Enter</span> <span style='color:cyan;'>Comment</span> <span style='color: white;'>Here ⬇️</span> </h1>",
                        unsafe_allow_html=True)
                    Comment = st.text_input('   ')
                    st.write(Comment)
                    if st.button('Save Comment'):
                        collection.insert_one({'comment of user': Comment})
                        st.write("")
                        st.write("")
                        col1, col2, col3, = st.columns([5, 8, 5])
                        st.success('Your Valuable Comment Saved Thankyou!', icon="✅")
                        col1, col2, col3 = st.columns([10, 30, 10])
                        with col2:
                            file = lottie("star.json")
                            st_lottie(
                                file,
                                speed=1,
                                reverse=False,
                                loop=True,
                                quality='low',
                                # renderer='svg',
                                height=100,
                                width=500,
                                key=None
                            )

                col1, col2, col3, = st.columns([3, 8, 3])
                with col2:
                    colored_header(
                        label="",
                        description="",
                        color_name="blue-green-70", )


            elif selected_1 == 'Explore User Thoughts':

                def lottie(filepath):
                    with open(filepath, 'r') as file:
                        return js.load(file)

                col1, col2, col3 = st.columns([10, 30, 5])

                with col2:

                    file = lottie("down_arrow.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=300,
                        width=800,
                        key=None
                    )
                col2.markdown(
                    "<h1 style='font-size: 70px;'><span style='color:white;'>Explore</span> <span style='color:cyan;'>User Thoughts </span> <span style='color: white;'>Here </span> </h1>",
                    unsafe_allow_html=True)
                col2.write("")
                col2.write("")

                with col2:

                    file = lottie("thoughts.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=500,
                        width=800,
                        key=None
                    )
                st.write("")
                st.write("")
                st.write("")
                col1, col2, col3, = st.columns([3.6, 10, 3])
                with col2:
                    # if st.button("Click Me!"):
                    res = [i['comment of user'] for i in collection.find()]
                    st.write("")
                    with st.spinner('Wait for it...'):
                        time.sleep(5)

                    colored_header(
                        label="Comments By Users ⬇",
                        description="",
                        color_name="blue-green-70", )
                    for i in res:
                        print(st.code(i))

                    col1, col2, col3 = st.columns([1, 10, 1])
                    col2.write("")
                    col2.write('')
                    col2.markdown(
                        "<h1 style='font-size: 35px;'><span style='color:cyan;'>Press</span> <span style='color:white;'>'G'</span> <span style='color:cyan;'>On Keyboard To Explore More Project</span> </h1>",
                        unsafe_allow_html=True)
                    with col2:
                        keyboard_to_url(key="G", url="https://github.com/praveendecode")

                    def lottie(filepath):
                        with open(filepath, 'r') as file:  # 'G' On Keyboard To Explore More Project
                            return js.load(file)

                    with col2:
                        file = lottie("click2.json")
                        st_lottie(
                            file,
                            speed=1,
                            reverse=False,
                            loop=True,
                            quality='low',
                            height=100,
                            width=700,
                            key=None
                        )

                    colored_header(
                        label="",
                        description="",
                        color_name="blue-green-70", )
# Object 

Object = airbnb()
Object.dashboard()
