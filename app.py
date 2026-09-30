import streamlit as st
import time

# 1. On importe TON IA depuis le fichier backend.py
from backend import analyser_question

# Configuration de la page
st.set_page_config(page_title="SD Worx - Trust Engine", layout="wide")

st.title("🛡️ SD Worx — TrustEngine")
st.caption("Assistant de recherche interne : trouver, comprendre et faire confiance aux connaissances.")
st.divider()

# 2. La barre de recherche
st.write("Posez une question à l'IA. Essayez par exemple d'inclure les mots 'Teams' ou 'France' pour voir l'IA réagir.")
query = st.text_input("Votre recherche :", value="Quel est le montant du télétravail en Belgique ?")
bouton_recherche = st.button("Lancer l'analyse TrustEngine")

st.divider()

# 3. Que se passe-t-il quand on clique sur le bouton ?
if bouton_recherche:
    # Effet de chargement stylé
    with st.spinner("🔍 L'IA croise les documents et calcule le score de confiance..."):
        time.sleep(1.5)  # Simule le temps de calcul
        
        # ON APPELLE TON IA ICI !
        resultat = analyser_question(query)

    # 4. Affichage dynamique selon le résultat renvoyé par le JSON
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Réponse synthétisée")
        
        # Affichage de la barre de confiance avec la bonne couleur
        if resultat["statut_couleur"] == "success":
            st.progress(resultat["score"] / 100, text=f"Indice de confiance global : {resultat['score']}%")
            st.success(resultat["reponse"])
        elif resultat["statut_couleur"] == "warning":
            st.progress(resultat["score"] / 100, text=f"Indice de confiance global : {resultat['score']}%")
            st.warning(resultat["reponse"])
        else:
            st.progress(resultat["score"] / 100, text=f"Indice de confiance global : {resultat['score']}%")
            st.error(resultat["reponse"])

        # Affichage des signaux d'explicabilité
        st.markdown("#### 🔍 Signaux de confiance")
        for signal in resultat["signaux"]:
            st.write(signal)

    with col2:
        # Affichage des sources documentaires
        st.subheader("📚 Sources analysées")
        for source in resultat["sources"]:
            st.write(source)
            
        st.divider()
        
        # Affichage du contact humain
        st.subheader("👤 Expert Référent")
        st.write(f"**{resultat['expert']}**")
        st.button("Envoyer un message Teams à l'expert")
        
# --- PREUVES DOCUMENTAIRES (Dossier data) ---
st.divider()
with st.expander("👁 Consulter les documents bruts extraits de la base SD Worx (Dossier 'data')"):
    st.markdown("""
    **📄 data/teletravail_2026.md (Circulaire officielle - Validée)**
    > *Extrait :* "À partir de janvier 2026, l'indemnité forfaitaire nette pour frais de télétravail en Belgique est revalorisée à 154,74 € par mois pour un temps plein. Condition obligatoire : Le télétravail doit être encadré par un avenant..."
    
    **💬 data/teams_chat_informel.md (Discussion non validée)**
    > *Thomas :* "Moi j'ai appliqué 154,74 € comme le dit la circulaire de Sarah, mais bon, entre nous, si le client insiste un peu on peut arrondir à 160 € sans que ça bloque."
    
    **📄 data/teletravail_2022.md (Archive obsolète)**
    > *Extrait :* "L'indemnité forfaitaire nette pour les employés en télétravail est fixée à 129,48 € par mois maximum. Elle couvre les frais de bureau, d'électricité et de connexion internet."
    
    **📄 data/teletravail_france.md (Hors juridiction)**
    > *Extrait :* "En France, le remboursement des frais de télétravail s'effectue sous forme d'allocation forfaitaire [...] plafonnée à 58,05 € par mois."
    """)