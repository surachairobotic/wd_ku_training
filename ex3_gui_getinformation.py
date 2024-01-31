from PyQt5 import QtCore, QtGui, QtWidgets
import requests, threading, time, json

def sendJson(num, ip_port):
    # Get Request
    host = 'http://'+ip_port+'/btn_call/'
    #host = '0.0.0.0:8000/btn_call/'
    # host = 'http://192.168.12.253:8000/btn_call/'

    r = requests.post(host, json={"call_id": num})
    print('Status code : ', r.status_code)
    print(r.json())

def pWidgets(wdgt, func=None, font=None):
    if not font:
        font = QtGui.QFont("Arial", 48, QtGui.QFont.Bold)

    p = wdgt
    p.setFont(font)

    method = getattr(p, "setAlignment", None)
    if callable(method):
        p.setAlignment(QtCore.Qt.AlignCenter)
        
    method = getattr(p, "setSizePolicy", None)
    if callable(method):
        p.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)

    if func:
        p.clicked.connect(func)
    return p

class PageWindow(QtWidgets.QMainWindow):
    gotoSignal = QtCore.pyqtSignal(str)

    def __init__(self):
        name = 'PageWindow'
        print(str(name + " 1"))
        super().__init__()
        print(str(name + " 2"))
        self.w = 640
        self.h = 480
        frm = QtWidgets.QFrame()
        self.setCentralWidget(frm)
        # self.setFixedSize(self.w, self.h)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)

    def goto(self, name):
        self.gotoSignal.emit(name)

class MainWindow(PageWindow):
    def __init__(self, f, parent):
        super().__init__()
        self.font = f
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        self.parent = parent

        name = 'MainWindow'
        print(str(name + " 1"))
        super().__init__()
        print(str(name + " 2"))
        self.initUI()
        self.setWindowTitle("MainWindow")
        #self.feet_ip = '192.168.8.173:8000'
        self.bThread = False
        #self.threadStatus = threading.Thread(target=self.getStatusThreadRun)
        #self.threadStatus.start()
        
    def __del__(self):
        print('MainWindow del')
        self.bThread = False
        #self.threadStatus.join()

    def get_status(self):
        robot_ip='192.168.12.20'
        # Get Request
        host = 'http://' + robot_ip + '/api/v2.0.0/status'

        # Format Headers
        headers = {}
        headers['Content-Type'] = 'application/json'
        headers['Authorization'] = 'Basic YWRtaW46OGM2OTc2ZTViNTQxMDQxNWJkZTkwOGJkNGRlZTE1ZGZiMTY3YTljODczZmM0YmI4YTgxZjZmMmFiNDQ4YTkxOA=='
        print(headers)

        get_status = requests.get(host, headers=headers)
        parsed = json.loads(get_status.content)
        
        json_formatted_str = json.dumps(parsed, indent=2)

        res = "Robot_name : " + str(parsed['robot_name']) + '\n' + str(parsed['mission_text']) + '\n' + str(parsed['state_text'])
        self.robotstateLabel.setText(res)

        print(json_formatted_str)

    def send_mission(self, num):
        robot_ip='192.168.12.20'
        pos = [ 'f8fda182-717e-11ee-a0c8-0001299981a2', # 0
                '5d6ad2d7-7323-11ee-bad0-0001299981a2'  # 1
              ]
        mission_id = {"mission_id": pos[num]}

        # Get Request
        host = 'http://' + robot_ip + '/api/v2.0.0/'

        # Format Headers
        headers = {}
        headers['Content-Type'] = 'application/json'
        headers['Authorization'] = 'Basic YWRtaW46OGM2OTc2ZTViNTQxMDQxNWJkZTkwOGJkNGRlZTE1ZGZiMTY3YTljODczZmM0YmI4YTgxZjZmMmFiNDQ4YTkxOA=='
        print(headers)

        post_mission = requests.post(host + 'mission_queue', json=mission_id, headers=headers)


    def initUI(self):
        self.UiComponents()

    def getSize(self):
        print('getSize')
        size = self.size()
        print('{}, {}'.format(size.width(), size.height()))


    def UiComponents(self):
        btn_call = QtWidgets.QPushButton("GET STATUS")
        btn_call.setStyleSheet("background-color: gray")

        btn_1 = QtWidgets.QPushButton("GOTO_1")
        btn_1.setStyleSheet("background-color: yellow")

        btn_2 = QtWidgets.QPushButton("GOTO_2")
        btn_2.setStyleSheet("background-color: blue")

        btn_3 = QtWidgets.QPushButton("GOTO_3")
        btn_3.setStyleSheet("background-color: green")
        
        self.robotstateLabel = QtWidgets.QLabel("Robot Status : READY")

        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(pWidgets(btn_call, self.get_status))
        hLayout.addWidget(pWidgets(btn_1, lambda: self.send_mission(0)), 1)
        hLayout.addWidget(pWidgets(btn_2, lambda: self.send_mission(1)), 1)
        hLayout.addWidget(pWidgets(btn_3, lambda: self.send_mission(2)), 1)

        vLayout = QtWidgets.QVBoxLayout()
        vLayout.addLayout(hLayout, 1)
        vLayout.addWidget(pWidgets(self.robotstateLabel), 1)

        wdg = QtWidgets.QWidget()
        wdg.setLayout(vLayout)
        self.setCentralWidget(wdg)

    def refresh(self):
        print("MainWindow refresh.")

    def make_handleButton(self, button):
        def handleButton():
            print('handleButton')
        return handleButton

class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None, ip_robot=None):
        super().__init__()
        self.ip_robot = ip_robot
        self.font = QtGui.QFont("Arial", 7, QtGui.QFont.Bold)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)

        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.m_pages = {}

        self.register(MainWindow(self.font, self), "main")

        self.goto("main")

    def resizeEvent(self, event):
        # print("resize")
        QtWidgets.QMainWindow.resizeEvent(self, event)
        # self.getSize(event)

    def getSize(self, event):
        print('getSize')
        size = event.size()
        print('{}, {}'.format(size.width(), size.height()))

    def register(self, widget, name):
        self.m_pages[name] = widget
        self.stacked_widget.addWidget(widget)
        if isinstance(widget, PageWindow):
            widget.gotoSignal.connect(self.goto)

    @QtCore.pyqtSlot(str)
    def goto(self, name):
        if name in self.m_pages:
            widget = self.m_pages[name]
            self.stacked_widget.setCurrentWidget(widget)
            self.setWindowTitle(widget.windowTitle())
            widget.refresh()

if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    
    w = Window(parent=app, ip_robot='192.168.12.20')
    w.show()

    sys.exit(app.exec_())
