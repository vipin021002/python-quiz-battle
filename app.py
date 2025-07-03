import streamlit as st
from passlib.hash import bcrypt
from sqlalchemy.orm import Session
from db import User, Score, get_db
from questions import (
    easy_questions, intermediate_questions, expert_questions,
    code_combat_easy, code_combat_intermediate, code_combat_expert
)
from hindi.questions_hindi import (
    easy_questions_hindi, intermediate_questions_hindi, expert_questions_hindi,
    rapid_fire_easy_hindi, rapid_fire_intermediate_hindi, rapid_fire_expert_hindi,
    code_combat_easy_hindi, code_combat_intermediate_hindi, code_combat_expert_hindi
)
import random
import time
from streamlit_autorefresh import st_autorefresh
import pandas as pd

st.set_page_config(page_title="Python Quiz Battle", layout="centered")

# --- Consistent Theme: Inject only once at the top ---
st.markdown(
    '''
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif !important;
        background: linear-gradient(135deg, #18181b 0%, #232946 100%) !important;
    }
    .main {
        background: linear-gradient(135deg, #18181b 0%, #232946 100%) !important;
    }
    .stButton>button {
        background: linear-gradient(90deg, #6366f1 0%, #60a5fa 100%);
        color: #fff;
        border-radius: 12px;
        font-size: 18px;
        font-family: 'Inter', sans-serif !important;
        padding: 0.5em 2em;
        margin: 0.5em 0;
        box-shadow: 0 2px 8px rgba(99,102,241,0.18);
        transition: background 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #4338ca 0%, #2563eb 100%);
        color: #fff;
    }
    .stRadio>div>label {
        font-size: 20px !important;
        color: #fff !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 500 !important;
        margin-bottom: 18px !important;
        margin-top: 8px !important;
        letter-spacing: 0.01em;
    }
    .stRadio>div {
        margin-bottom: 16px !important;
    }
    .stTable, .stMarkdown, .stRadio, .stTextInput, .stSubheader, .stHeader {
        background: #232946;
        color: #fff;
        border-radius: 16px;
        box-shadow: 0 2px 16px rgba(99,102,241,0.18);
        padding: 1.5em;
        margin-bottom: 1.5em;
        font-family: 'Inter', sans-serif !important;
    }
    h1, h2, h3, h4, h5, h6, div, p, span, label {
        color: #fff !important;
        font-family: 'Inter', sans-serif !important;
    }
    .icon {
        display: inline-block;
        vertical-align: middle;
        margin-right: 0.5em;
    }
    </style>
    ''',
    unsafe_allow_html=True
)

# --- Language Selector and Dictionary ---
if 'language' not in st.session_state:
    st.session_state.language = 'English'
language_options = {'English': 'English', 'Hindi': 'हिन्दी'}
prev_language = st.session_state.get('language')
selected_language = st.sidebar.selectbox('Language / भाषा चुनें', list(language_options.keys()), format_func=lambda x: language_options[x], key='lang_select')
if prev_language != selected_language:
    st.session_state.language = selected_language
    st.session_state.quiz = None
    st.session_state.question_idx = 0

