# Prompt: Can you help me create a simple Flask application in Python that includes one API endpoint? This endpoint should handle GET requests at the URL/multiply, which accepts two query parameters a and b and returns the multiplication of these two parameters as a JSON response. Make sure to include error handling if the parameters are not provided or if they are not convertible to integers

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/multiply", methods=["GET"])
def multiply():
    try:
        # Get query parameters
        a = request.args.get("a")
        b = request.args.get("b")

        # Check if parameters are missing
        if a is None or b is None:
            return jsonify({"error": "Missing query parameters 'a' or 'b'"}), 400

        # Convert parameters to integers
        a = int(a)
        b = int(b)

        # Multiply the values
        result = a * b
        return jsonify({"result": result}), 200

    except ValueError:
        # Handle the case where a or b can't be converted to an integer
        return jsonify({"error": "'a' and 'b' must be integers"}), 400


if __name__ == "__main__":
    app.run(debug=True)
