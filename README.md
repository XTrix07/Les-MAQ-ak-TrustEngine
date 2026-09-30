# 🛡️ TrustEngine — SD Worx Knowledge Base
> *Unlock the Knowledge Within : Find it. Understand it. Trust it.*

Projet développé par l'équipe **Les MAQ-ak** dans le cadre du **Tectonic Hackathon 2026** pour le défi **SD Worx**.

---

## 📌 Le Problème (SD Worx Challenge)

Dans une grande organisation comme SD Worx (plus de 10 000 collaborateurs répartis dans plusieurs pays), la connaissance interne est fragmentée entre manuels officiels, documents partagés et conversations Teams informelles. 

Trouver un document est facile, mais **savoir s'il est digne de confiance est un véritable défi** :
* Un consultant RH/paie fait face à des informations contradictoires ou obsolètes.
* Une recherche classique ou un résumé d'IA standard fournit souvent des réponses sans explicabilité ni garantie de validité légale locale.
* Le doute ralentit la prise de décision et fait perdre du temps aux équipes.

---

## 💡 Notre Solution : TrustEngine

**TrustEngine** transforme la recherche documentaire interne en un système axé sur la **confiance** et l'**explicabilité** :

1. **Score de confiance transparent (Trust Score)** : Chaque réponse synthétisée est pondérée selon la fraîcheur des données, la juridiction applicable et le niveau d'approbation interne.
2. **Détection active de contradictions** : Mise en évidence des conflits entre documents officiels et discussions non validées (ex. un montant obsolète issu d'un canal Teams).
3. **Mise en relation d'experts ("Human-in-the-loop")** : Si l'incertitude est trop grande, le système oriente immédiatement l'employé vers le bon référent métier au sein de l'entreprise.
4. **Briefing Audio Express** : Synthèse vocale instantanée des points de vigilance légaux pour les consultants en déplacement.

---

## 🛠️ Stack Technique

* **Interface Utilisateur** : Streamlit (Python)
* **Traitement & Logique IA** : Python / GCP (Google Cloud Platform)
* **Synthèse Vocale** : ElevenLabs API
* **Audit & Sécurité du Code** : Aikido Security (Code Security Audit)

---

## 🚀 Installation et Lancement Local

### Prérequis
* Python 3.9+
* Git

### Instructions pas à pas

1. Cloner le dépôt :
git clone https://github.com/XTrix07/Les-MAQ-ak.git
cd Les-MAQ-ak

2. Installer les dépendances nécessaires :
pip install streamlit

3. Lancer l'application :
streamlit run app.py

L'application s'ouvrira automatiquement dans votre navigateur à l'adresse http://localhost:8501.

---

## 🔒 Sécurité & Audit Aikido

Conformément aux exigences du hackathon, l'intégralité du code a été soumise à l'outil d'audit de sécurité **Aikido** :
* Détection et correction des failles d'authentification et de logique métier.
* Ségrégation stricte des données et absence d'API keys ou de secrets dans le code source public.
* *(Captures d'écran de l'audit Aikido avant/après disponibles dans le dossier /docs ou jointes à la soumission Builderbase).*

---

## 👥 Équipe — Les MAQ-ak
Projet réalisé lors du Tectonic Hackathon 2026.
