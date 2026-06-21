import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Grade Calculator",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS for beautiful styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .grade-A { color: #28a745; font-size: 2.5rem; font-weight: bold; }
    .grade-B { color: #17a2b8; font-size: 2.5rem; font-weight: bold; }
    .grade-C { color: #ffc107; font-size: 2.5rem; font-weight: bold; }
    .grade-D { color: #fd7e14; font-size: 2.5rem; font-weight: bold; }
    .grade-E { color: #dc3545; font-size: 2.5rem; font-weight: bold; }
    .result-box {
        padding: 20px;
        border-radius: 15px;
        background: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin: 15px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🎓 Student Grade Calculator")
st.markdown("### Find out your grade instantly!")

# Sidebar
with st.sidebar:
    st.header("📋 Grading Scale")
    st.markdown("""
    | Marks     | Grade |
    |-----------|-------|
    | 90 - 100  | **A** |
    | 80 - 89   | **B** |
    | 70 - 79   | **C** |
    | 60 - 69   | **D** |
    | Below 60  | **E** |
    """)

# Main Input
col1, col2 = st.columns([2, 1])

with col1:
    mark = st.number_input(
        "Enter your marks",
        min_value=0,
        max_value=100,
        value=85,
        step=1,
        help="Enter a number between 0 and 100"
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    calculate = st.button("Calculate Grade 🎯", type="primary", use_container_width=True)

# Grade Calculation Logic
def get_grade(marks):
    if marks > 100 or marks < 0:
        return None, "❌ Marks must be between 0 and 100"
    elif marks >= 90:
        return "A", "Excellent! Outstanding performance! 🏆"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👏"
    elif marks >= 70:
        return "C", "Good! You can do better! 👍"
    elif marks >= 60:
        return "D", "Pass! Need to work harder! 📚"
    else:
        return "E", "Needs significant improvement 😔"

# Display Result
if calculate or mark:
    grade, message = get_grade(mark)
    
    st.markdown("---")
    st.subheader("📊 Your Result")
    
    result_col1, result_col2 = st.columns(2)
    
    with result_col1:
        st.metric(label="Your Marks", value=f"{mark}")
    
    with result_col2:
        if grade:
            st.markdown(f"**Grade**")
            st.markdown(f"<div class='grade-{grade}'>{grade}</div>", unsafe_allow_html=True)
        else:
            st.error(grade)  # This will show error message

    # Result Box
    if grade:
        st.markdown(f"""
        <div class="result-box">
            <h3>{message}</h3>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Please enter marks between 0 and 100.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ for vijayarumugam's Community")