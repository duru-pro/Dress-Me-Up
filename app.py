import streamlit as tf
import google.generativeai as gemini

# Page Config & Pink Clueless Theme
tf.set_page_config(page_title="Dress Me Up - Clueless Wardrobe", page_icon="🛍️", layout="centered")

tf.markdown("""
    <style>
    .stApp {
        background-image: url("https://unsplash.com");
        background-color: #FFF0F5;
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .block-container {
        background-color: rgba(255, 240, 245, 0.85);
        padding: 30px !important;
        border-radius: 20px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
        border: 2px solid #FF69B4;
    }
    h1 { color: #C71585; font-family: 'Courier New', sans-serif; text-align: center; font-weight: bold; }
    p, span, label { color: #4A0E2E !important; font-weight: bold; }
    .stButton>button { background-color: #FF69B4; color: white !important; border-radius: 20px; border: 2px solid #C71585; font-weight: bold; }
    .wardrobe-card { background-color: #FFFFFF; padding: 15px; border-radius: 15px; border: 2px dashed #C71585; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# 💾 KALICI TARAYICI HAFIZASI
if "my_closet" not in tf.session_state:
    tf.session_state.my_closet = [
        {"name": "Pink Power Blazer", "cat": "Outerwear"},
        {"name": "Black Loafers", "cat": "Shoes"}
    ]

tf.title("🛍️ DRESS ME UP 🛍️")

# 🔐 GİZLİ KASADAN ŞİFREYİ OKUMA SİSTEMİ
try:
    api_key = tf.secrets["GEMINI_KEY"]
    gemini.configure(api_key=api_key)
except Exception:
    pass

total_clothes = len(tf.session_state.my_closet)
tf.sidebar.markdown(f"### 👑 Premium Membership")
tf.sidebar.info(f"Clothes: {total_clothes} / 10 Free Slots")
if tf.sidebar.button("👑 Upgrade for $2 / month"):
    tf.sidebar.success("Redirecting to secure Stripe checkout...")

tab1, tab2 = tf.tabs(["👗 My Wardrobe", "✨ AI Outfit Match"])

with tab1:
    tf.subheader("Inside Your Closet")
    cols = tf.columns(2)
    for index, item in enumerate(tf.session_state.my_closet):
        with cols[index % 2]:
            tf.markdown(f'<div class="wardrobe-card"><span style="color:#C71585;">🌸 <b>{item["name"]}</b></span><br><small>{item["cat"]}</small></div>', unsafe_allow_html=True)
        
    tf.markdown("---")
    tf.subheader("📸 Add New Item")
    uploaded_file = tf.file_uploader("Snap or upload a photo of your cloth", type=["jpg", "png", "jpeg"])
    kiyafet_adi = tf.text_input("Item Name (e.g., Yellow Plaid Skirt)")
    kiyafet_turu = tf.selectbox("Category", ["Tops", "Bottoms", "Outerwear", "Shoes", "Accessories"])
    
    if tf.button("➕ Add to Closet"):
        if total_clothes >= 10:
            tf.error("❌ Free limit reached! Upgrade to Premium ($2/mo) for unlimited slots.")
        elif kiyafet_adi:
            tf.session_state.my_closet.append({"name": kiyafet_adi, "cat": kiyafet_turu})
            tf.success(f"'{kiyafet_adi}' saved successfully!")
            tf.rerun()

with tab2:
    tf.subheader("🤖 Clueless AI Stylist")
    closet_names = [item["name"] for item in tf.session_state.my_closet]
    secilen_parca = tf.selectbox("Select Core Piece", closet_names)
    durum = tf.selectbox("Where are you going?", ["School", "Coffee", "Dinner", "Party"])
    
    if tf.button("✨ Match My Outfit"):
        try:
            model = gemini.GenerativeModel('gemini-pro')
            prompt = f"Act as Cher Horowitz from Clueless movie. Suggest a trendy outfit match for a {secilen_parca} for a {durum} situation. Keep it short, fabulous, and Y2K style."
            response = model.generate_content(prompt)
            tf.markdown(f"### 🎀 Cher's AI Recommendation:")
            tf.write(response.text)
        except Exception as e:
            tf.error("AI Error: Configuration missing. Please check Secrets.")
