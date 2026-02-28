import streamlit as st
from ultralytics import YOLO
from PIL import Image
import os

# ─── Page Configuration ───────────────────────────────────────────────────────
st.set_page_config(
    page_title="Parking Occupancy Classifier",
    page_icon="🚗",
    layout="centered",
)

# ─── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
#MainMenu, footer { visibility: hidden; }

.header-title {
    font-size: 2rem;
    font-weight: 800;
    text-align: center;
    color: #1E3A5F;
    margin-bottom: 1.5rem;
}
.result-card {
    padding: 2rem;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    margin-top: 1rem;
}
.result-card.empty {
    background: linear-gradient(135deg, #ECFDF5, #D1FAE5);
    border: 2px solid #10B981;
}
.result-card.occupied {
    background: linear-gradient(135deg, #FEF2F2, #FEE2E2);
    border: 2px solid #EF4444;
}
.result-label {
    font-size: 1.6rem;
    font-weight: 700;
    margin-bottom: 0.4rem;
}
.result-label.empty    { color: #065F46; }
.result-label.occupied { color: #991B1B; }
.confidence-value {
    font-size: 3.2rem;
    font-weight: 900;
    letter-spacing: -1px;
}
.confidence-value.empty    { color: #059669; }
.confidence-value.occupied { color: #DC2626; }
.confidence-sub {
    font-size: 0.82rem;
    color: #6B7280;
    margin-top: 0.2rem;
}
</style>
""", unsafe_allow_html=True)

# ─── Model Loading ────────────────────────────────────────────────────────────
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model", "best.pt")


@st.cache_resource(show_spinner="Loading model...")
def load_model(path: str) -> YOLO:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model not found at: {path}")
    return YOLO(path)


# ─── Header ───────────────────────────────────────────────────────────────────
st.markdown('<div class="header-title">🚗 Parking Occupancy Classifier</div>', unsafe_allow_html=True)

# ─── Load Model ───────────────────────────────────────────────────────────────
try:
    model = load_model(MODEL_PATH)
except FileNotFoundError as e:
    st.error(f"⚠️ {e}")
    st.stop()

# ─── File Upload ──────────────────────────────────────────────────────────────
uploaded_file = st.file_uploader(
    "Upload a parking slot image",
    type=["jpg", "jpeg", "png", "bmp", "webp"],
)

if uploaded_file is None:
    st.stop()

# ─── Image Preview ────────────────────────────────────────────────────────────
try:
    image = Image.open(uploaded_file).convert("RGB")
except Exception:
    st.error("❌ Could not read the image. Please upload a valid file.")
    st.stop()

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(image, use_container_width=True)

# ─── Prediction ───────────────────────────────────────────────────────────────
with st.spinner("Classifying..."):
    try:
        results        = model(image)
        probs          = results[0].probs
        predicted_class: str   = results[0].names[probs.top1]
        confidence: float      = float(probs.top1conf)
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")
        st.stop()

# ─── Result Card ──────────────────────────────────────────────────────────────
if predicted_class == "space-occupied":
    card_cls = "occupied"
    label    = "🚗 SPACE OCCUPIED"
else:
    card_cls = "empty"
    label    = "🅿 SPACE EMPTY"

conf_pct = confidence * 100

st.markdown(f"""
<div class="result-card {card_cls}">
    <div class="result-label {card_cls}">{label}</div>
    <div class="confidence-value {card_cls}">{conf_pct:.2f}%</div>
    <div class="confidence-sub">Confidence</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.progress(confidence, text=f"Confidence: {conf_pct:.2f}%")
