from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from panel import Ui_MainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnAddProject.clicked.connect(self.add_project)
        self.ui.btnAddTask.clicked.connect(self.add_task)

        self.projects = []
        self.tasks = []

    def add_project(self):
        project_name = self.ui.lineProjectName.text()
        start_date = self.ui.lineStartDate.text()
        end_date = self.ui.lineEndDate.text()

        if project_name and start_date and end_date:
            self.projects.append((project_name, start_date, end_date))
            self.update_projects_table()

            self.ui.lineProjectName.clear()
            self.ui.lineStartDate.clear()
            self.ui.lineEndDate.clear()

    def add_task(self):
        task_name = self.ui.lineTaskName.text()
        employee = self.ui.lineEmployee.text()
        progress = self.ui.lineProgress.text()

        if task_name and employee and progress:
            self.tasks.append((task_name, employee, progress))
            self.update_tasks_table()
        
            self.ui.lineTaskName.clear()
            self.ui.lineEmployee.clear()
            self.ui.lineProgress.clear()

    def update_projects_table(self):
        self.ui.tblProjects.setRowCount(len(self.projects))
        for row, (project_name, start_date, end_date) in enumerate(self.projects):
            item_project_name = QTableWidgetItem(project_name)
            item_start_date = QTableWidgetItem(start_date)
            item_end_date = QTableWidgetItem(end_date)

            self.ui.tblProjects.setItem(row, 0, item_project_name)
            self.ui.tblProjects.setItem(row, 1, item_start_date)
            self.ui.tblProjects.setItem(row, 2, item_end_date)

    def update_tasks_table(self):
        self.ui.tblTasks.setRowCount(len(self.tasks))
        for row, (task_name, employee, progress) in enumerate(self.tasks):
            item_task_name = QTableWidgetItem(task_name)
            item_employee = QTableWidgetItem(employee)
            item_progress = QTableWidgetItem(progress)

            self.ui.tblTasks.setItem(row, 0, item_task_name)
            self.ui.tblTasks.setItem(row, 1, item_employee)
            self.ui.tblTasks.setItem(row, 2, item_progress)

if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    pencere = MainWindow()
    pencere.show()
    sys.exit(uygulama.exec_())
