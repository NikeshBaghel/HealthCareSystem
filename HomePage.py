import streamlit as st
import Analyser as ast
import Covid19_Data2 as cvd
import DiabetesAnalyser as da

sel = st.sidebar.selectbox("Select as per requirement: ",["Home Page","COVID-19","Diabetes"],index = 0)

if(sel == "Home Page"):
    page_bg_img = '''
		<div style="background-color: #3BCA14; width: 85%;padding-left: 5%;border-radius: 8px 8px;padding-bottom: 1%">
			<h1 style="color: white">Welcome to Healthcare System</h1>
		</div>
				<h3>This project is an effort towards building an online healthcare system<br>We have included COVID-19 and Diabetes as options and we will include furthur options in future<br>We have used Machine Learning for prediction and visualization of data</h3>

		<div style="background-color: #ED7D53; width: 60%;padding-left: 5%;margin-top: 3%;border-radius: 5px 5px;padding-bottom: 1%">
			<h2>Choose an option from left</h2>
		</div>


    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.write("** This webpage is incomplete **")
    #st.write("# WELCOME TO HEALTHCARE SYSTEM")
    #st.write("Choose from options on left")
if(sel == "COVID-19"):
    sel2 = st.sidebar.radio("SELECT: ",["Covid Cases Comparator","Visual Analyser"])
    if(sel2 == "Visual Analyser"):
        st.write("** Close the navigation bar on left for better experience **")
        ast.race()
    elif("Covid Cases Comparator"):
        cvd.CovidCases()
    else:
        pass
elif(sel == "Diabetes"):
    da.Mainapp()
else:
    pass

    
