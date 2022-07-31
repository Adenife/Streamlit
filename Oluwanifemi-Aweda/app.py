import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import base64
import os
import smtplib
import ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

st.set_page_config(page_title="My Portfolio", page_icon=":computer:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# use local css
def local_css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)


path = os.path.dirname(__file__)
# path_labels = path+'/style/style.css'
# local_css(path_labels)

my_image_path = path+'/style/profile-pics.png'


my_image = Image.open(my_image_path)
# edaApp = Image.open("images/edaApp.jpg")
# financeApp = Image.open("images/financeApp.jpg")
# flaskRepo = Image.open("images/flaskRepo.jpg")
edaApp = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_2b3k5idb.json")
financeApp = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_z6scuqaw.json")
flaskRepo = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_fvrs1qak.json")
googleCapstone = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_ht8zw3es.json")
tableauRepo = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_hx7ddrx9.json")
witcherAnalysis = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_1a8dx7zj.json")
covidAnalysis = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_vckswclv.json")
modeEngagement = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_SqEf0A.json")

linkedIn = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_iotglorw.json")
twitter = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_thh7qfpt.json")
github = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_dgBN4P.json")

lottie_dataAnalysis = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_iv4dsx3q.json")


# Header Section
with st.container():
    image, text = st.columns([1,2])

    with image:
        st.image(my_image, width=250)

    with text:
        st.subheader("Hi, I am Oluwanifemi :wave:")
        st.title("A Data Analyst from Nigeria!")
        st.write("""I am curious and passionate about data. I explore datasets to derive insights and drive decisions. 
        I have excellent understanding and proficiency of tools and platforms for effective data analysis, data mining, data visualization, and software engineering. 
        I am passionate about the sustainable development goals most especially the alleviation of poverty in Africa, Nigeria precisely(SDG 1).""")


# What I Do
with st.container():
    st.write("---")
    whatIDo, lottieImage = st.columns(2)

    with whatIDo:
        st.header("What I Do")
        st.write(
            """
                - API development💻.
                - Data mining, analytics, and visualization📊.
                - Data modeling and ETL development📉.
                - Machine learning (Regression, Classification, Time series, and Clustering)🤖.
                - Proficient in SQL, Python, Tableau, and Excel🐍. 
                - I serve as a mentor and tech trainer at Matadors Leadership Institute and D-Pedagogic Hub.
                
                **Check me out on [LinkedIn](https://www.linkedin.com/in/oluwanifemi-aweda-2b9206118/)**

                *My interests include: music, volleyball, home exercising, travelling, cooking, volunteering, mentoring, tech innovation, STEM education.*
            """
        )
    
    with lottieImage:
        st_lottie(lottie_dataAnalysis, key="analysis", height=350)


