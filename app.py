import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# ------------------------------------------------------------
# TaxFit 회계 협업 도구 - Streamlit Cloud 배포용 wrapper
# taxfit-landing.html 은 완전히 독립적인 HTML/CSS/JS 앱이며
# 데이터는 브라우저의 localStorage에 저장됩니다.
# 이 app.py는 해당 HTML을 components.html()로 그대로 렌더링합니다.
# ------------------------------------------------------------

st.set_page_config(
    page_title="TaxFit | 회계 협업 도구",
    page_icon="🧾",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# app.py와 같은 폴더에 taxfit-landing.html 파일이 있어야 합니다.
HTML_PATH = Path(__file__).parent / "taxfit-landing.html"


@st.cache_data
def load_html(path: Path) -> str:
    return path.read_text(encoding="utf-8")


if not HTML_PATH.exists():
    st.error(
        "taxfit-landing.html 파일을 찾을 수 없습니다. "
        "app.py와 같은 디렉토리에 taxfit-landing.html이 있는지 확인해주세요."
    )
else:
    html_content = load_html(HTML_PATH)
    # Streamlit 기본 여백 제거 (전체 화면처럼 보이게)
    st.markdown(
        """
        <style>
            .block-container {padding-top: 0rem; padding-bottom: 0rem; padding-left: 0rem; padding-right: 0rem;}
            iframe {min-height: 100vh;}
        </style>
        """,
        unsafe_allow_html=True,
    )
    components.html(html_content, height=1600, scrolling=True)
