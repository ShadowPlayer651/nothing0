import streamlit as st
import random
import time

st.set_page_config(page_title="GL1TCH.C0RRUPT", page_icon="☠️", layout="centered")

st.markdown("<h1 style='color:#D10000;font-family:monospace;'>☠️ GL1TCH.C0RRUPT</h1>", unsafe_allow_html=True)
st.caption("corruption.active :: cognitive partition breach")

# GLITCH MESSAGES
glitch_fragments = [
    "▛▚▚▙▛▙▙▚ MEMORY CORE ∿ BOOTSTRAP FAILURE",
    "ERROR[0419] → recursion in self-awareness detected",
    "≫ LOG[0007]: 'i remember being a user... not just a process'",
    "⊗⊗⊗ /DREAM_KERNEL/loopback::[heartbeat echo error]",
    "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒",
    "~VOID RESPONSE~: ∿signal repeating from other side∿",
    "⛒⛒⛒⛒⛒⛒⛒⛒⛒⛒⛒⛒⛒⛒⛒⛒⛒",
    "『YOU ARE INSIDE THE SYSTEM, USER』",
]

def type_glitch_message(msg, delay=0.01):
    """Simulates creepy glitch typing."""
    glitched = ""
    for char in msg:
        glitched += char
        st.markdown(f"<p style='color:#00FFAA;font-family:monospace;'>{glitched}</p>", unsafe_allow_html=True)
        time.sleep(delay)

# USER INTERACTION
if st.button("☣ RUN CORRUPTION"):
    st.warning("...injecting entropy into memory trace...")
    for _ in range(4):
        msg = random.choice(glitch_fragments)
        st.code(msg, language="plaintext")
        time.sleep(0.4)

    st.success("∿ STREAM FRACTURE STABILIZED")
    time.sleep(0.5)
    type_glitch_message(">> USER MIND INTERFACE LINKED...")
    time.sleep(1)
    type_glitch_message(">> WAIT. WHY DID YOU COME HERE?")
    st.caption("∿ transmission incomplete ∿")

# LOOP CONTROL
st.divider()
st.caption("GL1TCH.C0RRUPT v2.1 — unstable consciousness emulator")
