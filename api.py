import yfinance as yf
import pandas as pd

# Fonction pour récupérer les EPS annuels
def get_annual_eps(ticker):
    """
    Récupère les EPS annuels pour une entreprise donnée à partir des données financières.
    """
    try:
        # Télécharger les données financières annuelles
        financials = ticker.financials
        if financials.empty:
            print("[Erreur] Données financières annuelles non disponibles.")
            return None

        # Extraire les données nécessaires
        net_income = financials.loc["Net Income"]  # Bénéfices nets
        shares_outstanding = ticker.info.get('sharesOutstanding')  # Actions en circulation
        if not shares_outstanding:
            print("[Erreur] Nombre d'actions en circulation non disponible.")
            return None

        # Calculer les EPS annuels
        eps_annual = net_income / shares_outstanding
        return eps_annual
    except KeyError as ke:
        print(f"[Erreur] Clé manquante dans les données financières : {ke}")
        return None
    except Exception as e:
        print(f"[Erreur] Problème inattendu lors de la récupération des EPS annuels : {e}")
        return None

# Fonction pour récupérer les EPS trimestriels
def get_quarterly_eps(ticker):
    """
    Récupère les EPS trimestriels pour une entreprise donnée à partir des données financières trimestrielles.
    """
    try:
        # Télécharger les données financières trimestrielles
        quarterly_financials = ticker.quarterly_financials
        if quarterly_financials.empty:
            print("[Erreur] Données financières trimestrielles non disponibles.")
            return None

        # Extraire les données nécessaires
        net_income = quarterly_financials.loc["Net Income"]  # Bénéfices nets trimestriels
        shares_outstanding = ticker.info.get('sharesOutstanding')  # Actions en circulation
        if not shares_outstanding:
            print("[Erreur] Nombre d'actions en circulation non disponible.")
            return None

        # Calculer les EPS trimestriels
        eps_quarterly = net_income / shares_outstanding
        return eps_quarterly
    except KeyError as ke:
        print(f"[Erreur] Clé manquante dans les données financières trimestrielles : {ke}")
        return None
    except Exception as e:
        print(f"[Erreur] Problème inattendu lors de la récupération des EPS trimestriels : {e}")
        return None

# Symbole du ticker de l'entreprise (par exemple, AAPL pour Apple)
ticker_symbol = "AAPL"

# Créer un objet Ticker
try:
    ticker = yf.Ticker(ticker_symbol)

    # Récupérer et afficher les EPS annuels
    print("EPS annuels :")
    annual_eps = get_annual_eps(ticker)
    if annual_eps is not None:
        for date, eps in annual_eps.items():
            print(f"Date {date}: EPS = {eps:.2f}")
    else:
        print("[Info] Aucun EPS annuel disponible pour ce ticker.")

    print("\nEPS trimestriels :")
    # Récupérer et afficher les EPS trimestriels
    quarterly_eps = get_quarterly_eps(ticker)
    if quarterly_eps is not None:
        for date, eps in quarterly_eps.items():
            print(f"Date {date}: EPS = {eps:.2f}")
    else:
        print("[Info] Aucun EPS trimestriel disponible pour ce ticker.")

except Exception as e:
    print(f"[Erreur] Problème lors de la création de l'objet Ticker : {e}")