pdfPath = path+"/Oluwanifemi Aweda's Resume.pdf"
# Resume
with st.container():
    viewResume, downloadResume, otherColumn1, otherColumn2, otherColumn3, otherColumn4 = st.columns(6)
    with viewResume:
        with open(pdfPath, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="Download My Resume",  data=PDFbyte, file_name="Oluwanifemi Aweda's Resume.pdf", mime='application/octet-stream', help='Download Resume File')
                       
    with downloadResume:
        def show_pdf(file_path):
            with open(file_path,"rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

        if st.button('  View My Resume  ', key='1', help='Open PDF File Here'):            
                show_pdf(pdfPath)

    with otherColumn1:
        st.button('Close Resume View', key='2', help='Close the PDF View')

    with otherColumn2:
        st.empty()

    with otherColumn3:
        st.empty()

    with otherColumn4:
        st.empty()

# <a style="text-decoration: none; color: white" href="">
# Projects
with st.container():
    st.write("---")
    st.markdown('<div style="text-align: center;"><h2>Some Notable Projects...</h2></div>', unsafe_allow_html=True)
    sectionOne, sectionTwo = st.columns(2)

    with sectionOne:
        # st.image(tableauRepo, use_column_width=True)
        st_lottie(tableauRepo, key="tableau", height=300)
        st.markdown('<div style="text-align: center;"><a style="text-decoration: none; color: white" href="https://public.tableau.com/app/profile/aweda.oluwanifemi.adeola"><h3>Tableau Portfolio</h3></a></div>', unsafe_allow_html=True)
        st.info("""
            Tableau is one of the most powerful visualization tools ever, and my all time favourite. Checkout my Tableu public profile to see the visualizations I have built. From partaking in challenges, to creating visuals on interesting datasets, and course project work.
            Taka a look at my profile [here](https://public.tableau.com/app/profile/aweda.oluwanifemi.adeola).
        """)

    with sectionTwo:
        # st.image(edaApp, use_column_width=True)
        st_lottie(edaApp, key="eda", height=300)
        st.markdown('<div style="text-align: center;"><a style="text-decoration: none; color: white" href="https://adenife-streamlit-eda-applicationapp-lldgdx.streamlitapp.com/"><h3>EDA Application</h3></a></div>', unsafe_allow_html=True)
        st.info("""
            A simple Exploratory Data Analysis (EDA) tool in python using the *streamlit* library. The *streamlit* library helps to build applications with little code purely in python. Upload a dataset (.csv file) and watch the magic happen. Have fun!!!
            Try out my EDA application [here](https://adenife-streamlit-eda-applicationapp-lldgdx.streamlitapp.com/).
        """)


with st.container():
    sectionOne, sectionTwo = st.columns(2)

    with sectionOne:
        # st.image(witcherAnalysis, use_column_width=True)
        st_lottie(witcherAnalysis, key="witcher", height=300)
        st.markdown('<div style="text-align: center;"><a style="text-decoration: none; color: white" href="https://github.com/Adenife/Data-Analysis/blob/main/The%20witcher%20Analysis/witcherFinalAnalysisReport.ipynb"><h3>Witcher Analysis</h3></a></div>', unsafe_allow_html=True)
        st.info("""
            This project aimed to see the relationship between characters in the witcher book series. Selenium was used to scrape the data from the witcher wiki webpage, spacy was majorly used for the analysis and pyvis was used to visualize the results. See how each character relates to each other in this mind blowing end-to-end project.
            Taka a look [here](https://github.com/Adenife/Data-Analysis/blob/main/The%20witcher%20Analysis/witcherFinalAnalysisReport.ipynb).
        """)

    with sectionTwo:
        # st.image(financeApp, use_column_width=True)
        st_lottie(financeApp, key="finance", height=300)
        st.markdown('<div style="text-align: center;"><a style="text-decoration: none; color: white" href="https://adenife-streamlit-stockprice-applicationapp-p6xufg.streamlitapp.com/"><h3>Finance Tracker Application</h3></a></div>', unsafe_allow_html=True)
        st.info("""
            Are you a financial analyst? Do you find it stressful to get company financial data? Have all you need to start analysing company finances from this amazing finance tracker application. Built solely in *streamlit* and harnessing the power of yfinance, see important financial information from the S&P 500 company. 
            Taka a look [here](https://adenife-streamlit-stockprice-applicationapp-p6xufg.streamlitapp.com/).
        """)


with st.container():
    sectionOne, sectionTwo = st.columns(2)

    with sectionOne:
        # st.image(googleCapstone, use_column_width=True)
        st_lottie(googleCapstone, key="capstone", height=300)
        st.markdown('<div style="text-align: center;"><a style="text-decoration: none; color: white" href="https://github.com/Adenife/Data-Analysis/blob/main/Google%20Capstone%20Case%201/How%20Does%20a%20Bike-Share%20Navigate%20Speedy%20Success_.pdf"><h3>Bike Share Analysis</h3></a></div>', unsafe_allow_html=True)
        st.info("""
            This analysis was done to fulfill the requirements for getting the google data analytics certification hosted on coursera. The case study involves a bikeshare companys data of its customers trip details over a 12 month period (June 2021 - May 2022). The analysis follows the 6 phases of the Data Analysis process as a guideline which includes the; Ask, Prepare, Process, Analyze, and Act phases.
            Download my report [here](https://github.com/Adenife/Data-Analysis/blob/main/Google%20Capstone%20Case%201/How%20Does%20a%20Bike-Share%20Navigate%20Speedy%20Success_.pdf).
        """)

    with sectionTwo:
        # st.image(flaskRepo, use_column_width=True)
        st_lottie(flaskRepo, key="flask", height=300)
        st.markdown('<div style="text-align: center;"><a style="text-decoration: none; color: white" href="https://github.com/Adenife/Flask"><h3>Flask Code Repository</h3></a></div>', unsafe_allow_html=True)
        st.info("""
            Flask is one of the major python web frameworks. This means that flask provides you with tools, libraries and technologies that allows you to build a web application. Flask is often referred to as a micro framework, but can be scalable because of it's flexibility. Flask comes with some standard functionalities and allows developers to add any number of libraries or plugins for an extension.
            Checkout my flask repository [here](https://github.com/Adenife/Flask).
        """)


with st.container():
    sectionOne, sectionTwo = st.columns(2)

    with sectionOne:
        st_lottie(covidAnalysis, key="sql1", height=300)
        st.markdown('<div style="text-align: center;"><a style="text-decoration: none; color: white" href="https://github.com/Adenife/Data-Analysis/blob/main/SQL/covidAnalysis.sql"><h3>Covid-19 Analysis</h3></a></div>', unsafe_allow_html=True)
        st.info("""
            COVID-19 made the world go on lockdown, so why not analyze how it affected different countries and how these countries were able to contain it?. In this SQL analysis peoject I dived into the Covid dataset to find insight on it's impact in various parts of the world. Skills used include Joins, CTE's, Temp Tables, Windows Functions, Aggregate Functions, Creating Views, Converting Data Types. 
            Taka a look [here](https://github.com/Adenife/Data-Analysis/blob/main/SQL/covidAnalysis.sql).
        """)

    with sectionTwo:
        st_lottie(modeEngagement, key="sql2", height=300)
        st.markdown('<div style="text-align: center;"><a style="text-decoration: none; color: white" href="https://github.com/Adenife/Data-Analysis/blob/main/SQL/modeEngagementInvestigation.sql"><h3>User Engagement Analysis</h3></a></div>', unsafe_allow_html=True)
        st.info("""
            You show up to work Tuesday morning, September 2, 2014. The head of the Product team walks over to your desk and asks you what you think about the latest activity on the user engagement dashboards. You are responsible for determining what caused the dip at the end of the chart shown above and, if appropriate, recommending solutions for the problem. 
            Checkout this SQL customer engagement script [here](https://github.com/Adenife/Data-Analysis/blob/main/SQL/modeEngagementInvestigation.sql).
        """)


# Contact
# with st.container():
#     st.write("---")
#     st.markdown('<div style="text-align: center;"><h2>Get in Touch With Me!</h2></div>', unsafe_allow_html=True)
#     st.write("##")

#     # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
#     contact_form = """
#     <form style=" width: 50vw; margin-left : 25vw; action="https://formspree.io/f/mwkzeenv" method="POST">
#         <input type="email" name="email" placeholder="Your email" required>
#         <textarea name="message" placeholder="Your message here" required></textarea>
#         <button type="submit">Send</button>
#     </form>
#     """

#     # st.markdown(contact_form, unsafe_allow_html=True)
#     left_column, center_column, right_column = st.columns(3)
#     with left_column:
#         st.empty()
#     with center_column:
#         st.markdown(contact_form, unsafe_allow_html=True)
#     with right_column:
#         st.empty()


with st.container():
    left, main, right = st.columns(3)

    with left:
        st.empty()

    with main:
        with st.form(key="send_mail", clear_on_submit=True):
            st.write("---")
            st.markdown('<div style="text-align: center;"><h2>Get in Touch With Me!</h2></div>', unsafe_allow_html=True)
            sender_name = st.text_input(label='Your Name')
            sender_mail = st.text_input(label='Your Mail')
            email_body = st.text_area(label='Your Message Here...')

            # Define the transport variables
            ctx = ssl.create_default_context()
            password = "gcddbwbizvmvduku"    # Your app password goes here
            sender = "awedaoluwanifemi@gmail.com"    # Your e-mail address
            receiver = "awedaoluwanifemi@gmail.com" # Recipient's address

            # Create the message
            message = MIMEMultipart("alternative")
            message["Subject"] = sender_name + " -- " + sender_mail
            message["From"] = sender
            message["To"] = receiver

            # Plain text alternative version
            plain = email_body
            message.attach(MIMEText(plain, "plain"))      
                
            # Every form must have a submit button.
            submitted = st.form_submit_button("Submit")
            if submitted:
                # Connect with server and send the message
                with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx) as server:
                    server.login(sender, password)
                    server.sendmail(sender, receiver, message.as_string())

                st.success("Mail Successfully Sent!!!")


    with right:
        st.empty()