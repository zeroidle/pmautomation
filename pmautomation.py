#-*- coding: utf-8 -*-
from flask import Flask,render_template;
import json;
import datetime;

app = Flask(__name__);
dow = [u'월',u'화',u'수',u'목',u'금',u'토',u'일']

@app.route("/")
def home():
    return "Running...";

@app.route("/set/<sdate>/<edate>", methods=["GET","POST"])
def set(sdate=None,edate=None):
    if (len(sdate) != len(edate) or len(sdate) != 6):
        return "10월 19일 오후 11시부터 다음날 새벽4시까지 점검인경우<br>\
                 /set/101923/102004 형식으로 입력해야 합니다."
    if (sdate > edate):
        return "날짜 및 시간설정이 잘못되었습니다."

    sdow = dow[datetime.date(datetime.date.today().year,int(sdate[:2]),int(sdate[2:4])).weekday()]
    edow = dow[datetime.date(datetime.date.today().year,int(edate[:2]),int(edate[2:4])).weekday()]
    sampm = int(sdate[4:6]) > 12 and u"오후" or u"오전";
    eampm = int(edate[4:6]) > 12 and u"오후" or u"오전";
    data = {'smon':sdate[:2], 'sday':sdate[2:4], 'shour':sdate[4:6],'sdow':sdow, 'edow':edow,\
            'emon':edate[:2], 'eday':edate[2:4], 'ehour':edate[4:6],'sampm':sampm,'eampm':eampm}
    ren = render_template('index.html',data=data)
    f = open('/var/www/html/index.html','w')
    f.write(ren.encode("utf-8"))
    f.close()
    return ren

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9823);
