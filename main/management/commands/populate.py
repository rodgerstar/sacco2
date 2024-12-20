# from django.core.management import BaseCommand
#
# from main.models import Customer
# from main.views import customers
#
#
# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         customers_data = [{"id":1,"first_name":"Norah","last_name":"Lambswood","email":"nlambswood0@youtu.be","gender":"Female","weight":93,"dob":"2005-08-27"},
# {"id":2,"first_name":"Lane","last_name":"Everall","email":"leverall1@wisc.edu","gender":"Male","weight":81,"dob":"2006-04-03"},
# {"id":3,"first_name":"Clayson","last_name":"Denekamp","email":"cdenekamp2@qq.com","gender":"Male","weight":83,"dob":"2005-08-14"},
# {"id":4,"first_name":"Derwin","last_name":"Crinidge","email":"dcrinidge3@nature.com","gender":"Male","weight":87,"dob":"2002-03-30"},
# {"id":5,"first_name":"Mac","last_name":"Rieflin","email":"mrieflin4@archive.org","gender":"Male","weight":71,"dob":"2006-02-10"},
# {"id":6,"first_name":"Audry","last_name":"Ghidini","email":"aghidini5@alexa.com","gender":"Female","weight":66,"dob":"2002-01-10"},
# {"id":7,"first_name":"Hobey","last_name":"Mathys","email":"hmathys6@booking.com","gender":"Male","weight":98,"dob":"2006-04-02"},
# {"id":8,"first_name":"Carolee","last_name":"Pooley","email":"cpooley7@icio.us","gender":"Female","weight":80,"dob":"2004-01-26"},
# {"id":9,"first_name":"Gabriellia","last_name":"McLarnon","email":"gmclarnon8@barnesandnoble.com","gender":"Female","weight":71,"dob":"2000-11-05"},
# {"id":10,"first_name":"Wendeline","last_name":"Krolle","email":"wkrolle9@theatlantic.com","gender":"Female","weight":84,"dob":"2004-01-31"},
# {"id":11,"first_name":"Toddy","last_name":"Bevan","email":"tbevana@phoca.cz","gender":"Male","weight":58,"dob":"2005-04-16"},
# {"id":12,"first_name":"Tymothy","last_name":"Stailey","email":"tstaileyb@purevolume.com","gender":"Male","weight":76,"dob":"2006-07-19"},
# {"id":13,"first_name":"Imogene","last_name":"Dixey","email":"idixeyc@comsenz.com","gender":"Female","weight":85,"dob":"2004-07-23"},
# {"id":14,"first_name":"Guinevere","last_name":"Beetham","email":"gbeethamd@wufoo.com","gender":"Female","weight":77,"dob":"2003-05-27"},
# {"id":15,"first_name":"Land","last_name":"Turnbull","email":"lturnbulle@tamu.edu","gender":"Male","weight":80,"dob":"2006-02-07"},
# {"id":16,"first_name":"Geri","last_name":"Iley","email":"gileyf@ow.ly","gender":"Female","weight":81,"dob":"2001-04-10"},
# {"id":17,"first_name":"Ariel","last_name":"Matthias","email":"amatthiasg@g.co","gender":"Male","weight":62,"dob":"1999-07-29"},
# {"id":18,"first_name":"Quincy","last_name":"Ghidini","email":"qghidinih@techcrunch.com","gender":"Male","weight":59,"dob":"2005-02-02"},
# {"id":19,"first_name":"Worthy","last_name":"Diano","email":"wdianoi@wufoo.com","gender":"Male","weight":78,"dob":"2002-03-09"},
# {"id":20,"first_name":"Jennifer","last_name":"Leport","email":"jleportj@trellian.com","gender":"Female","weight":84,"dob":"2001-06-12"},
# {"id":21,"first_name":"Hazel","last_name":"Scamal","email":"hscamalk@cisco.com","gender":"Male","weight":58,"dob":"2003-12-28"},
# {"id":22,"first_name":"Horton","last_name":"Tschursch","email":"htschurschl@odnoklassniki.ru","gender":"Male","weight":91,"dob":"2007-10-12"},
# {"id":23,"first_name":"Ermentrude","last_name":"Everill","email":"eeverillm@reverbnation.com","gender":"Female","weight":81,"dob":"2002-07-24"},
# {"id":24,"first_name":"Kym","last_name":"Otridge","email":"kotridgen@tripadvisor.com","gender":"Female","weight":72,"dob":"2001-09-30"},
# {"id":25,"first_name":"Jeanette","last_name":"Worters","email":"jworterso@webnode.com","gender":"Female","weight":97,"dob":"2004-01-16"},
# {"id":26,"first_name":"Aviva","last_name":"Maltster","email":"amaltsterp@tumblr.com","gender":"Female","weight":48,"dob":"2001-11-04"},
# {"id":27,"first_name":"Culley","last_name":"Warlowe","email":"cwarloweq@epa.gov","gender":"Male","weight":85,"dob":"2004-10-16"},
# {"id":28,"first_name":"Patrica","last_name":"Biaggetti","email":"pbiaggettir@ezinearticles.com","gender":"Female","weight":86,"dob":"2007-06-12"},
# {"id":29,"first_name":"Aylmer","last_name":"Lathwood","email":"alathwoods@linkedin.com","gender":"Male","weight":69,"dob":"2004-07-25"},
# {"id":30,"first_name":"Rosina","last_name":"Maslin","email":"rmaslint@webnode.com","gender":"Female","weight":92,"dob":"2004-11-20"},
# {"id":31,"first_name":"Nichole","last_name":"Hort","email":"nhortu@canalblog.com","gender":"Male","weight":87,"dob":"2003-01-21"},
# {"id":32,"first_name":"Jean","last_name":"Alred","email":"jalredv@issuu.com","gender":"Female","weight":60,"dob":"2003-07-11"},
# {"id":33,"first_name":"Pansie","last_name":"Dewsbury","email":"pdewsburyw@livejournal.com","gender":"Female","weight":98,"dob":"2000-11-14"},
# {"id":34,"first_name":"Yorker","last_name":"Tomini","email":"ytominix@etsy.com","gender":"Male","weight":62,"dob":"2001-06-05"},
# {"id":35,"first_name":"Ninetta","last_name":"Eslinger","email":"neslingery@time.com","gender":"Female","weight":54,"dob":"2003-05-25"},
# {"id":36,"first_name":"Wakefield","last_name":"Joannidi","email":"wjoannidiz@icq.com","gender":"Male","weight":88,"dob":"2003-03-02"},
# {"id":37,"first_name":"Cletus","last_name":"McClements","email":"cmcclements10@bloglines.com","gender":"Male","weight":53,"dob":"2006-04-14"},
# {"id":38,"first_name":"Johna","last_name":"Holbie","email":"jholbie11@sitemeter.com","gender":"Female","weight":71,"dob":"2001-04-19"},
# {"id":39,"first_name":"Gunther","last_name":"Albrooke","email":"galbrooke12@google.cn","gender":"Male","weight":94,"dob":"2000-09-05"},
# {"id":40,"first_name":"Izak","last_name":"Tamburo","email":"itamburo13@ed.gov","gender":"Male","weight":52,"dob":"2004-12-24"},
# {"id":41,"first_name":"Inglis","last_name":"Minchin","email":"iminchin14@yandex.ru","gender":"Male","weight":96,"dob":"2002-01-13"},
# {"id":42,"first_name":"Casar","last_name":"Noar","email":"cnoar15@yahoo.com","gender":"Male","weight":68,"dob":"1999-02-12"},
# {"id":43,"first_name":"Alejoa","last_name":"Cussons","email":"acussons16@google.co.uk","gender":"Male","weight":96,"dob":"2000-03-12"},
# {"id":44,"first_name":"Conni","last_name":"Kleisel","email":"ckleisel17@scribd.com","gender":"Female","weight":81,"dob":"1999-02-12"},
# {"id":45,"first_name":"Mitch","last_name":"Harrald","email":"mharrald18@npr.org","gender":"Male","weight":50,"dob":"2002-12-28"},
# {"id":46,"first_name":"Tammy","last_name":"Hudspith","email":"thudspith19@mashable.com","gender":"Male","weight":62,"dob":"2002-11-28"},
# {"id":47,"first_name":"Edlin","last_name":"Bloxsome","email":"ebloxsome1a@usa.gov","gender":"Male","weight":64,"dob":"2005-02-07"},
# {"id":48,"first_name":"Louisa","last_name":"Wakeman","email":"lwakeman1b@yahoo.co.jp","gender":"Female","weight":84,"dob":"2005-06-02"},
# {"id":49,"first_name":"Doralyn","last_name":"Ciccarello","email":"dciccarello1c@scribd.com","gender":"Female","weight":101,"dob":"2005-06-26"},
# {"id":50,"first_name":"Linet","last_name":"Wieprecht","email":"lwieprecht1d@51.la","gender":"Female","weight":79,"dob":"1998-12-11"},
# {"id":51,"first_name":"Sibella","last_name":"Barthod","email":"sbarthod1e@va.gov","gender":"Female","weight":102,"dob":"1999-08-12"},
# {"id":52,"first_name":"Cecilius","last_name":"Pashley","email":"cpashley1f@istockphoto.com","gender":"Male","weight":57,"dob":"2003-04-24"},
# {"id":53,"first_name":"Garth","last_name":"Houchen","email":"ghouchen1g@thetimes.co.uk","gender":"Male","weight":97,"dob":"2006-12-22"},
# {"id":54,"first_name":"Dulcea","last_name":"Jonathon","email":"djonathon1h@fema.gov","gender":"Female","weight":52,"dob":"2000-03-19"},
# {"id":55,"first_name":"Dorri","last_name":"Oag","email":"doag1i@discuz.net","gender":"Female","weight":80,"dob":"2004-02-15"},
# {"id":56,"first_name":"Elke","last_name":"Gernier","email":"egernier1j@slate.com","gender":"Female","weight":94,"dob":"2006-06-25"},
# {"id":57,"first_name":"Deane","last_name":"Penke","email":"dpenke1k@newyorker.com","gender":"Female","weight":64,"dob":"2007-03-28"},
# {"id":58,"first_name":"Gayle","last_name":"Ducrow","email":"gducrow1l@amazon.com","gender":"Male","weight":58,"dob":"2003-04-12"},
# {"id":59,"first_name":"Emmery","last_name":"Cometto","email":"ecometto1m@npr.org","gender":"Male","weight":53,"dob":"2000-10-09"},
# {"id":60,"first_name":"Loraine","last_name":"Grindlay","email":"lgrindlay1n@delicious.com","gender":"Female","weight":88,"dob":"2007-10-17"},
# {"id":61,"first_name":"Bogart","last_name":"Paoletti","email":"bpaoletti1o@jalbum.net","gender":"Male","weight":61,"dob":"2002-04-27"},
# {"id":62,"first_name":"Tiphanie","last_name":"Ollcott","email":"tollcott1p@epa.gov","gender":"Female","weight":78,"dob":"2002-04-04"},
# {"id":63,"first_name":"Debbi","last_name":"Grigoriev","email":"dgrigoriev1q@mlb.com","gender":"Female","weight":51,"dob":"2007-05-06"},
# {"id":64,"first_name":"Odell","last_name":"Moules","email":"omoules1r@ning.com","gender":"Male","weight":100,"dob":"2000-12-18"},
# {"id":65,"first_name":"Kendrick","last_name":"Beade","email":"kbeade1s@washingtonpost.com","gender":"Male","weight":94,"dob":"2007-10-10"},
# {"id":66,"first_name":"Ambrosio","last_name":"Sergeaunt","email":"asergeaunt1t@ibm.com","gender":"Male","weight":91,"dob":"2003-07-05"},
# {"id":67,"first_name":"Ron","last_name":"Stanistrete","email":"rstanistrete1u@unblog.fr","gender":"Male","weight":75,"dob":"2002-10-05"},
# {"id":68,"first_name":"Ralina","last_name":"Vanyashin","email":"rvanyashin1v@macromedia.com","gender":"Female","weight":54,"dob":"2001-06-05"},
# {"id":69,"first_name":"Danella","last_name":"Gresswell","email":"dgresswell1w@artisteer.com","gender":"Female","weight":86,"dob":"2000-01-24"},
# {"id":70,"first_name":"Brear","last_name":"Aikin","email":"baikin1x@skyrock.com","gender":"Female","weight":78,"dob":"2000-03-23"},
# {"id":71,"first_name":"Georgia","last_name":"Pawel","email":"gpawel1y@artisteer.com","gender":"Female","weight":76,"dob":"2004-10-09"},
# {"id":72,"first_name":"Archaimbaud","last_name":"Peake","email":"apeake1z@zimbio.com","gender":"Male","weight":50,"dob":"2000-12-20"},
# {"id":73,"first_name":"Grace","last_name":"Dilliway","email":"gdilliway20@canalblog.com","gender":"Male","weight":70,"dob":"1999-01-17"},
# {"id":74,"first_name":"Gae","last_name":"Dussy","email":"gdussy21@miibeian.gov.cn","gender":"Female","weight":59,"dob":"2003-12-22"},
# {"id":75,"first_name":"Betteann","last_name":"Vell","email":"bvell22@latimes.com","gender":"Female","weight":84,"dob":"2001-09-18"},
# {"id":76,"first_name":"Raviv","last_name":"Kneel","email":"rkneel23@printfriendly.com","gender":"Male","weight":49,"dob":"2000-10-04"},
# {"id":77,"first_name":"Heidie","last_name":"Bakewell","email":"hbakewell24@psu.edu","gender":"Female","weight":71,"dob":"2005-12-01"},
# {"id":78,"first_name":"Ronnie","last_name":"Lapworth","email":"rlapworth25@taobao.com","gender":"Female","weight":95,"dob":"2005-01-21"},
# {"id":79,"first_name":"Osmund","last_name":"Salmon","email":"osalmon26@webeden.co.uk","gender":"Male","weight":77,"dob":"2004-06-21"},
# {"id":80,"first_name":"Gwennie","last_name":"VanBrugh","email":"gvanbrugh27@prlog.org","gender":"Female","weight":101,"dob":"2005-08-01"},
# {"id":81,"first_name":"Bucky","last_name":"Norville","email":"bnorville28@mozilla.org","gender":"Male","weight":55,"dob":"2005-06-10"},
# {"id":82,"first_name":"Micah","last_name":"Giraudeau","email":"mgiraudeau29@dailymail.co.uk","gender":"Male","weight":79,"dob":"2001-01-28"},
# {"id":83,"first_name":"Correy","last_name":"Cobello","email":"ccobello2a@posterous.com","gender":"Male","weight":81,"dob":"2003-03-25"},
# {"id":84,"first_name":"Danielle","last_name":"Fawthorpe","email":"dfawthorpe2b@youku.com","gender":"Female","weight":50,"dob":"2002-07-29"},
# {"id":85,"first_name":"Hazlett","last_name":"McKern","email":"hmckern2c@sohu.com","gender":"Male","weight":93,"dob":"2000-09-24"},
# {"id":86,"first_name":"Alden","last_name":"Grimbaldeston","email":"agrimbaldeston2d@mapquest.com","gender":"Male","weight":72,"dob":"2003-11-11"},
# {"id":87,"first_name":"Reynolds","last_name":"Rickert","email":"rrickert2e@microsoft.com","gender":"Male","weight":73,"dob":"1999-06-03"},
# {"id":88,"first_name":"Cilka","last_name":"Lammiman","email":"clammiman2f@google.ru","gender":"Female","weight":101,"dob":"2003-03-02"},
# {"id":89,"first_name":"Vale","last_name":"Ibbeson","email":"vibbeson2g@sina.com.cn","gender":"Female","weight":61,"dob":"1999-10-31"},
# {"id":90,"first_name":"Prisca","last_name":"Chaffer","email":"pchaffer2h@macromedia.com","gender":"Female","weight":60,"dob":"2000-08-05"},
# {"id":91,"first_name":"Claretta","last_name":"Dugget","email":"cdugget2i@is.gd","gender":"Female","weight":89,"dob":"1999-07-17"},
# {"id":92,"first_name":"Andrej","last_name":"Samudio","email":"asamudio2j@google.com","gender":"Male","weight":62,"dob":"2002-03-16"},
# {"id":93,"first_name":"Bertina","last_name":"Skae","email":"bskae2k@marriott.com","gender":"Female","weight":51,"dob":"2001-11-13"},
# {"id":94,"first_name":"Tommy","last_name":"Fish","email":"tfish2l@alexa.com","gender":"Female","weight":74,"dob":"2003-04-21"},
# {"id":95,"first_name":"Karena","last_name":"Dyde","email":"kdyde2m@friendfeed.com","gender":"Female","weight":98,"dob":"2003-02-20"},
# {"id":96,"first_name":"Haily","last_name":"Wastling","email":"hwastling2n@google.it","gender":"Male","weight":50,"dob":"2004-03-02"},
# {"id":97,"first_name":"Ariana","last_name":"Pourvoieur","email":"apourvoieur2o@stanford.edu","gender":"Female","weight":67,"dob":"2001-07-11"},
# {"id":98,"first_name":"Salem","last_name":"Shenton","email":"sshenton2p@yahoo.co.jp","gender":"Male","weight":90,"dob":"1999-03-28"},
# {"id":99,"first_name":"Deck","last_name":"Northen","email":"dnorthen2q@free.fr","gender":"Male","weight":85,"dob":"2002-06-07"},
# {"id":100,"first_name":"Devin","last_name":"Glasheen","email":"dglasheen2r@howstuffworks.com","gender":"Male","weight":94,"dob":"2001-10-09"}]
#         for c in customers_data:
#             customer = Customer(**c)
#             customer.save()
#         self.stdout.write(
#             self.style.SUCCESS('Successfully populated.')
#         )
#
#         print("populated successfully")