import streamlit as st
import my_utils
import time
from PIL import Image

is_src_uploaded = False
is_style_uploaded = False
src_img = None
res_img = None

st.set_page_config(page_title="Style transfer tool",
                   page_icon=":mage:",
                  )

st.write("# :zap: Welcome to style transfer tool! :magic_wand:")

st.sidebar.header("Current state:")
if "curr_state" not in st.session_state:
    st.session_state.curr_state = 'waiting'
if "curr_progress" not in st.session_state:
    st.session_state.curr_progress = 0

progr_bar = st.sidebar.progress(st.session_state.curr_progress)

st.sidebar.markdown(
    """
    This tool uses [Neural Style Transfer (NST)](https://neerc.ifmo.ru/wiki/index.php?title=Neural_Style_Transfer) principles.
    #### How to proceed:
    1. Choose an image file to be modified. 
    2. Choose style (now restricted by two options). Now for testing only filters are applyed to image. For case 'style 1' - contour filter. For 'style 2' - blur.
    3. Wait for result. It will appear in section 3 of main page.
    4. To refresh page press 'Refresh' button on sidebar below.
    The current state can be checked on top of sidebar
    """
)

refresh_button = st.sidebar.button(label='refresh')
                                 
# upload source file to be modified
st.markdown('## 1. Choose an image file to be styled')
img_file = st.file_uploader('upload an image file')
if img_file is not None:
    with Image.open(img_file) as src_img:
        with st.expander('Click here to see uploaded image'):
            st.write('Original image')
            st.image(src_img)
            is_src_uploaded = True # if upload correct
            st.session_state.curr_state = 'waiting'
            progr_bar.progress(10)
            
            
# uploading styling file image (an example of style)
st.markdown('## 2. Choose a style to apply')
style = st.selectbox('Choose a style to transfer',
                     ('style_1',
                      'style_2',
                     ),
                     index=None
                    )
if style is not None:
    with st.expander('Click here to see chosen style'):
        st.write(f'You select {style}')
        style_img_file = f'style_imgs/{style}.jpg'
        with Image.open(style_img_file) as style_img:
            st.image(style_img)
            is_style_uploaded = True #if upload correct
            st.session_state.curr_state = 'waiting'
            progr_bar.progress(10)
            if is_src_uploaded:
                st.session_state.curr_state = 'ready'
                progr_bar.progress(20)

# show result when succeed
st.markdown('## 3. Result of style transfer')
st.write('Now for testing only contour or blur filters are applied')
if is_src_uploaded and is_style_uploaded:
    st.session_state.curr_state = 'ready'
    
    # emulate progress
    for i in range(20, 100):
        progr_bar.progress(i+1)
        time.sleep(0.02)

    # show result
    res_img = my_utils.styling(src_img, style)
    if res_img is not None:
        st.image(res_img)
        st.session_state.curr_state = 'result'