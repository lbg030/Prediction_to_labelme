import sys
import os
import os.path as osp
import json

from PySide6.QtUiTools import QUiLoader, loadUiType
from PySide6.QtWidgets import *
from PySide6.QtCore import QDir, Qt, QRect, QFile, QUrl
from PySide6.QtGui import QPixmap, QKeySequence, QShortcut, QDesktopServices
from PySide6.QtXml import QDomDocument

from utils import count_images, main_func
from ui.ui_seg import Ui_SemiLabeling

import torch
import torchvision

import time
import datetime

class Seg(QMainWindow):
    def __init__(self):
        super(Seg, self).__init__()
        self.ui = Ui_SemiLabeling()
        self.ui.setupUi(self)
        self.model = QFileSystemModel()
        self.model.setNameFilters(
            ["*.png", "*.jpg", "*.jpeg"]
        )  # Add more extensions if needed
        self.model.setNameFilterDisables(False)  # Hide non-matching files
        self.ui.treeView.setModel(self.model)

        # Connect the 'Open Directory' button to the open_directory function
        self.ui.toolButton_7.clicked.connect(self.open_directory)

        # Connect the selection changed signal to our slot
        self.ui.treeView.selectionModel().selectionChanged.connect(self.display_image)
        self.ui.treeView.setColumnHidden(3, True)

        # self.ui.tableWidget_2.setColumnCount(3)
        # self.ui.tableWidget_2.setHorizontalHeaderLabels(
        #     ["Folder", "Image Count", "Label Count"]
        # )

        # * labelme to Hubble functions
        self.ui.toolButton_5.clicked.connect(self.prediction)

    def open_directory(self):
        # directory = QFileDialog.getExistingDirectory(self, "Select directory")
        directory = QFileDialog.getExistingDirectory(self, "Select directory")
        if directory:  # if a directory is selected
            self.model.setRootPath(directory)
            self.ui.treeView.setRootIndex(self.model.index(directory))

            # Count the images in each subdirectory and show the results in the label
            image_counts = count_images(directory)

            total_images = sum(image_counts.values())
            self.ui.textBrowser.setText(f"Total Images : {total_images}")

            # Create a dictionary of subdirectory names and their indices
            subdirs = sorted(next(os.walk(directory))[1])

            self.class_dict = {subdir: i for i, subdir in enumerate(subdirs)}

            self.counts_by_label = {
                osp.split(subdir)[-1]: value
                for subdir, value in image_counts.items()
                if osp.split(subdir)[-1] in subdirs
            }

            self.counts_by_label = dict(sorted(self.counts_by_label.items()))

            # Fill the table with data
            # for i, (subdir, index) in enumerate(self.class_dict.items()):
            #     self.ui.tableWidget.setRowHeight(i, 10)
            #     label_count = self.counts_by_label[subdir]
            #     self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(subdir))
            #     self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(str(index)))
            #     self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(str(label_count)))

            self.root_directory = directory
            self.bool_open_directory = True

    def display_image(self, selected):
        index = selected.indexes()[0]
        file_path = self.model.filePath(index)

        pixmap = QPixmap(file_path)

        label_size = self.ui.image_label.size()
        pixmap = pixmap.scaled(
            label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )

        self.ui.image_label.setPixmap(pixmap)

    def prediction(self):
        if self.bool_open_directory:
            reply = QMessageBox.question(
                self,
                "Message",
                f"실행하시겠습니까?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.Yes,
            )

            if reply == QMessageBox.Yes:

                main_func(self.root_directory)
                
                QMessageBox.information(
                        self,
                        f"Complete !\n Saved in {self.root_directory}",
                        f"Complete !\n Saved in {self.root_directory}",
                    )

        else:
            QMessageBox.information(
                self, "Select Directory First", "Select Directory First"
            )


if __name__ == "__main__":
    app = QApplication.instance()  # 현재 인스턴스를 가져옵니다.
    if not app:  # 인스턴스가 없는 경우 새로 생성합니다.
        app = QApplication(sys.argv)

    source = Seg()
    source.show()
    sys.exit(app.exec())
