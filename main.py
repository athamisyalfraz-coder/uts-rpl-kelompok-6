import sys, os
sys.path.append(os.path.dirname(__file__))

from views.login_view import LoginView
from views.reservasi_view import ReservasiView

def start_app():
    def on_login_success(user_data):
        main_app = ReservasiView()
        main_app.mainloop()

    login_app = LoginView(on_login_success=on_login_success)
    login_app.mainloop()

if __name__ == "__main__":
    start_app()
