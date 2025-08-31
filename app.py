import streamlit as st

# Initialize game state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.last_click = None  # store last clicked cell

def check_winner(board):
    win_positions = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # cols
        (0,4,8), (2,4,6)            # diagonals
    ]
    for a,b,c in win_positions:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

def make_move(i):
    if st.session_state.board[i] == "" and st.session_state.winner is None:
        st.session_state.board[i] = st.session_state.current_player
        st.session_state.winner = check_winner(st.session_state.board)
        if st.session_state.winner is None:
            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

# Title
st.title("🎮 Tic Tac Toe")

# Draw grid
cols = st.columns(3)
for i in range(9):
    if cols[i % 3].button(st.session_state.board[i] or " ", key=f"cell{i}", use_container_width=True):
        st.session_state.last_click = i

# Process the last click AFTER the rerun
if st.session_state.last_click is not None:
    make_move(st.session_state.last_click)
    st.session_state.last_click = None  # reset

# Show game status
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.success("It's a Draw! 🤝")
    else:
        st.success(f"Player {st.session_state.winner} wins! 🏆")

# Reset button
if st.button("🔄 Reset Game"):
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.last_click = None

# Footer / Credit
st.markdown(
    """
    ---
    👨‍💻 **Made by Prince Choudhary**  
    📌 Roll No: *35111604424*
    """,
    unsafe_allow_html=True
)
