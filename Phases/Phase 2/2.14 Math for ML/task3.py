
import numpy as np

# 1. Dataset
X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([3, 5, 7, 9, 11], dtype=float)

# 2. Initialize parameters
w = 0.0
b = 0.0

# 3. Learning settings
learning_rate = 0.01
epochs = 1000
n = len(X)


# Prediction function
def predict(X, w, b):
    return w * X + b


# Mean Squared Error function
def mse(y_actual, y_predicted):
    return np.mean((y_predicted - y_actual) ** 2)


# 4. Training loop
for epoch in range(1, epochs + 1):

    # Calculate predictions using current parameters
    y_predicted = predict(X, w, b)

    # Calculate current loss
    loss = mse(y, y_predicted)

    # Calculate errors
    errors = y_predicted - y

    # Calculate gradients using current parameters
    dw = (2 / n) * np.sum(errors * X)
    db = (2 / n) * np.sum(errors)

    # Update both parameters using the same gradients
    w = w - learning_rate * dw
    b = b - learning_rate * db

    # Display progress every 100 epochs
    if epoch % 100 == 0:
        new_loss = mse(y, predict(X, w, b))

        print(
            f"Epoch {epoch}: "
            f"w = {w:.6f}, "
            f"b = {b:.6f}, "
            f"Loss = {new_loss:.8f}"
        )


# 5. Final results
final_predictions = predict(X, w, b)
final_loss = mse(y, final_predictions)

print("\nFinal Results")
print("Final weight:", w)
print("Final bias:", b)
print("Final MSE:", final_loss)

# 6. Predict for X = 6
new_X = 6.0
prediction = predict(new_X, w, b)

print("Prediction for X = 6:", prediction)