LANG = {
    'English': {
        'login_title': "🐍⚔️ Python Quiz Battle",
        'login_welcome': "Welcome! Please log in or create a new account to get started.",
        'username': "Username",
        'password': "Password",
        'login': "Log In",
        'register': "Register",
        'menu_welcome': "Welcome, {username}!",
        'select_mode': "Select Quiz Mode:",
        'select_level': "Select Quiz Level:",
        'choose_player_mode': "Choose Player Mode:",
        'solo': "Solo",
        'multiplayer': "Multiplayer Battle",
        'player1': "Enter Player 1 Name:",
        'player2': "Enter Player 2 Name:",
        'start_battle': "Start Battle",
        'start_solo': "Start Solo Quiz",
        'leaderboard': "Leaderboard",
        'logout': "Log Out",
        'question': "Question {num} of {total}",
        'select_answer': "Select your answer:",
        'submit': "Submit Answer",
        'time_left': "Time left: {sec} seconds",
        'result_title': "Quiz Complete!",
        'your_score': "Your Score: {score} / {total}",
        'back_menu': "Back to Menu",
        'view_leaderboard': "View Leaderboard",
        'better_luck': "Better luck next time!",
        'average': "Average! Keep practicing!",
        'congrats': "Congratulations! You are a Python Pro!",
        'keep_going': "Keep going! Every attempt makes you a better Pythonista.",
        'believe': "Believe in yourself and keep learning!",
        'battle_complete': "Battle Complete!",
        'winner': "{winner} Wins!",
        'tie': "It's a Tie!",
        'score': "Score",
        'invalid_login': "Invalid username or password.",
        'username_exists': "Username already exists. Please choose another.",
        'account_created': "Account created! You are now logged in.",
        'enter_both_names': "Please enter both player names.",
        'select_mode_level': "Select a mode and level to begin your Python quiz journey. Compete solo or challenge friends in battle mode!",
        '50_50': '🧩 50-50',
        'time_freeze': '🕒 Time Freeze',
        'use_50_50': 'Use this lifeline to remove 2 wrong answers.',
        'use_time_freeze': 'Use this lifeline to freeze the timer.',
        'remove_2_wrong': 'Remove 2 wrong answers, can be used once.',
        'freeze_10s': 'Freeze timer for 10 seconds, can be used once.',
        'timestamp': 'Timestamp',
        'tip': 'Tip',
        'feedback_bug_report': 'Feedback / Bug Report',
        'forgot_password': 'Forgot Password?',
        'choose_avatar': 'Choose your avatar/emoji:',
        'feedback_thanks': 'Thank you for your feedback! Please email us at vipin.ks395@gmail.com or describe your issue here.',
        'forgot_password_instructions': "Enter your username or email to reset your password.",
        'reset_user_label': "Username or Email",
        'reset_password_button': "Reset Password",
        'reset_success_message': "If this user exists, a password reset link has been sent!",
        'back_to_login_button': "Back to Login"
    },
    'Hindi': {
        'login_title': "🐍⚔️ पाइथन क्विज़ बैटल",
        'login_welcome': "स्वागत है! शुरू करने के लिए लॉगिन करें या नया खाता बनाएं।",
        'username': "यूज़रनेम",
        'password': "पासवर्ड",
        'login': "लॉग इन करें",
        'register': "रजिस्टर करें",
        'menu_welcome': "स्वागत है, {username}!",
        'select_mode': "क्विज़ मोड चुनें:",
        'select_level': "क्विज़ स्तर चुनें:",
        'choose_player_mode': "प्लेयर मोड चुनें:",
        'solo': "एकल",
        'multiplayer': "मल्टीप्लेयर बैटल",
        'player1': "प्लेयर 1 का नाम दर्ज करें:",
        'player2': "प्लेयर 2 का नाम दर्ज करें:",
        'start_battle': "बैटल शुरू करें",
        'start_solo': "एकल क्विज़ शुरू करें",
        'leaderboard': "लीडरबोर्ड",
        'logout': "लॉग आउट",
        'question': "प्रश्न {num} / {total}",
        'select_answer': "अपना उत्तर चुनें:",
        'submit': "उत्तर सबमिट करें",
        'time_left': "समय शेष: {sec} सेकंड",
        'result_title': "क्विज़ समाप्त!",
        'your_score': "आपका स्कोर: {score} / {total}",
        'back_menu': "मेनू पर वापस जाएँ",
        'view_leaderboard': "लीडरबोर्ड देखें",
        'better_luck': "अगली बार और अच्छा करें!",
        'average': "औसत! अभ्यास जारी रखें!",
        'congrats': "बधाई हो! आप पाइथन प्रो हैं!",
        'keep_going': "जारी रखें! हर प्रयास आपको बेहतर बनाता है।",
        'believe': "खुद पर विश्वास रखें और सीखते रहें!",
        'battle_complete': "बैटल समाप्त!",
        'winner': "{winner} विजेता है!",
        'tie': "टाई!",
        'score': "स्कोर",
        'invalid_login': "अमान्य यूज़रनेम या पासवर्ड।",
        'username_exists': "यूज़रनेम पहले से मौजूद है। कृपया दूसरा चुनें।",
        'account_created': "खाता बन गया! आप लॉग इन हो गए हैं।",
        'enter_both_names': "कृपया दोनों प्लेयर के नाम दर्ज करें।",
        'select_mode_level': "मोड और स्तर चुनें और अपनी पाइथन यात्रा शुरू करें! एकल खेलें या दोस्तों को चुनौती दें!",
        '50_50': '🧩 50-50',
        'time_freeze': '🕒 टाइम फ्रीज़',
        'use_50_50': 'इस लाइफलाइन से 2 गलत उत्तर हटाएँ।',
        'use_time_freeze': 'इस लाइफलाइन से टाइमर रोकें।',
        'remove_2_wrong': '2 गलत उत्तर हटाएँ, एक बार उपयोग करें।',
        'freeze_10s': 'टाइमर 10 सेकंड के लिए रोकें, एक बार उपयोग करें।',
        'timestamp': 'समय',
        'tip': 'सुझाव',
        'feedback_bug_report': 'प्रतिक्रिया / बग रिपोर्ट',
        'forgot_password': 'पासवर्ड भूल गए?',
        'choose_avatar': 'अपना अवतार/इमोजी चुनें:',
        'feedback_thanks': 'आपकी प्रतिक्रिया के लिए धन्यवाद! कृपया हमें vipin.ks395@gmail.com पर ईमेल करें या अपनी समस्या का यहाँ वर्णन करें।',
        'forgot_password_instructions': "अपना पासवर्ड रीसेट करने के लिए अपना यूज़रनेम या ईमेल दर्ज करें।",
        'reset_user_label': "यूज़रनेम या ईमेल",
        'reset_password_button': "पासवर्ड रीसेट करें",
        'reset_success_message': "यदि यह यूज़र मौजूद है, तो एक पासवर्ड रीसेट लिंक भेजा गया है!",
        'back_to_login_button': "लॉगिन पर वापस जाएं"
    }
}

