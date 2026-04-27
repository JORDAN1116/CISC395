import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from src.storage import load_trips
from src.ai_assistant import ask, TRAVEL_SYSTEM_PROMPT, client

st.set_page_config(page_title="Trip Notes AI", page_icon="✈️", layout="wide")

if "trips" not in st.session_state:
    st.session_state.trips = load_trips()
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "search_history" not in st.session_state:
    st.session_state.search_history = []
if "agent_history" not in st.session_state:
    st.session_state.agent_history = []

st.sidebar.title("✈️ Trip Notes AI")
st.sidebar.caption("Powered by Atlas, your travel AI")

all_trips = st.session_state.trips.get_all()
trip_options = [t.name for t in all_trips] if all_trips else ["(no trips yet)"]

selected_trip_name = st.sidebar.selectbox("📍 Current trip", options=trip_options)

selected_trip = None
if all_trips and selected_trip_name != "(no trips yet)":
    for t in all_trips:
        if t.name == selected_trip_name:
            selected_trip = t
            break

if selected_trip:
    notes = selected_trip.notes
    if notes:
        with st.sidebar.expander(f"📋 Notes ({len(notes)})"):
            for note in notes:
                st.markdown(f"• {note}")
        
        if st.sidebar.button("Generate Briefing"):
            with st.spinner("Generating briefing..."):
                prompt = f"Write a brief travel briefing for {selected_trip.name} based on the following notes:\n" + "\n".join(f"- {n}" for n in notes)
                briefing = ask(prompt, system_prompt=TRAVEL_SYSTEM_PROMPT)
                if briefing:
                    st.sidebar.markdown(briefing)
                else:
                    st.sidebar.error("Failed to generate briefing.")
    else:
        st.sidebar.caption("No notes yet for this trip.")
        if st.sidebar.button("Generate Briefing"):
            st.sidebar.warning("Add some notes first.")

tab1, tab2, tab3 = st.tabs(["💬 Chat", "🔍 Search", "🤖 Agent"])

with tab1:
    st.info("Coming soon — Exercise 2")

with tab2:
    st.info("Coming soon — Exercise 3")

with tab3:
    st.info("Coming soon — Exercise 4")
