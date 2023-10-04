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
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)


path = os.path.dirname(__file__)
# path_labels = path+'/style/style.css'
# local_css(path_labels)

my_image_path = path + "/style/profile-pics.png"


my_image = Image.open(my_image_path)
# edaApp = Image.open("images/edaApp.jpg")
# financeApp = Image.open("images/financeApp.jpg")
# flaskRepo = Image.open("images/flaskRepo.jpg")
edaApp = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_2b3k5idb.json")
financeApp = load_lottieurl(
    "https://assets8.lottiefiles.com/packages/lf20_z6scuqaw.json"
)
flaskRepo = load_lottieurl(
    "https://assets8.lottiefiles.com/packages/lf20_fvrs1qak.json"
)
googleCapstone = load_lottieurl(
    "https://assets4.lottiefiles.com/packages/lf20_ht8zw3es.json"
)
tableauRepo = load_lottieurl(
    "https://assets7.lottiefiles.com/packages/lf20_hx7ddrx9.json"
)
witcherAnalysis = load_lottieurl(
    "https://assets6.lottiefiles.com/packages/lf20_1a8dx7zj.json"
)
covidAnalysis = load_lottieurl(
    "https://assets4.lottiefiles.com/packages/lf20_vckswclv.json"
)
modeEngagement = load_lottieurl(
    "https://assets5.lottiefiles.com/packages/lf20_SqEf0A.json"
)
tableauTrading = load_lottieurl(
    "https://lottie.host/52e604b3-9eb7-4b7e-9510-d5504456fbd5/9Qik7QeQjf.json"
)
lottie_dataAnalysis = load_lottieurl(
    "https://assets4.lottiefiles.com/packages/lf20_iv4dsx3q.json"
)
twitterBot = load_lottieurl(
    "https://lottie.host/971e48ea-f06a-4896-a42c-dbfe9aad57ca/fVwOhnWw3i.json"
)
realEstate = load_lottieurl(
    "https://lottie.host/e595df0d-5ff9-4670-8855-4b46dbac5424/NhAPEre1y9.json"
)

# Header Section
with st.container():
    image, text = st.columns([1, 2])

    with image:
        st.image(my_image, width=250)

    with text:
        st.write("Hi, I am Oluwanifemi :wave:")
        st.subheader(
            "A multifaceted professional in the fields of data analysis, software engineering, and data engineering. "
        )
        st.write(
            """I thrive on navigating complex challenges and finding innovative solutions. With a solid foundation in computer science, I excel at understanding intricate technical concepts and translating them into actionable insights for business growth. My passion lies in unraveling the potential of data to drive informed decision-making and fuel organizational success."""
        )