# Helper to get text in selected language
def T(key, **kwargs):
    lang = st.session_state.language
    text = LANG[lang].get(key)
    if text is None:
        text = LANG['English'].get(key, key)
    if isinstance(text, str) and kwargs:
        return text.format(**kwargs)
    return text if text is not None else key

# --- Helper Functions ---
def get_user(username, db):
    return db.query(User).filter(User.username == username).first()

def register_user(username, password, db):
    hashed = bcrypt.hash(password)
    user = User(username=username, password=hashed)
    db.add(user)
    db.commit()
    return user

def check_password(user, password):
    return bcrypt.verify(password, user.password)

def save_score(user_id, score, db):
    s = Score(user_id=user_id, score=score)
    db.add(s)
    db.commit()

def get_leaderboard(db):
    return db.query(User.username, Score.score, Score.timestamp).join(Score).order_by(Score.score.desc(), Score.timestamp).limit(10).all()

# --- Celebration Animation ---
def improved_celebration(score, max_score):
    import streamlit as st
    import time
    st.snow()
    score_placeholder = st.empty()
    for i in range(0, score + 1):
        score_placeholder.markdown(f"""
        <div style='text-align:center; font-size:2.5em; color:#6366f1; font-weight:700; margin-bottom:0.2em; opacity:0.92;'>
            {i} <span style='font-size:1.2em; color:#aaa;'>/ {max_score}</span>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.06)
    progress_placeholder = st.empty()
    percent = int((score / max_score) * 100)
    for p in range(0, percent + 1, 2):
        progress_placeholder.progress(p)
        time.sleep(0.008)
    # Improved, attractive message styling
    if score <= 3:
        msg = "Better luck next time."
        color = "#f87171"
        icon = "😢"
    elif 4 <= score <= 6:
        msg = "Average. Practice more."
        color = "#fbbf24"
        icon = "💡"
    else:
        msg = "Excellent! You are a Python Pro."
        color = "#10b981"
        icon = "🏆"
    st.markdown(f"""
    <div style='display:flex; justify-content:center; align-items:center; margin-top:1.2em; margin-bottom:1.2em;'>
      <div style='background:{color}22; color:{color}; border-radius:18px; padding:1.1em 2.2em; font-size:1.6em; font-weight:700; box-shadow:0 2px 16px rgba(99,102,241,0.10); text-align:center; letter-spacing:0.01em;'>
        <span style='font-size:1.3em; margin-right:0.4em;'>{icon}</span> {msg}
      </div>
    </div>
    """, unsafe_allow_html=True)
    time.sleep(0.5)
    progress_placeholder.empty()

# --- Session State ---
if 'page' not in st.session_state:
    st.session_state.page = 'login'
if 'user' not in st.session_state:
    st.session_state.user = None
if 'mode' not in st.session_state:
    st.session_state.mode = None
if 'quiz' not in st.session_state:
    st.session_state.quiz = None
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question_idx' not in st.session_state:
    st.session_state.question_idx = 0
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'lifeline_used' not in st.session_state:
    st.session_state.lifeline_used = False
if 'fifty_fifty_used' not in st.session_state:
    st.session_state.fifty_fifty_used = False
if 'time_freeze_used' not in st.session_state:
    st.session_state.time_freeze_used = False
if 'freeze_until' not in st.session_state:
    st.session_state.freeze_until = 0
# Track used questions for each level
if 'used_questions_easy' not in st.session_state:
    st.session_state.used_questions_easy = set()
if 'used_questions_intermediate' not in st.session_state:
    st.session_state.used_questions_intermediate = set()
if 'used_questions_expert' not in st.session_state:
    st.session_state.used_questions_expert = set()

# --- Motivational Quotes / Python Tips ---
MOTIVATIONAL_QUOTES = [
    "Every expert was once a beginner. Keep going!",
    "Code is like humor. When you have to explain it, it's bad.",
    "Practice makes perfect. Try one more quiz!",
    "Debugging is twice as hard as writing the code in the first place.",
    "Tip: Use list comprehensions for concise loops!",
    "Tip: Use enumerate() to get index and value in a loop.",
    "Tip: Use f-strings for easy string formatting in Python 3.6+.",
    "Motivation: The only way to learn to code is to code!",
    "Tip: Use 'with open()' to handle files safely.",
    "Motivation: Small progress is still progress!"
]

# --- Sidebar Features ---
SIDEBAR_TIPS = [
    "Fun Fact: Python was named after 'Monty Python', not the snake!",
    "You can swap two variables in Python with 'a, b = b, a'!",
    "Fun Fact: The Zen of Python can be accessed by 'import this' in Python.",
    "Use '_' as a throwaway variable in loops or unpacking.",
    "Fun Fact: Python supports multiple assignment: a, b, c = 1, 2, 3.",
    "Use 'enumerate()' to get both index and value in a loop.",
    "Fun Fact: Python lists are dynamic arrays.",
    "Use 'set()' to remove duplicates from a list.",
    "Fun Fact: You can chain comparison operators: 1 < x < 10.",
    "Use 'help(object)' to get documentation in Python shell."
]

def sidebar_features():
    # Remove extra top and bottom lines and space for a cleaner sidebar
    user = st.session_state.get('user')
    if user:
        st.sidebar.markdown(f"""
        <div style='text-align:center; margin-bottom:1em; margin-top:0.5em;'>
            <div style='font-size:2.5em;'>{user.get('avatar', '👤')}</div>
            <div style='font-size:1.1em; color:#6366f1; font-weight:600;'>{user.get('username')}</div>
        </div>
        """, unsafe_allow_html=True)
    st.sidebar.markdown(f"""
    <div style='background:#232946; color:#fff; border-radius:12px; padding:1em; margin-bottom:1em; font-size:1em; box-shadow:0 2px 8px rgba(99,102,241,0.10);'>
        💡 <b>{T('tip')}:</b> {random.choice(SIDEBAR_TIPS)}
    </div>
    """, unsafe_allow_html=True)
    if st.sidebar.button(f"🐞 {T('feedback_bug_report')}", key="feedback_btn"):
        st.sidebar.info(T('feedback_thanks'))
    # No extra lines or space at the top or bottom

# Call sidebar_features at the top of the script (after set_page_config)
sidebar_features()

# --- Pages ---
def login_page():
    st.markdown(f"<h1 style='text-align:center; color:#6366f1; font-weight:700;'>{T('login_title')}</h1>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style='text-align:center; font-size:18px; margin-bottom:1em;'>
        <span class='icon'>🔑</span>{T('login_welcome')}
    </div>
    """, unsafe_allow_html=True)
    with st.container():
        username = st.text_input(T('username'), help=T('username'))
        password = st.text_input(T('password'), type="password", help=T('password'))
        # Avatar/emoji picker for registration
        avatar_options = ['😀', '🐍', '🚀', '🦄', '👩‍💻', '👨‍💻', '🧑‍🎓', '🐱', '🐼', '🦉', '🦊', '🐢', '🐧', '🦕', '🦖', '🦁', '🐯', '🐸', '🐵', '🦋']
        avatar = st.selectbox(T('choose_avatar'), avatar_options, key="avatar_picker")
        st.session_state['avatar'] = avatar
        # Forgot password flow
        if 'show_reset' not in st.session_state:
            st.session_state['show_reset'] = False
        if not st.session_state['show_reset']:
            col1, col2 = st.columns(2)
            login_clicked = col1.button(T('login'), use_container_width=True, type="primary", key="login_btn")
            register_clicked = col2.button(T('register'), use_container_width=True, key="register_btn")
            if st.button(T('forgot_password'), key="forgot_btn"):
                st.session_state['show_reset'] = True
            # Only process one action per click
            if login_clicked:
                db = next(get_db())
                user = get_user(username, db)
                if user and check_password(user, password):
                    st.session_state.user = {"id": user.id, "username": user.username, "avatar": st.session_state['avatar']}
                    st.session_state.page = 'menu'
                    st.rerun()
                    return  # Prevent further code from running
            elif register_clicked:
                db = next(get_db())
                if get_user(username, db):
                    st.error(T('username_exists'))
                else:
                    user = register_user(username, password, db)
                    st.session_state.user = {"id": user.id, "username": user.username, "avatar": st.session_state['avatar']}
                    st.session_state.page = 'menu'
                    st.rerun()
                    return  # Prevent further code from running
        else:
            st.info(T('forgot_password_instructions'))
            reset_user = st.text_input(T('reset_user_label'), key="reset_user")
            if st.button(T('reset_password_button'), key="reset_btn"):
                st.success(T('reset_success_message'))
                st.session_state['show_reset'] = False
            if st.button(T('back_to_login_button'), key="back_login_btn"):
                st.session_state['show_reset'] = False

