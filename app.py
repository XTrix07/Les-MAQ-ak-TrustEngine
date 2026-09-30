import streamlit as st
import time
from backend import analyser_question

st.set_page_config(page_title="SD Worx - Trust Engine", layout="wide")

st.title("🛡️ SD Worx — TrustEngine")
st.caption("Internal Knowledge Assistant: Find it. Understand it. Trust it.")
st.divider()

st.write("Ask the AI a question. Try including words like 'Teams' or 'France' to see how the AI reacts.")
query = st.text_input("Your search query:", value="What is the teleworking allowance amount in Belgium?")
bouton_recherche = st.button("Run TrustEngine Analysis")

st.divider()

if bouton_recherche:
    with st.spinner("🔍 AI is cross-referencing documents and calculating the trust score..."):
        time.sleep(1.5)
        
        resultat = analyser_question(query)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Synthesized Answer")
        
        if resultat["statut_couleur"] == "success":
            st.progress(resultat["score"] / 100, text=f"Global Trust Score: {resultat['score']}%")
            st.success(resultat["reponse"])
        elif resultat["statut_couleur"] == "warning":
            st.progress(resultat["score"] / 100, text=f"Global Trust Score: {resultat['score']}%")
            st.warning(resultat["reponse"])
            st.audio("alerte.mp3", format="audio/mp3")
        else:
            st.progress(resultat["score"] / 100, text=f"Global Trust Score: {resultat['score']}%")
            st.error(resultat["reponse"])

        st.markdown("#### 🔍 Trust Signals")
        for signal in resultat["signaux"]:
            st.write(signal)

    with col2:
        st.subheader("📚 Analyzed Sources")
        for source in resultat["sources"]:
            st.write(source)
            
        st.divider()
        
        st.subheader("👤 Lead Expert")
        st.write(f"**{resultat['expert']}**")
        st.button("Send Teams message to expert")
        
st.divider()
with st.expander("👁 View raw documents extracted from SD Worx database ('data' folder)"):
    st.markdown("""
    **📄 data/teletravail_2026.md (Official updated rule)**
    > *Excerpt:* "Starting January 2026, the net flat-rate teleworking allowance in Belgium is increased to €154.74 per month for a full-time employee. Mandatory condition: Teleworking must be framed by an addendum..."
    
    **💬 data/teams_chat_informel.md (Unverified discussion)**
    > *Thomas:* "I applied €154.74 as Sarah's circular says, but honestly, if the client insists a bit, we can round it up to €160 without any issues."
    
    **📄 data/teletravail_2022.md (Obsolete archive)**
    > *Excerpt:* "The net flat-rate allowance for teleworking employees is set at a maximum of €129.48 per month. It covers office expenses, electricity, and internet."
    
    **📄 data/teletravail_france.md (Out of jurisdiction)**
    > *Excerpt:* "In France, the reimbursement of teleworking expenses is made in the form of a flat-rate allowance [...] capped at €58.05 per month."
    """)
