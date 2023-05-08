Invoke-WebRequest https://www.python.org/ftp/python/3.9.4/python-3.9.4-amd64.exe -OutFile python.exe
./python.exe /quiet InstallAllUsers=1 PrependPath=1
Invoke-WebRequest https://bootstrap.pypa.io/get-pip.py -OutFile get-pip.py
python get-pip.py
pip install -r ./requirements.txt
