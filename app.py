import streamlit as st

# Configuration de la page
st.set_page_config(page_title="SD Worx - Trust Engine", layout="wide")

# Titre et introduction
st.title("🛡️ SD Worx — TrustEngine")
st.caption("Assistant de recherche interne : trouver, comprendre et faire confiance aux connaissances.")

# Barre latérale : simulation de différents scénarios pour la démo
st.sidebar.header("Mode Démo (Scénarios)")
scenario = st.sidebar.radio(
    "Choisir un cas d'usage :",
    ["1. Cas Nominal (Confiance Élevée)", "2. Cas Litigieux (Conflit Détecté)", "3. Cas Incertain (Expert Requis)"]
)

# Zone de recherche
query = st.text_input("Posez votre question RH ou Paie :", value="Quel est le montant de l'indemnité forfaitaire de télétravail en Belgique ?")

st.divider()

# Logique d'affichage selon le scénario choisi
if scenario == "1. Cas Nominal (Confiance Élevée)":
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Réponse synthétisée")
        st.success("Indice de confiance global : 92% (Document officiel et récent)")
        st.write("""
        Pour les employés effectuant du télétravail structurel et régulier, 
        l'employeur peut accorder une indemnité forfaitaire de bureau exonérée d'ONSS 
        et d'impôts s'élevant à **150,50 € par mois**.
        """)

        st.markdown("#### 🔍 Signaux de confiance")
        st.write("🟢 **Fraîcheur :** Circulaire mise à jour pour 2026.")
        st.write("🟢 **Juridiction :** Législation belge (ONSS) confirmée.")
        st.write("🟢 **Validation :** Relu et approuvé par le pôle Legal SD Worx.")

    with col2:
        st.subheader("📚 Sources documentaires")
        st.info("📄 **Circulaire_ONSS_FraisBureau_2026.pdf** (Statut : Officiel & Validé)")
        
        st.subheader("👤 Contact Référent")
        st.write("**Sarah Martin**")
        st.caption("Lead Payroll Consultant — Bureau de Bruxelles")
        st.button("Envoyer un message Teams")

elif scenario == "2. Cas Litigieux (Conflit Détecté)":
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Réponse synthétisée")
        st.warning("Indice de confiance modéré : 64% (Contradiction détectée)")
        st.write("""
        Le montant officiel est fixé à **150,50 €**, mais une divergence a été trouvée dans les communications internes.
        """)

        st.markdown("#### 🔍 Signaux de confiance")
        st.write("🟢 **Juridiction :** Droit social belge.")
        st.write("🟠 **Alerte Conflit :** Un canal Teams mentionne l'ancien plafond de 134,10 €.")
        st.write("🟠 **Action requise :** Ne pas transmettre l'ancien montant au client sans validation.")

    with col2:
        st.subheader("📚 Documents en conflit")
        st.error("❌ Discussion Teams (Support PME) : mentionne 134,10 € (Obsolète)")
        st.success("✅ Circulaire ONSS 2026 : confirme 150,50 €")

        st.subheader("👤 Contact Référent")
        st.write("**Marc Dupont** (Expert Fiscalité)")
        st.button("Demander un arbitrage")

else:  # Cas Incertain
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Réponse synthétisée")
        st.error("Indice de confiance faible : 25% (Aucune source certifiée récente)")
        st.write("""
        Les éléments trouvés concernent la réglementation française et ne s'appliquent pas au contrat belge de votre client.
        """)

        st.markdown("#### 🔍 Signaux de confiance")
        st.write("🔴 **Juridiction inadéquate :** Document source = France (URSSAF).")
        st.write("🔴 **Donnée manquante :** Aucune procédure belge indexée pour cette convention collective.")

    with col2:
        st.subheader("👤 Expert à contacter immédiatement")
        st.write("L'IA ne peut pas garantir la réponse. Contactez directement :")
        st.write("**Sarah Martin** (Lead Consultant Belgique)")
        st.button("Prendre rendez-vous (15 min)")
