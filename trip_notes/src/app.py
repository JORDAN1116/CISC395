import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from src.storage import load_trips
from src.ai_assistant import ask, TRAVEL_SYSTEM_PROMPT, client, MODEL, rag_ask
from src.rag import ensure_index

st.set_page_config(page_title="Trip Notes AI", page_icon="✈️", layout="wide")

if "trips" not in st.session_state:
    st.session_state.trips = load_trips()
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "search_history" not in st.session_state:
    st.session_state.search_history = []
if "agent_history" not in st.session_state:
    st.session_state.agent_history = []

ensure_index()

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

MAX_TURNS = 8

with tab1:
    st.subheader("Atlas — Your Travel AI")
    st.caption("Ask me anything about travel.")
    
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    if prompt := st.chat_input("Ask Atlas anything..."):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            with st.spinner("Atlas is thinking..."):
                messages = [{"role": "system", "content": TRAVEL_SYSTEM_PROMPT}]
                
                recent_history = st.session_state.chat_history[-(MAX_TURNS * 2):]
                messages.extend(recent_history)
                
                try:
                    response = client.chat.completions.create(
                        model=MODEL,
                        messages=messages,
                        temperature=0.7,
                        max_tokens=500,
                        timeout=30,
                    )
                    reply = response.choices[0].message.content
                except Exception as e:
                    reply = f"Error: Could not reach Atlas. ({str(e)})"
                    
                st.markdown(reply)
                st.session_state.chat_history.append({"role": "assistant", "content": reply})
                
    st.button("Clear chat", on_click=lambda: st.session_state.update(chat_history=[]))

with tab2:
    st.subheader("Search My Guides")
    st.caption("Answers grounded in your guides/ documents.")
    
    for message in st.session_state.search_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    if prompt := st.chat_input("Search your guides...", key="search_input"):
        st.session_state.search_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            with st.spinner("Searching guides..."):
                reply = rag_ask(prompt)
                
            st.markdown(reply)
            st.session_state.search_history.append({"role": "assistant", "content": reply})
            
    st.button("Clear search", key="clear_search", on_click=lambda: st.session_state.update(search_history=[]))

with tab3:
    st.info("Coming soon — Exercise 4")
