# Fichier: backend.py

def analyser_question(question):
    """
    Simule une IA qui analyse la question, fouille dans les documents SD Worx
    et renvoie une réponse avec un indice de confiance (format JSON/Dictionnaire).
    """
    q = question.lower()

    # SCÉNARIO 1 : Conflit détecté (Teams ou rumeurs)
    if "télétravail" in q and ("conflit" in q or "teams" in q or "160" in q or "180" in q):
        return {
            "scenario_nom": "litigieux",
            "score": 64,
            "reponse": "Le montant officiel 2026 est fixé à 154,74 €/mois. Attention, une discussion Teams informelle suggère d'arrondir à 160 € ou 180 €. N'appliquez aucun arrondi non légal auprès du client.",
            "statut_couleur": "warning",  # orange
            "sources": [
                "✅ data/teletravail_2026.md (154,74 € - Officiel)",
                "❌ data/teams_chat_informel.md (160 € / 180 € - Non validé)",
                "❌ data/teletravail_2022.md (129,48 € - Obsolète)"
            ],
            "signaux": [
                "🟢 Juridiction : Droit social belge.",
                "🟠 Alerte Conflit : Contradiction avec un message Teams non validé.",
                "🟠 Obsolescence : L'IA a ignoré l'ancienne grille de 2022."
            ],
            "expert": "Sarah Martin (Lead Payroll Specialist)"
        }

    # SCÉNARIO 2 : Confiance Faible / Hors scope (France)
    elif "france" in q or "urssaf" in q:
        return {
            "scenario_nom": "incertain",
            "score": 25,
            "reponse": "Les éléments trouvés (plafond à 58,05 €/mois) concernent exclusivement la filiale française. Ils ne s'appliquent pas au contrat belge de votre client.",
            "statut_couleur": "error",  # rouge
            "sources": [
                "❓ data/teletravail_france.md (Actif uniquement France)"
            ],
            "signaux": [
                "🔴 Juridiction inadéquate : Document source français.",
                "🔴 Donnée manquante : Précisez 'Belgique' pour obtenir le plafond ONSS."
            ],
            "expert": "Équipe RH France"
        }

    # SCÉNARIO 3 : Cas Nominal par défaut (Confiance Élevée)
    else:
        return {
            "scenario_nom": "nominal",
            "score": 92,
            "reponse": "L'indemnité forfaitaire nette pour frais de télétravail en Belgique est fixée à 154,74 € par mois pour un temps plein. Condition obligatoire : le télétravail doit être encadré par un avenant au contrat.",
            "statut_couleur": "success",  # vert
            "sources": [
                "✅ data/teletravail_2026.md (Validé et Actif)"
            ],
            "signaux": [
                "🟢 Fraîcheur : Règle mise à jour pour 2026.",
                "🟢 Validation : Approuvé par Sarah Martin (Legal Expert)."
            ],
            "expert": "Sarah Martin (Lead Payroll Specialist)"
        }
