# ==========================================================
# Support Ticket Intelligence System
# app.py
# ==========================================================

import os
import streamlit as st

from helper import predict_ticket
from config import (
    APP_TITLE,
    APP_SUBTITLE,
    COMPANY_NAME,
    VERSION,
    ABOUT_APP,
    FOOTER_TEXT,
    SAMPLE_TICKETS,
    CATEGORY_ICONS,
    PRIORITY_ICONS
)

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Support Ticket Intelligence System",
    page_icon="🎫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# Load Custom CSS
# ==========================================================

css_path = os.path.join(
    os.path.dirname(__file__),
    "style.css"
)

if os.path.exists(css_path):
    with open(css_path) as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )

# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.title("🎫 SupportIQ")

    st.markdown("---")

    st.subheader("Project")

    st.write(COMPANY_NAME)

    st.write(f"Version : {VERSION}")

    st.markdown("---")

    st.subheader("About")

    st.write(ABOUT_APP)

    st.markdown("---")

    st.subheader("Example Tickets")

    example = st.selectbox(

        "Choose Example",

        [

            "Select Example",

            "Payment Failed",

            "Unable to Login",

            "Refund Request",

            "Software Installation Error",

            "Battery Draining Quickly"

        ]

    )

# ==========================================================
# Sample Ticket Loader
# ==========================================================

sample_subject = ""
sample_product = ""
sample_description = ""

if example != "Select Example":

    for ticket in SAMPLE_TICKETS:

        if ticket["subject"] == example:

            sample_subject = ticket["subject"]

            sample_product = ticket["product"]

            sample_description = ticket["description"]

            break

# ==========================================================
# Header
# ==========================================================

st.markdown(
    f"<h1 class='main-title'>{APP_TITLE}</h1>",
    unsafe_allow_html=True
)

st.markdown(
    f"<p class='sub-title'>{APP_SUBTITLE}</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# ==========================================================
# User Input
# ==========================================================

st.markdown(
    "<h3 class='section-title'>Enter Support Ticket Details</h3>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    ticket_subject = st.text_input(

        "Ticket Subject",

        value=sample_subject,

        placeholder="Example: Payment Failed"

    )

with col2:

    product_name = st.text_input(

        "Product Purchased",

        value=sample_product,

        placeholder="Example: Stripe Payment Gateway"

    )

ticket_description = st.text_area(

    "Ticket Description",

    value=sample_description,

    height=180,

    placeholder="Describe the customer issue..."

)

st.markdown("")

predict = st.button(
    "🚀 Predict Ticket",
    use_container_width=True
)

# ==========================================================
# Prediction
# ==========================================================

if predict:

    if (

        ticket_subject.strip() == ""

        or

        ticket_description.strip() == ""

    ):

        st.warning(
            "Please enter Ticket Subject and Description."
        )

    else:

        with st.spinner(
            "Analyzing support ticket..."
        ):

            result = predict_ticket(

                ticket_subject,

                product_name,

                ticket_description

            )

            ticket_type = result["ticket_type"]

            priority = result["priority"]

            confidence = result["confidence"]

            team = result["team"]

            sla = result["sla"]
            st.success("✅ Ticket analyzed successfully!")

        st.markdown("---")

        st.markdown(
            "<h3 class='section-title'>Prediction Results</h3>",
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)

        # ======================================================
        # Ticket Category
        # ======================================================

        with col1:

            st.markdown(
                f"""
                            <div class="category-card">
                                <h4>🎯 Ticket Category</h4>
                                <h2>{CATEGORY_ICONS.get(ticket_type, "📄")} {ticket_type}</h2>
                            </div>
                            """,
                unsafe_allow_html=True
            )

        # ======================================================
        # Ticket Priority
        # ======================================================

        with col2:

            st.markdown(
                f"""
                            <div class="priority-card">
                                <h4>⚡ Ticket Priority</h4>
                                <h2>{PRIORITY_ICONS.get(priority, "📌")} {priority}</h2>
                            </div>
                            """,
                unsafe_allow_html=True
            )

        st.markdown("")

        col3, col4 = st.columns(2)

        # ======================================================
        # Assigned Team
        # ======================================================

        with col3:

            st.markdown(
                f"""
                            <div class="team-card">
                                <h4>👨‍💻 Assigned Team</h4>
                                <h3>{team}</h3>
                            </div>
                            """,
                unsafe_allow_html=True
            )

        # ======================================================
        # SLA
        # ======================================================

        with col4:

            st.markdown(
                f"""
                            <div class="sla-card">
                                <h4>⏰ Recommended SLA</h4>
                                <h3>{sla}</h3>
                            </div>
                            """,
                unsafe_allow_html=True
            )

        st.markdown("")

        # ======================================================
        # Confidence
        # ======================================================

        if confidence != "N/A":

            st.markdown(
                f"""
                            <div class="confidence-card">
                                <h4>📊 Prediction Confidence</h4>
                                <h2>{confidence}%</h2>
                            </div>
                            """,
                unsafe_allow_html=True
            )

            st.progress(min(float(confidence) / 100, 1.0))

        else:

            st.info(
                "Confidence score is unavailable because the selected model "
                "does not support probability estimation."
            )

        st.markdown("---")

        # ======================================================
        # Summary
        # ======================================================

        st.subheader("📋 Prediction Summary")

        summary = f"""
            ### Support Ticket Summary

            **Subject**

            {ticket_subject}

            **Product**

            {product_name}

            **Description**

            {ticket_description}

            ---

            ### AI Prediction

            - **Ticket Category:** {ticket_type}

            - **Priority:** {priority}

            - **Assigned Team:** {team}

            - **Recommended SLA:** {sla}

            - **Confidence:** {confidence}
            """

        st.markdown(summary)

        st.download_button(

            label="📄 Download Prediction Summary",

            data=summary,

            file_name="ticket_prediction.txt",

            mime="text/plain"

        )

    # ==========================================================
    # Footer
    # ==========================================================

    st.markdown("---")

    st.markdown(

        f"""
                <div class="footer">

                <b>{FOOTER_TEXT}</b>

                <br><br>

                Support Ticket Intelligence System

                <br>

                Developed using Streamlit • Scikit-learn • NLP • Machine Learning

                </div>
                """,

        unsafe_allow_html=True

    )