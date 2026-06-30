# ==========================================================
# Support Ticket Intelligence System
# config.py
# ==========================================================

"""
Business Configuration File

This file contains:
1. Application Details
2. Team Mapping
3. SLA Mapping
4. Colors
5. Icons
6. Sample Tickets
7. Footer
"""

# ==========================================================
# Application Details
# ==========================================================

APP_TITLE = "🎫 Support Ticket Intelligence System"

APP_SUBTITLE = (
    "AI-Powered Support Ticket Classification & Prioritization"
)

COMPANY_NAME = "Future ML Internship Project"

VERSION = "1.0"

# ==========================================================
# Ticket Category -> Assigned Team
# ==========================================================

TEAM_MAPPING = {

    "Technical issue": "🛠️ Technical Support Team",

    "Billing inquiry": "💳 Finance Team",

    "Refund request": "💰 Customer Success Team",

    "Cancellation request": "❌ Retention Team",

    "Product inquiry": "📦 Sales Team"

}

# ==========================================================
# Priority -> SLA
# ==========================================================

SLA_MAPPING = {

    "Critical": "⏱️ Respond within 15 Minutes",

    "High": "⏳ Respond within 1 Hour",

    "Medium": "🕓 Respond within 4 Hours",

    "Low": "📅 Respond within 24 Hours"

}

# ==========================================================
# Priority Colors
# ==========================================================

PRIORITY_COLORS = {

    "Critical": "#E53935",

    "High": "#FB8C00",

    "Medium": "#1E88E5",

    "Low": "#43A047"

}

# ==========================================================
# Category Icons
# ==========================================================

CATEGORY_ICONS = {

    "Technical issue": "🛠️",

    "Billing inquiry": "💳",

    "Refund request": "💰",

    "Cancellation request": "❌",

    "Product inquiry": "📦"

}

# ==========================================================
# Priority Icons
# ==========================================================

PRIORITY_ICONS = {

    "Critical": "🔴",

    "High": "🟠",

    "Medium": "🔵",

    "Low": "🟢"

}

# ==========================================================
# Sample Tickets
# ==========================================================

SAMPLE_TICKETS = [

    {
        "subject": "Payment Failed",
        "product": "Stripe Payment Gateway",
        "description": (
            "Money has been deducted from my account "
            "but the payment failed."
        )
    },

    {
        "subject": "Unable to Login",
        "product": "Customer Portal",
        "description": (
            "I cannot log into my account after "
            "resetting my password."
        )
    },

    {
        "subject": "Refund Request",
        "product": "Premium Subscription",
        "description": (
            "I cancelled my subscription and would "
            "like to receive a refund."
        )
    },

    {
        "subject": "Software Installation Error",
        "product": "Desktop Application",
        "description": (
            "The software installation keeps failing "
            "with an unknown error."
        )
    },

    {
        "subject": "Battery Draining Quickly",
        "product": "Dell XPS Laptop",
        "description": (
            "My laptop battery drains within one hour "
            "even after a full charge."
        )
    }

]

# ==========================================================
# Application Information
# ==========================================================

ABOUT_APP = """
This AI-powered application automatically predicts:

• Ticket Category

• Ticket Priority

It also recommends:

• Assigned Support Team

• Response SLA

The application uses Natural Language Processing (NLP)
and Machine Learning models trained on customer support
ticket data.
"""

# ==========================================================
# Footer
# ==========================================================

FOOTER_TEXT = (
    "Built with ❤️ using Python, Streamlit, Scikit-learn & NLP"
)