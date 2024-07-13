import streamlit as st

from PIL import Image, ImageFilter

def sidebar_state(curr_state:str) -> None:
    """Change current state on the sidebar.
    Possible states(hardcoded): 'waiting', 'ready', 'progress', 'result'.
    Other states arise unexpected state

    Args:
        curr_state (str): current state to choose text and color
    """
    if curr_state == 'waiting':
        st.sidebar.error('Waiting correct input')
    elif curr_state == 'ready':
        st.sidebar.success('Ready to proceed')
    elif curr_state == 'progress':
        st.sidebar.warning('In progress')
    elif curr_state == 'result':
        st.sidebar.success('Showing results')
    else:
        st.sidebar.error('Unexpected state')


def styling(src_img:Image, style:str)->Image:
    """Styling module. For testing purpose, only PIL filter is applied

    Args:
        src_img (Image): source image to be modified
        style (str): style name allow to choose filter

    Returns:
        Image: modified image
    """
    filter_name = ImageFilter.CONTOUR if style=='style_1' else ImageFilter.BLUR
    return src_img.filter(filter_name)