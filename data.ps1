Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.10.1/python-3.10.1-amd64.exe -OutFile python-3.10.1-amd64.exe
.\python-3.10.1-amd64.exe /quiet InstallAllUsers=1 PrependPath=1
Invoke-WebRequest https://bootstrap.pypa.io/get-pip.py -OutFile get-pip.py
python get-pip.py
pip install -r ./requirements.txt
