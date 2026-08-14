import streamlit as tf
import google.generativeai as gemini
import os

# Page Config & Pink Clueless Theme
tf.set_page_config(page_title="Dress Me Up - Clueless Wardrobe", page_icon="🛍️", layout="centered")

# Enhanced Glitter Pink Leopard Background & Clear Text CSS
tf.markdown("""
    <style>
    .stApp {
        background-image: url("https://unsplash.com");
        background-color: #FFF0F5;
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .stApp::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: url("https://imgur.com") repeat;
        opacity: 0.15;
        z-index: -1;
    }
    /* Main container for text readability */
    .block-container {
        background-color: rgba(255, 240, 245, 0.85);
        padding: 30px !important;
        border-radius: 20px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
        border: 2px solid #FF69B4;
    }
    h1 { color: #C71585; font-family: 'Courier New', sans-serif; text-align: center; font-weight: bold; text-shadow: 2px 2px #FFF; }
    h3 { color: #C71585; font-family: 'Arial', sans-serif; font-weight: bold; }
    p, span, label, .stWrite { color: #4A0E2E !important; font-weight: bold; }
    .stButton>button { background-color: #FF69B4; color: white !important; border-radius: 20px; border: 2px solid #C71585; font-weight: bold; width: 100%; }
    .stButton>button:hover { background-color: #C71585; color: white !important; box-shadow: 0px 0px 10px #FF69B4; }
    .wardrobe-card { background-color: #FFFFFF; padding: 15px; border-radius: 15px; border: 2px dashed #C71585; margin-bottom: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.05); }
    .stTabs [data-baseweb="tab"] { color: #C71585 !important; font-weight: bold; font-size: 16px; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { border-bottom-color: #C71585 !important; }
    </style>
""", unsafe_allow_html=True)

tf.title("🛍️ DRESS ME UP 🛍️")
tf.markdown("<p style='text-align: center; color: #C71585; font-size: 18px; font-weight: bold;'>Your AI-Powered Clueless Style Wardrobe Assistant</p>", unsafe_allow_html=True)

# AI Connection (Runs on Cloud - Safe for iPad)
api_key = tf.sidebar.text_input("Enter Gemini API Key (Free)", type="password")

# Sidebar - Premium Subscription Business Model
tf.sidebar.markdown("### 👑 Premium Membership")
tf.sidebar.info("Free Limit: 10 Clothes. Upgrade to Premium for unlimited slots!")
if tf.sidebar.button("👑 Upgrade for $2 / month"):
    tf.sidebar.success("Redirecting to secure payment screen... (Stripe)")

# Main Application Tabs
tab1, tab2 = tf.tabs(["👗 My Wardrobe", "✨ AI Outfit Match"])

with tab1:
    tf.subheader("Inside Your Closet")
    
    col1, col2 = tf.columns(2)
    with col1:
        tf.markdown('<div class="wardrobe-card"><span style="color:#C71585;">🌸 <b>Pink Power Blazer</b></span><br><small style="color:#666;">Outerwear - Pink</small></div>', unsafe_allow_html=True)
    with col2:
        tf.markdown('<div class="wardrobe-card"><span style="color:#C71585;">👟 <b>Black Loafers</b></span><br><small style="color:#666;">Shoes - Black</small></div>', unsafe_allow_html=True)
        
    tf.markdown("---")
    tf.subheader("📸 Add New Item")
    uploaded_file = tf.file_uploader("Snap or upload a photo of your cloth", type=["jpg", "png", "jpeg"])
    kiyafet_adi = tf.text_input("Item Name (e.g., Yellow Plaid Skirt)")
    kiyafet_turu = tf.selectbox("Category", ["Tops", "Bottoms", "Outerwear", "Shoes", "Accessories"])
    
    if tf.button("➕ Add to Closet"):
        if kiyafet_adi:
            tf.success(f"'{kiyafet_adi}' successfully added to your wardrobe! (Demo Mode)")
        else:
            tf.error("Please give your item a name!")

with tab2:
    tf.subheader("🤖 Clueless AI Stylist")
    tf.markdown("<p style='color:#4A0E2E;'>What main piece do you want to wear today? Let the AI design the perfect look!</p>", unsafe_allow_html=True)
    
    secilen_parca = tf.selectbox("Select Core Piece", ["Pink Power Blazer", "Black Loafers"])
    durum = tf.selectbox("Where are you going?", ["School / Campus", "Coffee with Friends", "Elegant Dinner", "Party"])
    
    if tf.button("✨ Match My Outfit"):
        if not api_key:
            tf.warning("Note: Enter a free Gemini API key in the sidebar for real-time AI styling. Showing a preview style below:")
            tf.markdown(f"### 🎀 Recommended Look (For {durum}):")
            tf.write(f"Your **{secilen_parca}** pairs beautifully with a Plaid Mini Skirt and a White Crop Top! Total Cher Horowitz vibes!")
            
            # E-Commerce Monetization (Affiliate Marketing)
            tf.markdown("### 🛒 Complete the Look (Sponsored Products)")
            col_ad1, col_ad2 = tf.columns(2)
            with col_ad1:
                tf.markdown('<div style="background-color:white; padding:10px; border-radius:10px; text-align:center; border: 1px solid #FF69B4;"><b style="color:#C71585;">Plaid Skirt (Zara)</b><br><a href="https://amazon.com" target="_blank" style="color:#FF1493; font-weight:bold;">👉 Shop Now ($29.99)</a></div>', unsafe_allow_html=True)
            with col_ad2:
                tf.markdown('<div style="background-color:white; padding:10px; border-radius:10px; text-align:center; border: 1px solid #FF69B4;"><b style="color:#C71585;">White Crop Top (H&M)</b><br><a href="https://amazon.com" target="_blank" style="color:#FF1493; font-weight:bold;">👉 Shop Now ($12.99)</a></div>', unsafe_allow_html=True)
