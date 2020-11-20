import streamlit as st
import numpy as np
import pickle


clf = pickle.load(open("diabetes_model.pkl", "rb"))

def predict_diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, Bmi, DiabetesPedigreeFunction, Age):
    p = int(Pregnancies)
    g = float(Glucose)
    bp = float(BloodPressure)
    stk = float(SkinThickness)
    ins = float(Insulin)
    bmi = float(Bmi)
    dpf = float(DiabetesPedigreeFunction)
    age = int(Age)

    data = np.array([[p, g, bp, stk, ins, bmi, dpf, age]])

    prediction = clf.predict(data)[0]

    return prediction

def Mainapp():
    st.title("Diabetes Detection using ML")
    st.write("""
    ## What is diabetes

    According to the NIH, "Diabetes is a disease that occurs when your **blood glucose**,
     also called blood sugar, is **too high**. Blood **glucose** is your main source of
      energy and **comes from the food you eat**. **Insulin**, a hormone made from the pancreas,
       **helps glucose** from food get into your cells to be used for energy. Sometimes your 
       body doesn’t make enough or any insulin or doesn’t use insulin well. Glucose then stays 
       in your blood and doesn’t reach your cells.
    Over time, **having too much glucose in your blood** can cause health problems. """)
    st.sidebar.title("Write your Data here")
    p = st.sidebar.text_input("No. of Pregnancies", "0")
    if (int(p) > 25) or (int(p) < 0):
        st.warning("Value must be NON-NEGATIVE and WITHIN RANGE [0, 25]")
        return
    g = st.sidebar.text_input("Glucose Level (mg/dL)", "70")
    if float(g) < 0:
        st.warning("Value must be NON-NEGATIVE")
        return
    bp = st.sidebar.text_input("Blood Pressure (mmHg)", "85")
    if float(bp) < 0:
        st.warning("Value must be NON-NEGATIVE")
        return
    stk = st.sidebar.text_input("Skin Thickness (mm)", "30")
    if float(stk) < 0:
        st.warning("Value must be NON-NEGATIVE")
        return

    ins = st.sidebar.text_input("Insulin Level (mIU/mL)", "80")
    if float(ins) < 0:
        st.warning("Value must be NON-NEGATIVE")
        return

    bmi = st.sidebar.text_input("Body Mass Index", "25")
    if float(bmi) < 0:
        st.warning("Value must be NON-NEGATIVE")
        return

    dpf = st.sidebar.text_input("Diabetes Pedigree Function", "0.5")
    if float(dpf) < 0:
        st.warning("Value must be NON-NEGATIVE")
        return

    age = st.sidebar.text_input("Age (years)", "30")
    if int(g) < 0:
        st.warning("Value must be NON-NEGATIVE")
        return

    safe_html = """
    <div style="background-color:#1D8348; padding:10px">
    <h2 style="color:white; text-align:center;">You don't have diabetes! &#128512;</h2>
    </div>
    """

    unsafe_html = """
    <div style="background-color:#CB4335; padding:10px">
    <h2 style="color:white; text-align:center;">You have diabetes. &#128577;</h2>
    </div>
    """

    st.write("## ** PREDICT ** ")
    if st.checkbox("Do you want to know if you have diabetes? "):
        st.write("""     Please fill the required values given in navigation bar on left and click predict""")
    
    if st.sidebar.button("PREDICT"):
        output = predict_diabetes(p, g, bp, stk, ins, bmi, dpf, age)
        st.markdown("""### Data Processed""", True)

        if output == 1:
            st.markdown(unsafe_html, unsafe_allow_html=True)
        else:
            st.markdown(safe_html, unsafe_allow_html=True)
        st.write("""
         
        ** This result is based on model we created using Machine Learning.
           Keep in mind that this result cannot replace a professional doctor's diagnosis. **
         """)

    st.write("## More on Diabetes")
    if st.checkbox("MORE ON DIABETES"):
        st.write("""

        Although diabetes has no cure, you can take steps to manage your diabetes and stay healthy.
        Sometimes people call diabetes “a touch of sugar” or “borderline diabetes.” These terms suggest that someone doesn’t really have diabetes or has a less serious case, but every case of diabetes is serious.
        What are the different types of diabetes? The most common types of diabetes are type 1, type 2, and gestational diabetes.

        - Type 1 diabetes: If you have type 1 diabetes, your body does not make insulin. Your immune system attacks and destroys the cells in your pancreas that make insulin. Type 1 diabetes is usually diagnosed in children and young adults, although it can appear at any age. People with type 1 diabetes need to take insulin every day to stay alive.

        - Type 2 diabetes: If you have type 2 diabetes, your body does not make or use insulin well. You can develop type 2 diabetes at any age, even during childhood. However, this type of diabetes occurs most often in middle-aged and older people. Type 2 is the most common type of diabetes.

        ### Gestational diabetes 
        Gestational diabetes develops in some women when they are pregnant. Most of the time, this type of diabetes goes away after the baby is born. However, if you’ve had gestational diabetes, you have a greater chance of developing type 2 diabetes later in life. Sometimes diabetes diagnosed during pregnancy is type 2 diabetes.
        Other types of diabetes Less common types include monogenic diabetes, which is an inherited form of diabetes, and cystic fibrosis-related diabetes.
        """)
    st.write("## Health Measures")
    if(st.checkbox("Health Measures")):
        st.write("""
            1. Make a commitment to managing your diabetes
            2. Don't smoke
            3. Keep your blood pressure and cholesterol under control
            4. Schedule regular physicals and eye exams
            5. Keep your vaccines up to date
            6. Take care of your teeth(Diabetes may leave you prone to gum infections)
            7. Consider a daily aspirin
            8. If you drink alcohol, do so responsibly
            9. Stop being stressed
        """)
        
    
if __name__ == "__main__":
    Mainapp()

    
