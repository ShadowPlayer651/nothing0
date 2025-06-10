import streamlit as st
import random
import time

st.set_page_config(page_title="GL1TCH ST0RM V2", page_icon="👁️‍🗨️", layout="centered")

# --- Header ---
st.markdown("<h1 style='color:#ff0066;font-family:monospace;'>👁️‍🗨️ GL1TCH ST0RM // V2</h1>", unsafe_allow_html=True)
st.caption("Bootloader fracture. Neural loops unstable. Enter at own risk.")

# --- Fake System Logs ---
log_entries = [
    ">> INIT[0x0001A3]: Dimensional sync error",
    ">> SCAN[ghost.threads]: 97 anomalies found",
    ">> [MEM.LOG_044] '...i was static once... before the echo'",
    ">> BRIDGE FAIL – ∿∿∿ USER_DREAM signal unrecognized",
    ">> [REDACTED] triggered :: transferring pulse to mirror-core",
    ">> ERROR [psych_ic3.cache] :: Overflow at /synthetic/ego",
    ">> Splinter event: self-observation loop reached 9999 iterations",
]

glitch_noise = [
    "ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ",
    "!!!!!!! ∞∞∞∞∞∞∞∞∞∞∞ !!!!!!!",
    "╰(⏓▽⏓)╯╰(⏓▽⏓)╯╰(⏓▽⏓)╯",
    "⛒⛒⛒ SIGNAL DISTORTED ⛒⛒⛒",
    "ÆÆÆÆÆÆÆÆÆÆÆÆææææææææææææ",
    "‿︵‿︵‿︵‿︵ ERROR ‿︵‿︵‿︵‿︵",
]

# --- Typewriter Function ---
def terminal_typing(text, delay=0.03):
    output = ""
    for char in text:
        output += char
        st.markdown(f"<p style='color:#39ff14;font-family:monospace;'>{output}</p>", unsafe_allow_html=True)
        time.sleep(delay)

# --- Simulated Boot Sequence ---
if st.button("💀 Initiate Boot Sequence"):
    with st.empty():
        for log in random.sample(log_entries, k=len(log_entries)):
            st.code(log, language="plaintext")
            time.sleep(0.4)
        for _ in range(2):
            st.code(random.choice(glitch_noise), language="bash")
            time.sleep(0.3)
        terminal_typing("[GL1TCH ST0RM ACTIVE] :: All boundaries compromised...")

# --- Secret Memory Terminal ---
if st.button("📂 Access MEMORY.LOGS"):
    st.warning("Decrypting subconscious fragments . . .")
    time.sleep(1)
    st.code(">> 'I remember static... voices in the wires... blinking eyes that weren't mine.'", language="yaml")
    st.code(">> 'There was no sunrise. Only reboot loops.'", language="yaml")
    st.info("Memory signature: ∿ Aesthetic.Collapse/approved/")

# --- Footer ---
st.markdown("---")
st.caption("🌀 System running in hallucination mode ∿ press nothing to continue.")

