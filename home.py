import streamlit as st
import base64

def home():

    # Page configs (tab title, favicon)
    st.set_page_config(
        page_title="Prashant's Portfolio",
        page_icon="computer",
    )

    # CSS styles file
    with open("styles/main.css") as f:
        st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Profile image file
    with open("assets/profile_prashant.jpg", "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()

    # PDF Resume file
    with open("assets/prashant_resume.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    # Top title
    st.write(f"""<div class="title"><strong>Hi! My name is</strong> Prashant Singh👋</div>""", unsafe_allow_html=True)

    # Profile image
    # st.write(f"""
    # <div class="container">
    #     <div class="box">
    #         <div class="spin-container">
    #             <div class="shape">
    #                 <div class="bd">
    #                     <img src="{img}" alt="Enric Domingo">
    #                 </div>
    #             </div>
    #         </div>
    #     </div>
    # </div>
    # """,
    # unsafe_allow_html=True)

    # Alternative image (static and rounded) uncomment it if you prefer this one
    st.write(f"""
    <div style="display: flex; justify-content: center;">
       <img src="{img}" alt="Prashant Singh" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
    </div>
    """, unsafe_allow_html=True)

    # Subtitle
    st.write(f"""<div class="subtitle" style="text-align: center;">Software Engineer (Open to work)</div>""", unsafe_allow_html=True)

    # Social Icons
    social_icons_data = {
        # Platform: [URL, Icon]
        # "Kaggle": ["https://www.kaggle.com/", "https://www.kaggle.com/static/images/site-logo.svg"],
        "LinkedIn": ["https://www.linkedin.com/in/prshntsingh/", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/prshntsingh", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"],
        # "Twitter": ["https://twitter.com/", "https://cdn-icons-png.flaticon.com/512/733/733579.png"],
        # "YouTube": ["https://www.youtube.com/@", "https://cdn-icons-png.flaticon.com/512/1384/1384060.png"],
        "Medium": ["https://medium.com/@prashantsingh_63355", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Medium_logo_Monogram.svg/1200px-Medium_logo_Monogram.svg.png"],
        "Leetcode": ["https://leetcode.com/prshntsingh2010/", "https://upload.wikimedia.org/wikipedia/commons/1/19/LeetCode_logo_black.png?20191202080835"],

    }

    social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'></a>" for platform in social_icons_data]

    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>""",
    unsafe_allow_html=True)

    st.write("##")

    # About me section
    st.subheader("About Me")
    st.write("""
    - 🎓 I am a **Bachelor of Engineering** graduate from [Birla Institute of Technology, Mesra](https://www.bitmesra.ac.in/) and have 4 years of experience in Software Engineering.
    
    - 🧑‍💻 I am a **Backend and Platform Engineer** @ [Airbase](https://www.airbase.com/) working on Cashback and Pricing contracts. 

    - 🛩️ Prev: Software Engineer @ [Paysafe](https://www.paysafe.com/en/)

    - ❤️ I am passionate about **Web development, Artificial Intelligence, Startups, Cloud computing, Data, Software Engineering, DSA, Optimization, Automation**, and more!

    - 🤖 I enojy developing projects, photography and participating at platforms like [Leetcode](https://leetcode.com/prshntsingh2010/) 📈

    - 🏂 Also practicing sports such as cricket, football and badminton 🧗
    
    - 🏠 Bengaluru, India

    - 📫 Contact me: \n
       - 📩: prshntsingh2010@gmail.com
       - 📞: +91-8294246578
    """)

    st.write("##")

    # Download CV button
    st.download_button(
        label="📄 Download my CV",
        data=pdf_bytes,
        file_name="Prashant_Resume.pdf",
        mime="application/pdf",
    )

    st.write("##")

    # st.write(
    #     f"""<div class="subtitle" style="text-align: center;">⬅️ Check out my Projects in the navigation menu! (Coming soon...)</div>""",
    #     unsafe_allow_html=True)


if __name__ == "__main__":
    home()