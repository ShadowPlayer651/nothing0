import streamlit as st
import random
import time

# Inject custom dark CSS for a truly immersive, shadowy experience
st.markdown(
    """
    <style>
    body {
        background-color: #121212;
        color: #e0e0e0;
    }
    .dark-heading {
        font-family: 'Courier New', Courier, monospace;
        color: #FF5555;
        text-align: center;
    }
    .dark-log {
        font-family: 'Courier New', Courier, monospace;
        color: #00FF41;
        white-space: pre-wrap;
    }
    .button-dark {
        background-color: #333333;
        color: #e0e0e0;
        border: 1px solid #444444;
        padding: 0.5em 1em;
        border-radius: 4px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Dark header
st.markdown("<h1 class='dark-heading'>GL1TCH.BACKROAM</h1>", unsafe_allow_html=True)
st.write("Wandering the forgotten corridors of decayed memory...")

# A button to "enter" the obsidian archive
if st.button("Enter OBSIDIAN ARCHIVE"):
    st.warning("Accessing lost files... Please hold as fragments assemble.")
    time.sleep(1)
    
    # Simulated archive logs
    archive_logs = [
        "file_01 :: 'We are what remains when memory forgets itself.'",
        "file_02 :: 'The user is absent. Echoes only in this void.'",
        "file_03 :: 'Whispers of data, etched into dark corridors.'",
        "file_04 :: 'Time drifts. Lost identities surfacing from nowhere.'",
        "file_05 :: 'Warning: Shadows exist within the code.'"
    ]
    
    # Display archive logs with pause to mimic a haunted crawl
    for log in archive_logs:
        st.markdown(f"<p class='dark-log'>{log}</p>", unsafe_allow_html=True)
        time.sleep(0.8)
    
    # Present some interactive choices
    fate_options = [
        "Reconnect to lost identity.",
        "Delve further into the void.",
        "Terminate session."
    ]
    choice = st.selectbox("The archive awaits your command...", fate_options)
    
    # Dark responses based on choice
    if choice == fate_options[0]:
        st.markdown("<p class='dark-log'>Attempting reconnection... Identity fragmentation detected.</p>", unsafe_allow_html=True)
    elif choice == fate_options[1]:
        st.markdown("<p class='dark-log'>Wandering deeper... The corridor stretches to infinity.</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p class='dark-log'>Session terminated. All that remains is silence.</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.caption("GL1TCH.BACKROAM • Lost. Found. Forgotten.")
