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

if bouton_recherche:
    with st.spinner("🔍 Analyse des bases documentaires et vérification de la fiabilité..."):
        time.sleep(2) # Simule un temps de chargement de 2 secondes

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

