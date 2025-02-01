import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QTextEdit, QComboBox, QLabel
)
from PyQt6.QtGui import QTextCursor
from editor import CodeEditor
from sandbox import validate_solution


class LeetCodeStyleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Coding Competition")
        self.setGeometry(100, 100, 1000, 600)

        # Main Layout (Splitting into two parts like LeetCode UI)
        main_layout = QHBoxLayout()

        # Left Panel - Problem Description
        self.problem_description = QTextEdit()
        self.problem_description.setReadOnly(True)
        self.problem_description.setPlainText(self.get_problem_description())
        main_layout.addWidget(self.problem_description, 2)

        # Right Panel - Code Editor + Controls
        right_panel = QVBoxLayout()

        # Language Selector
        self.language_selector = QComboBox()
        self.language_selector.addItems(["Python", "cpp", "Java"])
        self.language_selector.currentIndexChanged.connect(self.change_language)
        right_panel.addWidget(self.language_selector)

        # Code Editor
        self.editor = CodeEditor()
        self.set_default_code()
        right_panel.addWidget(self.editor)

        # Run & Submit Buttons
        button_layout = QHBoxLayout()
        self.run_button = QPushButton("Run")
        self.submit_button = QPushButton("Submit")
        self.run_button.clicked.connect(self.run_code)
        self.submit_button.clicked.connect(self.submit_code)
        button_layout.addWidget(self.run_button)
        button_layout.addWidget(self.submit_button)
        right_panel.addLayout(button_layout)

        # Output Section
        self.output_label = QLabel("Test Result:")
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        right_panel.addWidget(self.output_label)
        right_panel.addWidget(self.output_area)

        main_layout.addLayout(right_panel, 3)
        self.setLayout(main_layout)

    def get_problem_description(self):
        return """
        3151. Special Array I

        An array is considered special if every pair of its adjacent elements contains 
        two numbers with different parity.

        Example 1:
        Input: nums = [1]
        Output: true

        Example 2:
        Input: nums = [2,1,4]
        Output: true

        Example 3:
        Input: nums = [4,3,1,6]
        Output: false
        """

    def set_default_code(self):
        default_codes = {
            "Python": "def is_special_array(nums):\n    pass",
            "cpp": "#include <iostream>\nusing namespace std;\nbool isSpecialArray(vector<int>& nums) {\n    return false;\n}",
            "Java": "class Solution {\n    public boolean isSpecialArray(int[] nums) {\n        return false;\n    }\n}"}
        self.editor.setText(default_codes[self.language_selector.currentText()])

    def change_language(self):
        self.set_default_code()

    def run_code(self):
        user_code = self.editor.toPlainText()
        language = self.language_selector.currentText().lower()
        result = validate_solution(user_code, language, 1)
        self.output_area.setPlainText(result)

    def submit_code(self):
        self.run_code()


