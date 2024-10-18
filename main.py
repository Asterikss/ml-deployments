import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def generate_data():
    num_points_1 = np.random.randint(50, 101)
    num_points_2 = np.random.randint(50, 101)

    # center (0, 0)
    cluster_1 = np.random.normal(loc=(0, 0), scale=1, size=(num_points_1, 2))

    # center (10, 10)
    cluster_2 = np.random.normal(loc=(10, 10), scale=1, size=(num_points_2, 2))

    return cluster_1, cluster_2


def train_model():
    cluster_1, cluster_2 = generate_data()

    data = np.vstack((cluster_1, cluster_2))
    labels = np.hstack((np.zeros(len(cluster_1)), np.ones(len(cluster_2))))

    x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.25)

    model = LogisticRegression()
    model.fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)

    acc_output = f"Model trained with accuracy: {accuracy * 100:.2f}%"
    print(acc_output)
    with open("accuracy.txt", "w") as f:
        f.write(acc_output)


if __name__ == "__main__":
    train_model()