# What I Do
with st.container():
    st.write("---")
    whatIDo, lottieImage = st.columns([2, 1])

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
                
                *In my career journey, I have had the privilege of wearing multiple hats, undertaking diverse roles that encompass data analysis, software engineering, and data engineering. This dynamic blend of responsibilities has enabled me to develop a comprehensive skill set and a unique perspective on how these interconnected disciplines can mutually reinforce and enhance one another.*
            """
        )

    with lottieImage:
        st_lottie(lottie_dataAnalysis, key="analysis", height=450)


pdfPath = path + "/Full Resume All.pdf"
daPath = path + "/Full Resume DA.pdf"
dePath = path + "/Full Resume DE.pdf"
sePath = path + "/Full Resume SE.pdf"
# Resume
# with st.container():
#     (
#         otherColumn3,
#         downloadResume,
#         linkedin,
#         github,
#         tableau,
#         otherColumn4,
#     ) = st.columns(6)
#     with downloadResume:
#         with open(pdfPath, "rb") as pdf_file:
#             PDFbyte = pdf_file.read()

#         st.download_button(
#             label="Download My Resume",
#             data=PDFbyte,
#             file_name="Oluwanifemi Aweda's Resume.pdf",
#             mime="application/octet-stream",
#             help="Download Resume File",
#         )

#     with linkedin:
#         st.write(
#             "**------------------ -----[LinkedIn](https://www.linkedin.com/in/oluwanifemi-aweda-2b9206118/)-----**"
#         )

#     with github:
#         st.write(
#             "------------------ ------**[GitHub](https://github.com/Adenife)------**"
#         )

#     with tableau:
#         st.write(
#             "**------------------ ------[Tableau](https://public.tableau.com/app/profile/aweda.oluwanifemi.adeola)-----**"
#         )

#     with otherColumn3:
#         st.empty()

#     with otherColumn4:
#         st.empty()


# Projects
with st.container():
    st.write("---")
    analysis, software, engineering = st.tabs(
        ["Data Analysis", "Software Engineering (Backend)", "Data Engineering"]
    )

    with analysis:
        st.write(
            "💡 As a data analyst, I possess a keen eye for patterns and trends hidden within vast datasets. Leveraging my expertise in statistical analysis and data visualization, I extract valuable insights to guide strategic decision-making processes. I have honed my ability to communicate complex analytical findings in a clear and concise manner, ensuring stakeholders understand the implications and opportunities that arise from the data."
        )

        st.write("---")

        with st.container():
            (
                otherColumn3,
                downloadResume,
                linkedin,
                github,
                tableau,
                otherColumn4,
            ) = st.columns(6)
            with downloadResume:
                with open(daPath, "rb") as pdf_file:
                    PDFbyte = pdf_file.read()

                st.download_button(
                    label="Download My Resume",
                    data=PDFbyte,
                    file_name="Oluwanifemi Aweda's Resume.pdf",
                    mime="application/octet-stream",
                    help="Download Resume File",
                )

            with linkedin:
                st.write(
                    "**[LinkedIn](https://www.linkedin.com/in/oluwanifemi-aweda-2b9206118/)**"
                )

            with github:
                st.write("**[GitHub](https://github.com/Adenife)**")

            with tableau:
                st.write(
                    "**[Tableau](https://public.tableau.com/app/profile/aweda.oluwanifemi.adeola)**"
                )

            with otherColumn3:
                st.empty()

            with otherColumn4:
                st.empty()

        st.write("---")

        with st.container():
            st.markdown(
                '<div style="text-align: center;"><h3>Example Projects Worked On</h3></div>',
                unsafe_allow_html=True,
            )
            sectionOne, sectionTwo = st.columns(2)

            with sectionOne:
                # st.image(tableauRepo, use_column_width=True)
                st_lottie(tableauRepo, key="tableau", height=300)
                st.markdown(
                    '<div style="text-align: center;"><a style="text-decoration: none; color: white" href="https://public.tableau.com/shared/NRX9X3BW3?:display_count=n&:origin=viz_share_link"><h3>Tableau Filter Challenge</h3></a></div>',
                    unsafe_allow_html=True,
                )
                st.info(
                    """
                    How well do you know Tableau's order of operations?
                    This challenge is designed to test your knowledge of Tableau's order of operations. In Tableau, filters are applied in a specific order, and the order of the filters can affect the results of the visualization. To complete the challenge, you will need to correctly order the filters in a Tableau visualization.
                    Taka a look at the challenge solution [here](https://public.tableau.com/shared/NRX9X3BW3?:display_count=n&:origin=viz_share_link).
                """
                )

            with sectionTwo:
                # st.image(edaApp, use_column_width=True)
                st_lottie(tableauTrading, key="trade", height=300)
                st.markdown(
                    '<div style="text-align: center;"><a style="text-decoration: none; color: white" href="https://public.tableau.com/views/TradingDashboardCFI_16633312603510/TechnicalAnalysis?:language=en-US&:display_count=n&:origin=viz_share_link"><h3>Trading Dashboard in Tableau</h3></a></div>',
                    unsafe_allow_html=True,
                )
                st.info(
                    """
                    A user-friendly and interactive Tableau trading dashboard built to help traders easily analyze explore trading data and find the information they need at a glance and as qiuck as possible. The project focuses more on trading US stocks. The dashboard includes: Candlestick Chart, Dynamic Bollinger Bands, Volume Chart, Previous Volume High, Relative Growth Chart, Total Growth Table Slicer, Dynamic View Period Selection, Ticker Selection.
                    Try it out [here](https://public.tableau.com/views/TradingDashboardCFI_16633312603510/TechnicalAnalysis?:language=en-US&:display_count=n&:origin=viz_share_link).
                """
                )

        with st.container():
            sectionOne, sectionTwo = st.columns(2)

            with sectionOne:
                st_lottie(covidAnalysis, key="sql1", height=300)
                st.markdown(
                    '<div style="text-align: center;"><a style="text-decoration: none; color: white" href="https://github.com/Adenife/Data-Analysis/blob/main/SQL/covidAnalysis.sql"><h3>Covid-19 Analysis</h3></a></div>',
                    unsafe_allow_html=True,
                )
                st.info(
                    """
                    COVID-19 made the world go on lockdown, so why not analyze how it affected different countries and how these countries were able to contain it?. In this SQL analysis peoject I dived into the Covid dataset to find insight on it's impact in various parts of the world. Skills used include Joins, CTE's, Temp Tables, Windows Functions, Aggregate Functions, Creating Views, Converting Data Types. 
                    Taka a look [here](https://github.com/Adenife/Data-Analysis/blob/main/SQL/covidAnalysis.sql).
                """
                )

            with sectionTwo:
                st_lottie(modeEngagement, key="sql2", height=300)
                st.markdown(
                    '<div style="text-align: center;"><a style="text-decoration: none; color: white" href="https://github.com/Adenife/Data-Analysis/blob/main/SQL/modeEngagementInvestigation.sql"><h3>User Engagement Analysis</h3></a></div>',
                    unsafe_allow_html=True,
                )
                st.info(
                    """
                    You show up to work Tuesday morning, September 2, 2014. The head of the Product team walks over to your desk and asks you what you think about the latest activity on the user engagement dashboards. You are responsible for determining what caused the dip at the end of the chart shown above and, if appropriate, recommending solutions for the problem. 
                    Checkout this SQL customer engagement script [here](https://github.com/Adenife/Data-Analysis/blob/main/SQL/modeEngagementInvestigation.sql).
                """
                )

        with st.container():
            sectionOne, sectionTwo = st.columns(2)

            with sectionOne:
                st_lottie(witcherAnalysis, key="witcher", height=300)
                st.markdown(
                    '<div style="text-align: center;"><a style="text-decoration: none; color: white" href="https://nbviewer.org/github/Adenife/Data-Analysis/blob/main/The%20witcher%20Analysis/witcherFinalAnalysisReport.ipynb"><h3>Witcher Analysis</h3></a></div>',
                    unsafe_allow_html=True,
                )
                st.info(
                    """
                    This project aimed to see the relationship between characters in the witcher book series. Selenium was used to scrape the data from the witcher wiki webpage, spacy was majorly used for the analysis and pyvis was used to visualize the results. See how each character relates to each other in this mind blowing end-to-end project.
                    Taka a look [here](https://nbviewer.org/github/Adenife/Data-Analysis/blob/main/The%20witcher%20Analysis/witcherFinalAnalysisReport.ipynb).
                """
                )

            with sectionTwo:
                st_lottie(googleCapstone, key="capstone", height=300)
                st.markdown(
                    '<div style="text-align: center;"><a style="text-decoration: none; color: white" href="https://github.com/Adenife/Data-Analysis/blob/main/Google%20Capstone%20Case%201/How%20Does%20a%20Bike-Share%20Navigate%20Speedy%20Success_.pdf"><h3>Bike Share Analysis</h3></a></div>',
                    unsafe_allow_html=True,
                )
                st.info(
                    """
                    This Project was done to fulfill the requirements for getting the google data analytics certification hosted on coursera. The case study involves a bikeshare companys data of its customers trip details over a 12 month period (June 2021 - May 2022). The analysis follows the 6 phases of the Data Analysis process as a guideline which includes the; Ask, Prepare, Process, Analyze, and Act phases ***(Using the R programming Language)***.
                    Download my report [here](https://github.com/Adenife/Data-Analysis/blob/main/Google%20Capstone%20Case%201/How%20Does%20a%20Bike-Share%20Navigate%20Speedy%20Success_.pdf).
                """
                )

    with software:
        st.write(
            "💻 With a solid foundation in software engineering, I possess the technical prowess to design and develop robust, scalable solutions. I am adept at leveraging programming languages and frameworks to create innovative software applications that streamline operations, optimize efficiency, and enhance user experiences. My coding expertise empowers me to bridge the gap between software development and data-driven decision-making, resulting in solutions that are both technically sound and business-driven."
        )

        st.write("---")

        with st.container():
            (
                otherColumn3,
                downloadResume,
                linkedin,
                github,
                tableau,
                otherColumn4,
            ) = st.columns(6)
            with downloadResume:
                with open(sePath, "rb") as pdf_file:
                    PDFbyte = pdf_file.read()

                st.download_button(
                    label="Download My Resume",
                    data=PDFbyte,
                    file_name="Oluwanifemi Aweda's Resume.pdf",
                    mime="application/octet-stream",
                    help="Download Resume File",
                )

            with linkedin:
                st.write(
                    "**[LinkedIn](https://www.linkedin.com/in/oluwanifemi-aweda-2b9206118/)**"
                )

            with github:
                st.write("**[GitHub](https://github.com/Adenife)**")

            with tableau:
                st.write(
                    "**[Tableau](https://public.tableau.com/app/profile/aweda.oluwanifemi.adeola)**"
                )

            with otherColumn3:
                st.empty()

            with otherColumn4:
                st.empty()

        st.write("---")

        with st.container():
            st.markdown(
                '<div style="text-align: center;"><h3>Example Projects Worked On</h3></div>',
                unsafe_allow_html=True,
            )
            sectionOne, sectionTwo = st.columns(2)

            with sectionOne:
                st_lottie(twitterBot, key="botornot", height=300)
                st.markdown(
                    '<div style="text-align: center;"><a style="text-decoration: none; color: white" href="https://github.com/Adenife/Twitter-BotOrNot"><h3>Twitter Bot or Not</h3></a></div>',
                    unsafe_allow_html=True,
                )
                st.info(
                    """
                    A Twitter bot detection system using Python, Flask, and Scikit-learn. The project uses a machine learning model to predict whether a Twitter user is a bot or not and flask for API service to interact with the predictor. Check out the repo [here](https://github.com/Adenife/Twitter-BotOrNot).
                """
                )

            with sectionTwo:
                st_lottie(edaApp, key="eda", height=300)
                st.markdown(
                    '<div style="text-align: center;"><a style="text-decoration: none; color: white" href="https://adenife-streamlit-eda-applicationapp-lldgdx.streamlitapp.com/"><h3>EDA Application</h3></a></div>',
                    unsafe_allow_html=True,
                )
                st.info(
                    """
                    A simple Exploratory Data Analysis (EDA) tool in python using the *streamlit* library. The *streamlit* library helps to build data applications with code written purely in python. Upload a dataset (.csv file) and watch the magic happen. Have fun!!!
                    Try out my EDA application [here](https://adenife-streamlit-eda-applicationapp-lldgdx.streamlitapp.com/).
                """
                )

        with st.container():
            sectionOne, sectionTwo = st.columns(2)

            with sectionOne:
                st_lottie(realEstate, key="realestate", height=300)
                st.markdown(
                    '<div style="text-align: center;"><a style="text-decoration: none; color: white" href="https://realestatebrazil.streamlit.app"><h3>Real Estate Analyzer</h3></a></div>',
                    unsafe_allow_html=True,
                )
                st.info(
                    """
                    A streamlit application for residential properties analyzer using Streamlit, Pandas, NumPy, Matplotlib, and Seaborn libraries. The app features 2 stripplots, the first stripplot, which compares the selected location's annual appreciation to other locations, and the second stripplot, which shows the relationship between location and price per square meter. Check out the repo [here](https://realestatebrazil.streamlit.app).
                """
                )

            with sectionTwo:
                pass

    with engineering:
        st.write(
            "🔌 In the realm of data engineering, I have a strong command of the tools and technologies required to efficiently collect, transform, and store large volumes of data. Whether it involves architecting data pipelines, implementing ETL processes, or managing databases, I possess the know-how to ensure data integrity and availability. By seamlessly integrating data engineering practices, I enable organizations to harness the full potential of their data assets."
        )

        st.write("---")

        with st.container():
            (
                otherColumn3,
                downloadResume,
                linkedin,
                github,
                tableau,
                otherColumn4,
            ) = st.columns(6)
            with downloadResume:
                with open(dePath, "rb") as pdf_file:
                    PDFbyte = pdf_file.read()

                st.download_button(
                    label="Download My Resume",
                    data=PDFbyte,
                    file_name="Oluwanifemi Aweda's Resume.pdf",
                    mime="application/octet-stream",
                    help="Download Resume File",
                )

            with linkedin:
                st.write(
                    "**[LinkedIn](https://www.linkedin.com/in/oluwanifemi-aweda-2b9206118/)**"
                )

            with github:
                st.write("**[GitHub](https://github.com/Adenife)**")

            with tableau:
                st.write(
                    "**[Tableau](https://public.tableau.com/app/profile/aweda.oluwanifemi.adeola)**"
                )

            with otherColumn3:
                st.empty()

            with otherColumn4:
                st.empty()

        st.write("---")


with st.container():
    left, main, right = st.columns([1, 3, 1])

    with left:
        st.empty()

    with main:
        with st.form(key="send_mail", clear_on_submit=True):
            st.markdown(
                '<div style="text-align: center;"><h2>Get in Touch With Me!</h2></div>',
                unsafe_allow_html=True,
            )
            st.write("---")
            sender_name = st.text_input(label="Your Name")
            sender_mail = st.text_input(label="Your Mail")
            email_body = st.text_area(label="Your Message Here...")

            # Define the transport variables
            ctx = ssl.create_default_context()
            password = st.secrets["password"]  # Your app password goes here
            sender = st.secrets["sender"]  # Your e-mail address
            receiver = st.secrets["receiver"]  # Recipient's address

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
            if submitted and sender_name and sender_mail and email_body:
                # Connect with server and send the message
                with smtplib.SMTP_SSL(
                    "smtp.gmail.com", port=465, context=ctx
                ) as server:
                    server.login(sender, password)
                    server.sendmail(sender, receiver, message.as_string())

                st.success("Mail Successfully Sent!!!")

            else:
                st.warning("Fill in the information correctly")

    with right:
        st.empty()