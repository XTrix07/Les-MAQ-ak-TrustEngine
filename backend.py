# Fichier: backend.py

def analyser_question(question):
    """
    Simulates an AI analyzing the question against SD Worx documents.
    Returns a JSON/Dictionary response with a trust score.
    """
    q = question.lower()

    # SCENARIO 1 : Conflict detected (Teams or rumors)
    if ("telework" in q or "wfh" in q or "allowance" in q) and ("conflict" in q or "teams" in q or "160" in q or "180" in q):
        return {
            "scenario_nom": "litigieux",
            "score": 64,
            "reponse": "The official 2026 teleworking allowance is €154.74/month. Warning: An informal Teams chat suggests rounding up to €160 or €180. Do not apply non-legal amounts to the client.",
            "statut_couleur": "warning",  # orange
            "sources": [
                "✅ data/teletravail_2026.md (€154.74 - Official)",
                "❌ data/teams_chat_informel.md (€160 / €180 - Unverified)",
                "❌ data/teletravail_2022.md (€129.48 - Obsolete)"
            ],
            "signaux": [
                "🟢 Jurisdiction: Belgian Social Law.",
                "🟠 Conflict Alert: Contradiction found with an unverified Teams message.",
                "🟠 Obsolescence: The AI ignored the outdated 2022 framework."
            ],
            "expert": "Sarah Martin (Lead Payroll Specialist)"
        }

    # SCENARIO 2 : Low Trust / Out of scope (France)
    elif "france" in q or "urssaf" in q:
        return {
            "scenario_nom": "incertain",
            "score": 25,
            "reponse": "The findings (cap at €58.05/month) apply exclusively to the French branch. They do not apply to your client's Belgian contract.",
            "statut_couleur": "error",  # rouge
            "sources": [
                "❓ data/teletravail_france.md (Active for France only)"
            ],
            "signaux": [
                "🔴 Invalid Jurisdiction: French source document.",
                "🔴 Missing Data: Specify 'Belgium' to get the ONSS limits."
            ],
            "expert": "HR Team France"
        }

    # SCENARIO 3 : Default Nominal Case (High Trust)
    else:
        return {
            "scenario_nom": "nominal",
            "score": 92,
            "reponse": "The net flat-rate teleworking allowance in Belgium is set at €154.74 per month for a full-time employee. Mandatory condition: teleworking must be formalized in an employment contract addendum.",
            "statut_couleur": "success",  # vert
            "sources": [
                "✅ data/teletravail_2026.md (Validated & Active)"
            ],
            "signaux": [
                "🟢 Freshness: Rule updated for 2026.",
                "🟢 Validation: Approved by Sarah Martin (Legal Expert)."
            ],
            "expert": "Sarah Martin (Lead Payroll Specialist)"
        }
