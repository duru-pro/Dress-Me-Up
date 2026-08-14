import streamlit as tf
import google.generativeai as gemini
import os

# Page Config & Pink Clueless Theme
tf.set_page_config(page_title="Dress Me Up - Clueless Wardrobe", page_icon="🛍️", layout="centered")

# Custom Glitter Pink Leopard Background CSS
tf.markdown("""
    <style>
    .stApp {
        background-image: url("https://unsplash.com"); /* Temporary premium pink base */
        background-color: #FFF0F5;
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    /* Leopard overlay concept with pink glitter vibe */
    .stApp::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: url("https://imgur.com") repeat; /* Custom placeholder for leopard patterns */
        opacity: 0.15;
        z-index: -1;
    }
    h1 { color: #FF1493; font-family: 'Courier New', sans-serif; text-align: center; font-weight: bold; text-shadow: 2px 2px #FFF; }
    h3 { color: #FF1493; font-family: 'Arial', sans-serif; }
    .stButton>button { background-color: #FF69B4; color: white; border-radius: 20px; border: 2px solid #FF1493; font-weight: bold; width: 100%; }
    .stButton>button:hover { background-color: #FF1493; color: white; box-shadow: 0px 0px 10px #FF69B4; }
    .wardrobe-card { background-color: rgba(255, 255, 255, 0.9); padding: 15px; border-radius: 15px; border: 2px dashed #FF69B4; margin-bottom: 10px; }
    .stTabs [data-baseweb="tab"] { color: #FF69B4; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

tf.title("🛍️ DRESS ME UP 🛍️")
tf.markdown("<p style='text-align: center; color: #FF1493; font-weight: bold; background: rgba(255,255,255,0.7); padding: 5px; border-radius: 10px;'>Your AI-Powered Clueless Style Wardrobe Assistant</p>", unsafe_allow_html=True)

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
        tf.markdown('<div class="wardrobe-card">🌸 <b>Pink Power Blazer</b><br><small>Outerwear - Pink</small></div>', unsafe_allow_html=True)
    with col2:
        tf.markdown('<div class="wardrobe-card">👟 <b>Black Loafers</b><br><small>Shoes - Black</small></div>', unsafe_allow_html=True)
        
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
    tf.write("What main piece do you want to wear today? Let the AI design the perfect look!")
    
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
                tf.markdown('<div style="background-color:white; padding:10px; border-radius:10px; text-align:center;"><b>Plaid Skirt (Zara)</b><br><a href="https://amazon.com" target="_blank">👉 Shop Now ($29.99)</a></div>', unsafe_allow_html=True)
            with col_ad2:
                tf.markdown('<div style="background-color:white; padding:10px; border-radius:10px; text-align:center;"><b>White Crop Top (H&M)</b><br><a href="https://amazon.com" target="_blank">👉 Shop Now ($12.99)</a></div>', unsafe_allow_html=True)