def menu_page():
    st.markdown(f"<h2 style='color:#6366f1; text-align:center; margin-bottom:0.5em; font-weight:600;'>👋 {T('menu_welcome', username=st.session_state.user['username'])}</h2>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style='text-align:center; font-size:17px; margin-bottom:1.5em;'>
        <span class='icon'>🧩</span>{T('select_mode_level')}
    </div>
    """, unsafe_allow_html=True)
    
    # Mode Selection
    mode_options = ['Classic', 'Rapid Fire', 'Code Combat']
    selected_mode = st.selectbox(T('select_mode'), mode_options, key='quiz_mode_selection')
    
    # Level Selection for all modes
    level = st.selectbox(T('select_level'), ['Easy', 'Intermediate', 'Expert'], key='quiz_level')
    
    # Player Mode Selection
    player_mode = st.radio(T('choose_player_mode'), [T('solo'), T('multiplayer')], key='player_mode_selection')
    
    if player_mode == T('multiplayer'):
        p1 = st.text_input(T('player1'), key='player1_name_input')
        p2 = st.text_input(T('player2'), key='player2_name_input')
        if st.button(T('start_battle')):
            if p1.strip() and p2.strip():
                st.session_state['player1_name'] = p1.strip()
                st.session_state['player2_name'] = p2.strip()
                st.session_state.mode = selected_mode
                st.session_state.player_mode = 'battle'
                start_quiz()
            else:
                st.warning(T('enter_both_names'))
    else: # Solo mode
        if st.button(T('start_solo')):
            st.session_state.mode = selected_mode
            st.session_state.player_mode = 'solo'
            start_quiz()
            
    st.button(T('view_leaderboard'), use_container_width=True, help=T('view_leaderboard'), key="leaderboard_btn", on_click=lambda: set_page('leaderboard'))
    st.button(T('logout'), use_container_width=True, help=T('logout'), key="logout_btn", on_click=logout)

    # Mode selection reset logic (in menu_page, after mode selection)
    prev_mode = st.session_state.get('mode')
    if prev_mode != selected_mode:
        st.session_state.quiz = None
        st.session_state.question_idx = 0

def set_mode(mode):
    st.session_state.mode = mode
    start_quiz()

def set_page(page):
    if page in ['menu', 'leaderboard']:
        if 'quiz_level' in st.session_state and 'mode' in st.session_state:
            level = st.session_state['quiz_level']
            mode = st.session_state['mode']
            lang = st.session_state.get('language', 'English')
            if lang == 'Hindi':
                if mode == 'Classic':
                    pool = {'Easy': easy_questions_hindi, 'Intermediate': intermediate_questions_hindi, 'Expert': expert_questions_hindi}[level]
                elif mode == 'Rapid Fire':
                    pool = {'Easy': rapid_fire_easy_hindi, 'Intermediate': rapid_fire_intermediate_hindi, 'Expert': rapid_fire_expert_hindi}[level]
                elif mode == 'Code Combat':
                    pool = {'Easy': code_combat_easy_hindi, 'Intermediate': code_combat_intermediate_hindi, 'Expert': code_combat_expert_hindi}[level]
                else:
                    pool = []
            else:
                if mode == 'Classic':
                    pool = {'Easy': easy_questions, 'Intermediate': intermediate_questions, 'Expert': expert_questions}[level]
                elif mode == 'Rapid Fire':
                    pool = {'Easy': code_combat_easy, 'Intermediate': code_combat_intermediate, 'Expert': code_combat_expert}[level]
                elif mode == 'Code Combat':
                    pool = {'Easy': code_combat_easy, 'Intermediate': code_combat_intermediate, 'Expert': code_combat_expert}[level]
                else:
                    pool = []
            used_set = set()
            all_ids = set(q['question'] for q in pool)
            available = [q for q in pool if q['question'] not in used_set]
            n = min(10, len(available))
            if n < 10:
                used_set.clear()
                available = pool[:]
                n = min(10, len(available))
            selected = random.sample(available, n)
            for q in selected:
                used_set.add(q['question'])
            st.session_state.quiz = selected
            if st.session_state.get('player_mode') == 'battle':
                st.session_state['player1_score'] = 0
                st.session_state['player2_score'] = 0
                st.session_state['player1_answers'] = []
                st.session_state['player2_answers'] = []
    st.session_state.page = page

def logout():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.session_state.page = 'login'

def start_quiz():
    st.session_state.fifty_fifty_used = False
    st.session_state.time_freeze_used = False
    st.session_state.fifty_fifty_question_idx = None
    st.session_state.time_freeze_question_idx = None
    mode = st.session_state.get('mode', 'Classic')
    level = st.session_state.get('quiz_level', 'Easy')
    lang = st.session_state.get('language', 'English')

    if lang == 'Hindi':
        classic_map = {
            'Easy': easy_questions_hindi,
            'Intermediate': intermediate_questions_hindi,
            'Expert': expert_questions_hindi
        }
        rapid_fire_map = {
            'Easy': rapid_fire_easy_hindi,
            'Intermediate': rapid_fire_intermediate_hindi,
            'Expert': rapid_fire_expert_hindi
        }
        code_combat_map = {
            'Easy': code_combat_easy_hindi,
            'Intermediate': code_combat_intermediate_hindi,
            'Expert': code_combat_expert_hindi
        }
    else:
        classic_map = {
            'Easy': easy_questions,
            'Intermediate': intermediate_questions,
            'Expert': expert_questions
        }
        rapid_fire_map = {
            'Easy': code_combat_easy,
            'Intermediate': code_combat_intermediate,
            'Expert': code_combat_expert
        }
        code_combat_map = {
            'Easy': code_combat_easy,
            'Intermediate': code_combat_intermediate,
            'Expert': code_combat_expert
        }
    question_map = {
        'Classic': classic_map,
        'Rapid Fire': rapid_fire_map,
        'Code Combat': code_combat_map
    }
    questions = question_map[mode][level]
    
    # In Rapid Fire, we take a random sample of 10 questions
    if mode == 'Rapid Fire':
        selected = random.sample(questions, min(10, len(questions)))
    else:
        # For Classic and Code Combat, we can implement used question tracking
        used_set_name = f"used_{mode.lower().replace(' ', '_')}_{level.lower()}"
        if used_set_name not in st.session_state:
            st.session_state[used_set_name] = set()
            
        used_set = st.session_state[used_set_name]
        available = [q for q in questions if q['question'] not in used_set]
        
        if len(available) < 5: # Changed to 5 to allow more reuse
            used_set.clear()
            available = questions
            
        selected = random.sample(available, min(10, len(available)))
        for q in selected:
            used_set.add(q['question'])

    st.session_state.quiz = selected
    st.session_state.score = 0
    st.session_state.question_idx = 0
    st.session_state.start_time = time.time()
    st.session_state.lifeline_used = False
    st.session_state.fifty_fifty_used = False
    st.session_state.time_freeze_used = False
    st.session_state.freeze_until = 0
    if st.session_state.get('player_mode') == 'battle':
        st.session_state['player1_score'] = 0
        st.session_state['player2_score'] = 0
        st.session_state['player1_answers'] = []
        st.session_state['player2_answers'] = []
    st.session_state.page = 'quiz'

def quiz_page():
    st_autorefresh(interval=1000, key="timerrefresh")
    quiz = st.session_state.quiz
    if quiz is None:
        st.warning("No quiz loaded. Please start a new quiz from the menu.")
        if st.button("Back to Menu"):
            set_page('menu')
        return
    idx = st.session_state.question_idx
    score = st.session_state.score
    total_q = len(quiz)
    mode = st.session_state.get('mode', 'Classic')
    player_mode = st.session_state.get('player_mode', 'solo')
    level = st.session_state.get('quiz_level', 'Easy')
    
    # --- Progress Tracker ---
    progress_html = '<div style="display:flex;justify-content:center;align-items:center;margin-bottom:1.5em;gap:10px;">'
    for i in range(total_q):
        if i < idx:
            color = '#10b981'  # completed (green)
        elif i == idx:
            color = '#6366f1'  # current (purple)
        else:
            color = '#232946'  # not reached (dark)
        progress_html += f'<div style="width:28px;height:28px;border-radius:50%;background:{color};display:flex;align-items:center;justify-content:center;font-weight:bold;font-size:16px;color:#fff;box-shadow:0 2px 8px rgba(99,102,241,0.10);">{i+1}</div>'
        if i < total_q-1:
            progress_html += '<div style="height:4px;width:24px;background:#6366f1;border-radius:2px;"></div>'
    progress_html += '</div>'
    st.markdown(progress_html, unsafe_allow_html=True)

    if idx >= len(quiz):
        db = next(get_db())
        save_score(st.session_state.user['id'], score, db)
        st.session_state.page = 'celebration'  # Go to celebration page first
        st.rerun()
    q = quiz[idx]
    # Multiplayer mode: both players answer
    if mode == 'battle':
        # --- Timer logic for battle mode ---
        if 'battle_start_time' not in st.session_state or st.session_state.get('battle_timer_question') != idx:
            st.session_state['battle_start_time'] = time.time()
            st.session_state['battle_timer_question'] = idx
        elapsed = int(time.time() - st.session_state['battle_start_time'])
        
        # Set timer based on mode
        if st.session_state.get('mode') == 'Rapid Fire':
            timer_duration = 10
        elif st.session_state.get('mode') == 'Code Combat':
            timer_duration = 60
        else: # Classic mode
            timer_duration = 15
            
        st.write(T('time_left', sec=max(0, timer_duration - elapsed)))
        if elapsed >= timer_duration:
            st.warning(T('time_left', sec=0))
            st.session_state['player1_answers'].append(None)
            st.session_state['player2_answers'].append(None)
            st.session_state.question_idx += 1
            st.session_state['battle_start_time'] = time.time()
            st.rerun()
        st.markdown(f"<h3 style='color:#6366f1;text-align:center;'>{T('player1')[:-1]} {st.session_state['player1_name']}</h3>", unsafe_allow_html=True)
        st.markdown(f"<div style='font-size:22px; margin-bottom:18px; text-align:center; color:#fff; background:#232946; border-radius:14px; padding:1em 0; box-shadow:0 2px 8px rgba(99,102,241,0.10); font-weight:500;'>"
                    f"{q['question']}</div>", unsafe_allow_html=True)
        p1_ans = st.radio(T('select_answer'), q['options'], key=f"p1q{idx}")
        st.markdown(f"<h3 style='color:#60a5fa;text-align:center;'>{T('player2')[:-1]} {st.session_state['player2_name']}</h3>", unsafe_allow_html=True)
        st.markdown(f"<div style='font-size:22px; margin-bottom:18px; text-align:center; color:#fff; background:#232946; border-radius:14px; padding:1em 0; box-shadow:0 2px 8px rgba(99,102,241,0.10); font-weight:500;'>"
                    f"{q['question']}</div>", unsafe_allow_html=True)
        p2_ans = st.radio(T('select_answer'), q['options'], key=f"p2q{idx}")
        if st.button(T('submit'), use_container_width=True):
            st.session_state['player1_answers'].append(p1_ans)
            st.session_state['player2_answers'].append(p2_ans)
            if p1_ans == q['answer']:
                st.session_state['player1_score'] += 1
            if p2_ans == q['answer']:
                st.session_state['player2_score'] += 1
            st.session_state.question_idx += 1
            st.session_state['battle_start_time'] = time.time()
            st.rerun()
        st.write(f"{st.session_state['player1_name']} {T('score')}: {st.session_state['player1_score']} | {st.session_state['player2_name']} {T('score')}: {st.session_state['player2_score']}")
        return
    # --- Solo mode logic below (unchanged) ---
    if f"shuffled_options_{idx}" not in st.session_state:
        st.session_state[f"shuffled_options_{idx}"] = q['options'][:]
        random.shuffle(st.session_state[f"shuffled_options_{idx}"])
    st.markdown(f"<h2 style='color:#6366f1; text-align:center; margin-bottom:0.5em; font-weight:600;'><span class='icon'>❓</span>{T('question', num=idx+1, total=len(quiz))}</h2>", unsafe_allow_html=True)
    question_color = '#fff'
    st.markdown(f"<div style='font-size:22px; margin-bottom:18px; text-align:center; color:{question_color}; background:#232946; border-radius:14px; padding:1em 0; box-shadow:0 2px 8px rgba(99,102,241,0.10); font-weight:500;'>"
                f"{q['question']}</div>", unsafe_allow_html=True)

    # --- Lifelines ---
    if level == 'Expert':
        lifeline_cols = []
        if not st.session_state.get('fifty_fifty_used', False):
            lifeline_cols.append('fifty')
        if not st.session_state.get('time_freeze_used', False):
            lifeline_cols.append('freeze')
        if lifeline_cols:
            cols = st.columns(len(lifeline_cols))
            col_idx = 0
            if 'fifty' in lifeline_cols:
                with cols[col_idx]:
                    if st.button(T('50_50'), key=f'fifty_{idx}', help=T('remove_2_wrong')):
                        st.session_state.fifty_fifty_used = True
                        st.session_state.fifty_fifty_question_idx = idx
                        st.rerun()
                col_idx += 1
            if 'freeze' in lifeline_cols:
                with cols[col_idx]:
                    if st.button(T('time_freeze'), key=f'freeze_{idx}', help=T('freeze_10s')):
                        st.session_state.time_freeze_used = True
                        st.session_state.time_freeze_question_idx = idx
                        st.session_state.freeze_until = int(time.time()) + 10
                        st.rerun()
    else:  # Easy and Intermediate levels
        if not st.session_state.lifeline_used:
            col1, col2 = st.columns(2)
            with col1:
                if st.button(T('50_50'), key=f'fifty_{idx}', help=T('use_50_50')):
                    st.session_state.lifeline_used = True
                    st.session_state.fifty_fifty_used = True
                    st.session_state.lifeline_question = idx
                    st.rerun()
            with col2:
                if st.button(T('time_freeze'), key=f'freeze_{idx}', help=T('use_time_freeze')):
                    st.session_state.lifeline_used = True
                    st.session_state.time_freeze_used = True
                    st.session_state.freeze_until = int(time.time()) + 10
                    st.session_state.lifeline_question = idx
                    st.rerun()

    # --- 50-50 logic ---
    options = st.session_state[f"shuffled_options_{idx}"][:]
    # The following block ensures the 50-50 options are selected and stored only once per question
    if (level == 'Expert' and st.session_state.get('fifty_fifty_used', False) and st.session_state.get('fifty_fifty_question_idx') == idx) or \
       (level != 'Expert' and st.session_state.fifty_fifty_used and st.session_state.lifeline_question == idx):
        key = f"fifty_fifty_options_{idx}"
        if key not in st.session_state:
            correct = q['answer']
            wrongs = [opt for opt in options if opt != correct]
            if len(wrongs) > 0:
                wrong = random.choice(wrongs)
                two_opts = [correct, wrong]
                random.shuffle(two_opts)  # Shuffle only once
                st.session_state[key] = two_opts
        # Always use the stored options, never change after first set
        if key in st.session_state:
            options = st.session_state[key]

    # --- Timer logic ---
    now = int(time.time())
    if st.session_state.time_freeze_used and st.session_state.lifeline_question == idx and now < st.session_state.freeze_until:
        elapsed = int(st.session_state.freeze_until - st.session_state.start_time - 10)
        st.write(f"🕒 {T('time_freeze')}! {st.session_state.freeze_until - now} sec left")
    else:
        elapsed = int(time.time() - st.session_state.start_time)
        
        # Set timer based on mode
        if st.session_state.get('mode') == 'Rapid Fire':
            timer_duration = 10
        elif st.session_state.get('mode') == 'Code Combat':
            timer_duration = 60
        else: # Classic mode
            timer_duration = 20
            
        st.write(T('time_left', sec=max(0, timer_duration - elapsed)))
        if elapsed >= timer_duration:
            st.warning(T('time_left', sec=0))
            next_question(False)
            st.rerun()

    selected = st.radio(T('select_answer'), options, key=f"q{idx}", help=T('select_answer'))

    col1, col2 = st.columns([2,1])
    with col2:
        if st.button(T('submit'), use_container_width=True):
            correct = selected == q['answer']
            next_question(correct)
            st.rerun()

def next_question(correct):
    if correct:
        st.session_state.score += 1
    st.session_state.question_idx += 1
    st.session_state.start_time = time.time()
    # Remove previous shuffled options to avoid memory leak
    idx = st.session_state.question_idx - 1
    key = f"shuffled_options_{idx}"
    if key in st.session_state:
        del st.session_state[key]

def celebration_page():
    mode = st.session_state.get('mode', 'Classic')
    score = st.session_state.score
    max_score = len(st.session_state.quiz)
    st.markdown(f"<h1 style='text-align:center;'>🎉 {T('result_title')} 🎉</h1>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center; color:#6366f1;'>{T('congrats')}</h2>", unsafe_allow_html=True)
    improved_celebration(score, max_score)
    st.session_state.page = 'result'
    st.rerun()

def result_page():
    if st.session_state.get('quiz') is None:
        st.warning('No quiz data found. Please start a new quiz from the menu.')
        if st.button('Back to Menu'):
            set_page('menu')
        return
    mode = st.session_state.get('mode', 'Classic')
    if mode == 'battle':
        p1 = st.session_state['player1_name']
        p2 = st.session_state['player2_name']
        s1 = st.session_state['player1_score']
        s2 = st.session_state['player2_score']
        winner = None
        if s1 > s2:
            winner = p1
        elif s2 > s1:
            winner = p2
        st.markdown(f"<h1 style='color:#10b981; text-align:center; margin-bottom:0.5em; font-weight:700;'>🎉 {T('battle_complete')} 🎉</h1>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='color:#6366f1; text-align:center; margin-bottom:1em; font-weight:600;'>{p1}: {s1} | {p2}: {s2}</h2>", unsafe_allow_html=True)
        if winner:
            st.markdown(f"<h2 style='color:#10b981; text-align:center;'>🏆 {T('winner', winner=winner)} 🏆</h2>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h2 style='color:#fbbf24; text-align:center;'>🤝 {T('tie')} 🤝</h2>", unsafe_allow_html=True)
        st.button(T('back_menu'), use_container_width=True, on_click=lambda: set_page('menu'))
        return
    
    # --- Solo mode result logic ---
    st.markdown(f"<h1 style='color:#10b981; text-align:center; margin-bottom:0.5em; font-weight:700;'>🎉 {T('result_title')} 🎉</h1>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='color:#6366f1; text-align:center; margin-bottom:1em; font-weight:600;'>{T('your_score', score=st.session_state.score, total=len(st.session_state.quiz))}</h2>", unsafe_allow_html=True)
    
    # --- Improved Animation ---
    improved_celebration(st.session_state.score, len(st.session_state.quiz))
    
    # Motivational message
    st.markdown(f"""
    <div style='text-align:center; font-size:18px; margin-bottom:1.5em; color:#60a5fa; font-weight:600;'>
        <span class='icon'>🚀</span>{T('keep_going')}<br>
        <span style='color:#10b981;'>{T('believe')} 🌟</span>
    </div>
    """, unsafe_allow_html=True)
    st.button(T('back_menu'), use_container_width=True, on_click=lambda: set_page('menu'))

def leaderboard_page():
    st.markdown(f"<h1 style='color:#6366f1; text-align:center; margin-bottom:0.5em; font-weight:700;'>{T('leaderboard')}</h1>", unsafe_allow_html=True)
    db = next(get_db())
    data = get_leaderboard(db)
    df = pd.DataFrame(data)
    df.columns = [str(T('username')), str(T('score')), str(T('timestamp'))]
    st.table(df)
    st.button(T("back_menu"), use_container_width=True, on_click=lambda: set_page('menu'))

# --- Main Routing ---
if st.session_state.page == 'login':
    login_page()
elif st.session_state.page == 'menu':
    menu_page()
elif st.session_state.page == 'quiz':
    quiz_page()
elif st.session_state.page == 'celebration':
    celebration_page()
elif st.session_state.page == 'result':
    result_page()
elif st.session_state.page == 'leaderboard':
    leaderboard_page() 