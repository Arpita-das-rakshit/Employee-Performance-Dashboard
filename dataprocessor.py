import numpy as np

def normalize(col):
    return (col - col.min()) / (col.max() - col.min() + 1e-9)


def calculate_score(df):
    df['Score'] = (
        normalize(df['TotalTickets']) * 0.2 +
        normalize(df['P1_Critical']) * 0.4 +
        normalize(df['Incidents_Handled']) * 0.25 +
        normalize(df['KT_Sessions']) * 0.3 +
        normalize(df['Appreciations']) * 0.4 -
        normalize(df['Ticket_Breaches']) * 0.9 -
        normalize(df['Escalations']) * 0.8
    )
    return df


def detect_risk(df):
    risks = []

    for _, row in df.iterrows():
        reasons = []

        if row['Ticket_Breaches'] > 1:
            reasons.append("High Breach")

        if row['Escalations'] > 1:
            reasons.append("Frequent Escalation")

        if row['Score'] < 0.4:
            reasons.append("Low Performance")

        if reasons:
            risks.append((row['Name'], reasons))

    return risks