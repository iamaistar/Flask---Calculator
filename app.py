from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Welcome to My Flask Site!</h1><p>Visit <a href='/calculator'>/calculator</a> to use the calculator.</p>"


@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    result = ""
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operator = request.form["operator"]

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = num1 / num2
            else:
                result = "Invalid operator"

        except Exception as e:
            result = f"Error: {e}"

    return render_template_string("""
    <h1>Simple Calculator</h1>
    <form method="post">
      <input type="text" name="num1" placeholder="Enter first number" required><br><br>
      <input type="text" name="num2" placeholder="Enter second number" required><br><br>
      <select name="operator" required>
        <option value="+">+</option>
        <option value="-">-</option>
        <option value="*">*</option>
        <option value="/">/</option>
      </select><br><br>
      <input type="submit" value="Calculate">
    </form>
    {% if result != "" %}
    <h2>Result: {{ result }}</h2>
    {% endif %}
    """, result=result)


if __name__ == "__main__":
    app.run(debug=True)



