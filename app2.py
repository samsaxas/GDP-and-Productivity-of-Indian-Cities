#final code

import streamlit as st
import streamlit.components.v1 as components
import base64
import pandas as pd
from datetime import datetime
import pymongo
from bson.objectid import ObjectId
import bcrypt

# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["dashboard_db"]
users_collection = db["users"]

# Function to hash passwords
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Function to verify hashed passwords
def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)


# Login page
def login():
    st.title("Login")
    
    # Custom styling for the labels
    st.markdown(
        """
        <style>
        .custom-label {
            font-size: 24px; /* Increase font size */
            color: #06535e; /* Change font color to white */
            font-family: Arial, sans-serif;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    # Display the labels and inputs
    st.markdown('<label class="custom-label">Username</label>', unsafe_allow_html=True)
    username = st.text_input("", key="login_username")  # Empty label for custom styling
    
    st.markdown('<label class="custom-label">Password</label>', unsafe_allow_html=True)
    password = st.text_input("", type="password", key="login_password")  # Empty label for consistency
    
    if st.button("Login"):
        user = users_collection.find_one({"username": username})
        if user and bcrypt.checkpw(password.encode("utf-8"), user["password"]):
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success("Logged in successfully!")
        else:
            st.error("Invalid username or password. Please try again.")




# Signup page
def signup():
    st.title("Signup")
    
    # Custom styling for the labels
    st.markdown(
        """
        <style>
        .custom-label {
            font-size: 20px; /* Increase font size */
            color: white; /* Change font color to white */
            font-family: Arial, sans-serif;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    # Display the labels and inputs
    st.markdown('<label class="custom-label">Username</label>', unsafe_allow_html=True)
    username = st.text_input("", key="signup_username")  # Empty label to keep space for custom label
    
    st.markdown('<label class="custom-label">Password</label>', unsafe_allow_html=True)
    password = st.text_input("", type="password", key="signup_password")  # Empty label for consistency
    
    if st.button("Signup"):
        if users_collection.find_one({"username": username}):
            st.error("Username already exists. Please choose another.")
        else:
            hashed_password = hash_password(password)
            users_collection.insert_one({"username": username, "password": hashed_password})
            st.success("User registered successfully! Please login.")




import streamlit as st

def set_background():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
        .stApp {
            background-color: #ebf0f5;
            color: #06535e;
            font-family: 'Roboto', sans-serif;
        }
        .css-1d391kg {
            background-color: #f2f2f2;
        }
        .css-1d391kg .sidebar-content {
            color: #06535e;
        }
        .hero-section {
            text-align: center;
            padding: 100px 20px;
            background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://i0.wp.com/thecuriouseconomist.com/wp-content/uploads/2024/04/India-Economic-Growth-1.png?resize=600%2C381&ssl=1');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 400px;
        }
        .hero-section h1, .hero-section p {
            color: #ffffff;
        }
        .hero-section h1 {
            font-size: 48px;
            margin-bottom: 10px;
        }
        .hero-section p {
            font-size: 24px;
            margin-bottom: 20px;
        }
        .content-section {
            padding: 10px;
            max-width: 1200px;
            margin: auto;
        }
        .section-title {
            font-size: 24px;
            color: #06535e;
            margin-bottom: 10px;
            font-weight: bold;
        }
        .section-content {
            font-size: 18px;
            color: #4f4f4f;
            text-align: justify;
        }
        .button-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            gap: 10px;
        }
        .report-button {
            background-color: #06535e;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            border: none;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
            cursor: pointer;
            text-align: center;
            font-size: 16px;
            transition: transform 0.3s ease;
            width: 48%;
            height: 150px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        .report-button:hover {
            transform: translateY(-2px);
            box-shadow: 0px 6px 8px rgba(0, 0, 0, 0.3);
        }
        .name {
            font-weight: bold;
            font-size: 18px;
            text-decoration: underline;
            margin-bottom: 5px;
        }
        .desc {
            font-size: 14px;
            text-align: center;
        }
        .stAppHeader, .stDecoration, .stAppToolbar {
            background-color: #ebf0f5;
            color: #268bd4;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def home_page():
    st.markdown(
        """
        <div class="hero-section">
            <h1>Exploring the Economic Pulse of Indian Cities</h1>
            <p>Insights into GDP and Productivity Across Urban India</p>
        </div>
        <div class="content-section">
            <div class="section-title">Introduction</div>
            <div class="section-content">
                Welcome to our comprehensive resource on the GDP and productivity of Indian cities. Our aim is to provide valuable insights and data to help you understand the economic dynamics shaping India's urban landscapes.
            </div>
        </div>
        <div class="content-section">
            <div class="section-title">Overview</div>
            <div class="section-content">
                Our Dashboard offers detailed visualizations of GDP and productivity data. Check out the Conclusion page for insights and analysis.
            </div>
        </div>
        <div class="content-section">
            <div class="section-title">Understanding the data</div>
            <div class="section-content">
                <p><b>GDP:</b> Gross Domestic Product - the total value of goods produced and services provided in a city or country during one year.</p>
                <p><b>R&D:</b> Research and Development - activities in connection with corporate or governmental innovation.</p>
                <p><b>ICT:</b> Information and Communication Technology - an extended term for information technology (IT) which stresses the role of unified communications and the integration of telecommunications and computers.</p>
                <p><b>SME:</b> Small and Medium-sized Enterprises - businesses whose personnel numbers fall below certain limits.</p>
                <p><b>GDP Trends:</b> Refers to the changes in GDP over a certain period.</p>
                <p><b>City-wise GDP Comparison:</b> Comparing the GDP values of different cities.</p>
                <p><b>Geographical Representation:</b> Visualization of data on a map.</p>
                <p><b>Sector Contributions:</b> The contribution of different sectors (e.g., Agriculture, Industry, Services, Technology) to the GDP.</p>
                <p><b>Unemployment Rate:</b> The percentage of the total workforce that is unemployed and actively seeking employment.</p>
                <p><b>Youth Unemployment Rate:</b> The percentage of the workforce between specific ages (usually 15-24) that is unemployed.</p>
                <p><b>Patents per 100,000 Inhabitants:</b> The number of patents granted per 100,000 people in a city or country.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Calling the functions
set_background()




def dashboard_page():
    st.header("Power BI Dashboard")
    st.markdown(
        """
        <iframe title="Milestone2 dashboard - Copy - Copy" width="800" height="508" src="https://app.powerbi.com/view?r=eyJrIjoiZDYwNjdkNzgtODIwYy00NTk0LWJlYWYtZTU2ZjBmODlmNmMxIiwidCI6ImFlODc0N2EyLThhM2UtNGIyMi1iM2MyLTdlZjlhNDk0ZGZhMyJ9&pageName=4079d86eb763de173575" frameborder="0" allowFullScreen="true"></iframe>
        """,
     
        unsafe_allow_html=True
    )


def conclusion_page():
    st.markdown(
        """
        <div class="hero-section">
            <h1>Concluding Insights on Economic Trends</h1>
            <p>Comprehensive Analysis of GDP, R&D, and Employment Data Across Indian Cities</p>
        </div>
        <div class="content-section">
            <div class="section-title">GDP Analysis</div>
            <div class="section-content">
                <p><b>Total GDP:</b> The overall GDP for the region stands at 12.92K, reflecting the collective economic strength of urban India.</p>
                <p><b>GDP Trends:</b> The analysis of GDP trends from 2019 to 2023 shows fluctuating growth across cities such as Bengaluru, Hyderabad, and Mumbai.</p>
                <p><b>City-wise GDP Comparison:</b> Kolkata leads with the highest GDP at 1.10K, while Delhi reports the lowest GDP of 0.53K.</p>
                <p><b>Geographical Representation:</b> A map illustrating GDP values across Indian cities, with larger circles representing higher GDP values.</p>
            </div>
        </div>
        <div class="content-section">
            <div class="section-title">R&D Expenditure</div>
            <div class="section-content">
                <p><b>Total R&D Expenditure:</b> The total investment in R&D across cities amounts to 87.45, with a significant annual fluctuation.</p>
                <p><b>R&D Expenditure Over the Years:</b> From 2019 to 2023, the R&D expenditure has seen some declines, from 16.6 in 2019 to 15.7 in 2023.</p>
                <p><b>City-wise R&D Expenditure:</b> Cities like Chennai and Bengaluru show higher R&D investments, while other cities fall behind in comparison.</p>
                <p><b>Geographical Representation:</b> The map displays R&D expenditure as a percentage of GDP across different cities in India.</p>
            </div>
        </div>
        <div class="content-section">
            <div class="section-title">Sector Contributions</div>
            <div class="section-content">
                <p><b>Sector Contribution by City:</b> Hyderabad leads in services, while Ahmedabad has a greater proportion of industry-driven GDP.</p>
                <p><b>City-wise Sector Data:</b> Ahmedabad's industrial contribution stands at 34%, while Hyderabad's services contribute 46% to its GDP.</p>
                <p><b>Cumulative Sector Growth:</b> The agriculture sector remains stable, while industry and services show gradual growth, with technology making an upward trend.</p>
            </div>
        </div>
        <div class="content-section">
            <div class="section-title">Unemployment Insights</div>
            <div class="section-content">
                <p><b>Total Unemployment Rate:</b> The total unemployment rate is reported at 456.30 across all cities.</p>
                <p><b>Youth Unemployment Rate:</b> Youth unemployment rates vary significantly, with cities like Kolkata showing higher rates than others.</p>
                <p><b>ICT Sector Unemployment:</b> The ICT sector's unemployment rate of 1.19K signals challenges in employment in the tech industry.</p>
                <p><b>SME Sector Employment:</b> The SME sector continues to employ a significant portion of the workforce, employing 2.09K individuals in total.</p>
                <p><b>Tourism Sector Employment:</b> Employment in the tourism sector is at 501.00, indicating its importance for urban economies.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


    # Feedback Form Section
    col1, col2, col3 = st.columns([0.1, 1, 0.1])  # Adjusting column layout for feedback form
    
    with col2:
        st.markdown("<h2 style='font-size:40px; font-family: Tahoma, sans-serif; color:#06535e;'>We Value Your Feedback</h2>", unsafe_allow_html=True)
        
        with st.form("feedback_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            feedback = st.text_area("Your Feedback")
            
            submit_button = st.form_submit_button("Submit Feedback")
      
            if submit_button:
                feedback_data = {
                    "Name": name,
                    "Email": email,
                    "Feedback": feedback,
                    "Timestamp": datetime.now()
                }
                st.write("Thank you for your feedback!")
                  # Display feedback data (for customization, you can save this data)
    
    # Chatbot UI Section
    st.markdown("<h2 style='font-size:32px; font-family: Tahoma, sans-serif; color:#06535e;'>Chat with Us</h2>", unsafe_allow_html=True)

    # Closing div tag
    st.markdown("</div>", unsafe_allow_html=True)

    # Add chatbot script (your previous script)
    chatbot_script = """ 
    <style> 
    .chatbot-container { 
        position: fixed; 
        bottom: 0; 
        left: 50%; 
        transform: translateX(-50%); 
        z-index: 100;
        height: 80px; 
        width: 80px; 
        background: transparent;
    }
    </style> 

    <div class="chatbot-container"> 
        <script>
        (function(){
            if(!window.chatbase || window.chatbase("getState") !== "initialized"){
                window.chatbase = (...arguments) => {
                    if(!window.chatbase.q) {
                        window.chatbase.q = []
                    }
                    window.chatbase.q.push(arguments)
                };
                window.chatbase = new Proxy(window.chatbase, {
                    get(target, prop) {
                        if (prop === "q") {
                            return target.q
                        }
                        return (...args) => target(prop, ...args)
                    }
                })
            }
            const onLoad = function() {
                const script = document.createElement("script");
                script.src = "https://www.chatbase.co/embed.min.js";
                script.id = "eNBqRad92IKScVOKZD4u1";
                script.domain = "www.chatbase.co";
                document.body.appendChild(script)
            };
            if (document.readyState === "complete") {
                onLoad()
            } else {
                window.addEventListener("load", onLoad)
            }
        })();
        </script>
    </div> 
""" 

    components.html(chatbot_script, height=1000, width = 500, scrolling=True)


# Logout function to handle the logout process
def logout():
    st.session_state["logged_in"] = False
    st.session_state.page = "Login"  # Redirect to Login page
    st.success("You have been logged out.")

# Main function
def main():

    # Initialize session state
    if "page" not in st.session_state:
        st.session_state.page = "Home"

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    # Sidebar setup
    if st.session_state["logged_in"]:
        st.sidebar.title("Navigation")

        # Define buttons for navigation with unique keys
        st.markdown(
            """
            <style>
            .stButton > button {
                background-color: white;
                font-family: Tahoma, sans-serif;
                font-size: 24px;
                color: #050114;
                border: 2px solid #050114;
                padding: 15px 30px; /* Button size */
                box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
                transition: box-shadow 0.3s ease, background-color 0.3s ease, border-color 0.3s ease, color 0.3s ease;
            }
            .stButton > button:hover {
                background-color: #050114;
                color: white;
                border-color: #050114;
                box-shadow: 0px 0px 25px rgba(0,0,0,0.2);
            }
            .stButton > button:active,
            .stButton > button:focus {
                background-color: #050114 !important;
                color: white !important;
                border-color: #050114 !important;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        if st.sidebar.button("🏠 Home", key="home_button"):
            st.session_state.page = "Home"
        if st.sidebar.button("📊 Dashboard", key="dashboard_button"):
            st.session_state.page = "Dashboard"
        if st.sidebar.button("📝 Conclusion", key="conclusion_button"):
            st.session_state.page = "Conclusion"
        
        # Add a Logout button in the sidebar
        if st.sidebar.button("🚪 Logout", key="logout_button"):
            logout()  # Handle the logout process

        # Render the selected page
        if st.session_state.page == "Home":
            home_page()
        elif st.session_state.page == "Dashboard":
            dashboard_page()
        elif st.session_state.page == "Conclusion":
            conclusion_page()
    else:
        # Show login/signup options when not logged in
        option = st.sidebar.selectbox("Choose an option", ["Login", "Signup"])
        if option == "Login":
            login()
        elif option == "Signup":
            signup()


if __name__ == "__main__":
    main()