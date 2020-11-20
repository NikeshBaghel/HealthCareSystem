import streamlit as st

def race():
    st.title('Global Total Cases')
    st.markdown('### Click Play ▶️ at the bottom of the graph')
    #st.selectionbox()
    plots = st.radio('Choose a type of plot',('Bar Plot','Line Plot'))
    if plots == 'Bar Plot':
        st.markdown("""<html>
        <div class="flourish-embed" data-src="story/305795" data-url="https://flo.uri.sh/story/305795/embed">
        <script src="https://public.flourish.studio/resources/embed.js"></script>
        <iframe src=\"https://flo.uri.sh/story/305795/embed" frameborder=\"0\" scrolling=\"no\" height=\"810\" width=\"2000\" style=\"width:125%;\"></iframe>
        </div></html>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""<html>
        <div class="flourish-embed" data-src="story/307671" data-url="https://flo.uri.sh/story/307671/embed">
        <script src="https://public.flourish.studio/resources/embed.js"></script></div>
        <iframe src=\"https://flo.uri.sh/story/307671/embed" frameborder=\"0\" scrolling=\"no\" height=\"810\" width=\"2000\" style=\"width:125%;\"></iframe>
        </div></html>
        """, unsafe_allow_html=True)
    st.write('©Nikeshsingh Baghel ©Mehnaz Sheikh')
    
if __name__ == "__main__":
    race()
