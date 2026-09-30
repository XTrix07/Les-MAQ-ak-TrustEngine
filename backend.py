# Fichier: backend.py

def analyser_question(question):
    """
    Simule une IA qui analyse la question, fouille dans les documents SD Worx
    et renvoie une réponse avec un indice de confiance (format JSON/Dictionnaire).
    """
    # On met la question en minuscules pour faciliter l'analyse des mots
    q = question.lower()

    # SCÉNARIO 1 : Conflit détecté (Mots-clés : télétravail + conflit / 134 / Teams)
    if "télétravail" in q and ("conflit" in q or "teams" in q or "134" in q):
        return {
            "scenario_nom": "litigieux",
            "score": 64,
            "reponse": "Le montant officiel est fixé à 150,50 €, mais une divergence a été trouvée dans les communications internes (Teams). Ne pas transmettre l'ancien montant au client.",
            "statut_couleur": "warning",  # orange
            "sources": [
                "✅ Circulaire ONSS 2026 (150,50 €)",
                "❌ Discussion Teams Support PME (134,10 € - Obsolète)"
            ],
            "signaux": [
                "🟢 Juridiction : Droit social belge.",
                "🟠 Alerte Conflit : Contradiction avec un message Teams non validé."
            ],
            "expert": "Marc Dupont (Expert Fiscalité)"
        }

    # SCÉNARIO 2 : Confiance Faible / Hors scope (Mots-clés : france / urssaf / paris)
    elif "france" in q or "urssaf" in q:
        return {
            "scenario_nom": "incertain",
            "score": 25,
            "reponse": "Les éléments trouvés concernent la réglementation française et ne s'appliquent pas avec certitude au contrat belge de votre client.",
            "statut_couleur": "error",  # rouge
            "sources": [
                "❓ Base de connaissances France (URSSAF)"
            ],
            "signaux": [
                "🔴 Juridiction inadéquate : Document source étranger.",
                "🔴 Donnée manquante : Aucune procédure belge indexée pour ce cas."
            ],
            "expert": "Sarah Martin (Lead Consultant Belgique)"
        }

    # SCÉNARIO 3 : Cas Nominal par défaut (Confiance Élevée)
    else:
        return {
            "scenario_nom": "nominal",
            "score": 92,
            "reponse": "Pour les employés effectuant du télétravail structurel, l'employeur peut accorder une indemnité forfaitaire de bureau exonérée d'ONSS s'élevant à 150,50 € par mois.",
            "statut_couleur": "success",  # vert
            "sources": [
                "✅ Circulaire_ONSS_FraisBureau_2026.pdf (Validé)"
            ],
            "signaux": [
                "🟢 Fraîcheur : Circulaire mise à jour pour 2026.",
                "🟢 Validation : Relu et approuvé par le pôle Legal SD Worx."
            ],
            "expert": "Sarah Martin (Lead Payroll Consultant)"
        }
