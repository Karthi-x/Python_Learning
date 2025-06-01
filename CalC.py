from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator")
        self.setGeometry(100, 100, 500, 500)

        # Widgets
        self.num1_input = QLineEdit(self)
        self.num2_input = QLineEdit(self)
        self.result_label = QLabel("Result: ", self)
        
        # Buttons
        self.add_btn = QPushButton("Add", self)
        self.sub_btn = QPushButton("Subtract", self)
        self.mul_btn = QPushButton("Multiply", self)
        self.div_btn = QPushButton("Divide", self)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("First Number:"))
        layout.addWidget(self.num1_input)
        layout.addWidget(QLabel("Second Number:"))
        layout.addWidget(self.num2_input)
        layout.addWidget(self.add_btn)
        layout.addWidget(self.sub_btn)
        layout.addWidget(self.mul_btn)
        layout.addWidget(self.div_btn)
        layout.addWidget(self.result_label)

        # Central Widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Button Connections
        self.add_btn.clicked.connect(self.add)
        self.sub_btn.clicked.connect(self.subtract)
        self.mul_btn.clicked.connect(self.multiply)
        self.div_btn.clicked.connect(self.divide)

    def calculate(self, operation):
        try:
            x = float(self.num1_input.text())
            y = float(self.num2_input.text())
            if operation == "add":
                result = x + y
                self.result_label.setText(f"Result: {x} + {y} = {result}")
            elif operation == "subtract":
                result = x - y
                self.result_label.setText(f"Result: {x} - {y} = {result}")
            elif operation == "multiply":
                result = x * y
                self.result_label.setText(f"Result: {x} * {y} = {result}")
            elif operation == "divide":
                if y == 0:
                    self.result_label.setText("Error: Cannot divide by zero!")
                else:
                    result = x / y
                    self.result_label.setText(f"Result: {x} / {y} = {result}")
        except ValueError:
            self.result_label.setText("Error: Enter valid numbers!")

    def add(self):
        self.calculate("add")

    def subtract(self):
        self.calculate("subtract")

    def multiply(self):
        self.calculate("multiply")

    def divide(self):
        self.calculate("divide")

if __name__ == "__main__":
    app = QApplication([])
    window = CalculatorApp()
    window.show()
    app.exec_()
