#%%libraries
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# Set page config
st.set_page_config(page_title="My Streamlit App", page_icon=":smiley:", layout="wide")


#%%Set the background
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('images/bg.png')   

# st.image('https://wallpaperboat.com/wp-content/uploads/2019/10/free-website-background-07.jpg')


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/

#%%
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/V.png")
img_lottie_animation = Image.open("images/V.png")

#%% ---- HEADER SECTION ----
with st.container():
    st.subheader("Designed by 'QTool' ")
    st.title("Results of post-processing of the simulation")
    #st.write("[Learn More about Arash](https://www.linkedin.com/in/arash-hajisharifi-275173101/?originalSubdomain=it)")
    # st.write("[My personal website](https://it.linkedin.com/in/sajad-salavatidezfouli-26477978/it?trk=org-employees)")

#%% ---- First Sets of Results----

img_pv = Image.open("images/pv.png")
# Scale down the image by half
new_width = 300
new_height = 300
img_pv = img_pv.resize((new_width, new_height))

img_python = Image.open("images/python.png")
img_python = img_python.resize((new_width, new_height))

img_bash = Image.open("images/bash.png")
img_bash = img_bash.resize((new_width, new_height))

with st.container():
    st.write("---")
    left_column, mid1_column, mid2_column, right_column = st.columns(4)
    with left_column:
        st.header("A Brief Description")
        st.write("##")
        st.write(
            """
            - All the post-processing contours are derived with paraview.
            - A python code has been developed to extract data.
            - Automation process is handled with bash script.

            """
        )
    with mid1_column:
        st.image(img_python)
    with mid2_column:
        st.image(img_bash)
    with right_column:
            st.image(img_pv)

#%% ---- PP ----

img_v = Image.open("images/1.png")
img_T = Image.open("images/2.png")
img_P = Image.open("images/3.png")
img_meshes = Image.open("images/4.png")
img_VT_center = Image.open("images/5.png")

with st.container():
    st.write("---")
    st.header("Visualization")
    st.markdown("<span style='color:yellow;'>This part includes all the visualization data ", unsafe_allow_html=True)

    #Mesh    
    st.subheader("")
    st.markdown("<span style='color:lightblue; font-size:30px;'>XY View</span>", unsafe_allow_html=True)
  
    st.write("##")
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        st.image(img_meshes)




    #Temperature    
    st.subheader("")
    st.markdown("<span style='color:lightblue; font-size:30px;'>YZ View</span>", unsafe_allow_html=True)
  
    st.write("##")
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        st.image(img_T)



    #Pressure    
    st.subheader("")
    st.markdown("<span style='color:lightblue; font-size:30px;'>ZX View Field</span>", unsafe_allow_html=True)
  
    st.write("##")
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        st.image(img_P)






    #velocity    
    st.subheader("")
    st.markdown("<span style='color:lightblue; font-size:30px;'>3D View</span>", unsafe_allow_html=True)
  
    st.write("##")
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        st.image(img_v)



    #Centerline Velocity and Temperature    
    st.subheader("")
    st.markdown("<span style='color:lightblue; font-size:30px;'>3D View</span>", unsafe_allow_html=True)
  
    st.write("##")
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        st.image(img_VT_center)






#%% ---- CONTACT ----
# with st.container():
#     st.write("---")
#     st.header("Get In Touch With Me!")
#     st.write("##")

#     # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
#     contact_form = """
#     <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
#         <input type="hidden" name="_captcha" value="false">
#         <input type="text" name="name" placeholder="Your name" required>
#         <input type="email" name="email" placeholder="Your email" required>
#         <textarea name="message" placeholder="Your message here" required></textarea>
#         <button type="submit">Send</button>
#     </form>
#     """
#     left_column, right_column = st.columns(2)
#     with left_column:
#         st.markdown(contact_form, unsafe_allow_html=True)
#     with right_column:
#         st.empty()
