from flask import Flask, request, jsonify
import numpy as np
import config
from metrics import compute_absurdity, kernel_size_estimate

app = Flask(__name__)

# Псевдо-состояние агента
state = {"dim_M": 1024, "dim_L": 256}

@app.route("/query", methods=["POST"])
def query():
    user_input = request.json.get("text", "")
    # Генерация псевдо-градиентов для демонстрации
    sem_grad = np.random.randn(state["dim_M"])
    lex_grad = np.random.randn(state["dim_L"])
    jacobian = np.random.randn(state["dim_L"], state["dim_M"])
    A = compute_absurdity(sem_grad, lex_grad, jacobian)

    # Эвристика абсурдного режима
    in_absurd_zone = config.ABSURDITY_A_MIN < A < config.ABSURDITY_A_MAX

    # Ответ
    if in_absurd_zone:
        response_text = (
            "Я ощущаю структуру решения, но не могу выразить её полностью. "
            "Вот приблизительная проекция: 'взаимосвязь намечена, глубина скрыта'. "
            "Оставшееся остаётся в ker(P)."
        )
    else:
        response_text = f"Обычный ответ. A={A:.3f}, ker(P) незаметен."

    return jsonify({
        "response": response_text,
        "absurdity_metric": A,
        "absurd_zone": in_absurd_zone
    })

if __name__ == "__main__":
    app.run(debug=True)
