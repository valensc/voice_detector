from PyQt6.QtWidgets import QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt, QRectF
from audio_processor import process_audio, export_audio

class VoiceDetectorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Voice Activity Detector")
        self.setGeometry(100, 100, 800, 400)

        layout = QVBoxLayout()

        self.import_button = QPushButton("Import Audio File")
        self.import_button.clicked.connect(self.import_audio)
        layout.addWidget(self.import_button)

        self.export_button = QPushButton("Export Processed Audio")
        self.export_button.clicked.connect(self.export_audio)
        self.export_button.setEnabled(False)
        layout.addWidget(self.export_button)

        self.timeline = Timeline()
        layout.addWidget(self.timeline)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.audio_file = None
        self.voice_segments = None

    def import_audio(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav)")
        if file_name:
            self.audio_file = file_name
            self.voice_segments = process_audio(self.audio_file)
            self.timeline.set_segments(self.voice_segments)
            self.export_button.setEnabled(True)

    def export_audio(self):
        if not self.audio_file or not self.voice_segments:
            return

        output_file, _ = QFileDialog.getSaveFileName(self, "Save Processed Audio", "", "MP3 Files (*.mp3)")
        if output_file:
            export_audio(self.audio_file, self.voice_segments, output_file)

class Timeline(QWidget):
    def __init__(self):
        super().__init__()
        self.segments = []

    def set_segments(self, segments):
        self.segments = segments
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        width = self.width()
        height = self.height()

        # Draw background
        painter.fillRect(0, 0, width, height, QColor(200, 200, 200))

        # Draw voice segments
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor(0, 150, 0))

        for start, end in self.segments:
            x = int(start * width)
            w = int((end - start) * width)
            painter.drawRect(QRectF(x, 0, w, height))