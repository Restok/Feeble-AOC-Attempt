import numbers
import numpy as np
import copy
#DAY ONE PART TWO BELOW I DELETED PART ONE BY ACCIDENT TO DO PART TWO

"""numbers = "57276274387944537823652626177853384411146325384494935924454336611953119173638191671326254832624841593421667683474349154668177743437745965461678636631863541462893547616877914914662358836365421198516263335926544716331814125295712581158399321372683742773423626286669759415959391374744214595682795818615532673877868424196926497731144319736445141728123322962547288572434564178492753681842244888368542423832228211172842456231275738182764232265933625119312598161192193214898949267765417468348935134618964683127194391796165368145548814473129857697989322621368744725685183346825333247866734735894493395218781464346951777873929898961358796274889826894529599645442657423438562423853247543621565468819799931598754753467593832328147439341586125262733737128386961596394728159719292787597426898945198788211417854662948358422729471312456437778978749753927251431677533575752312447488337156956217451965643454445329758327129966657189332824969141448538681979632611199385896965946849725421978137753366252459914913637858783146735469758716752765718189175583956476935185985918536318424248425426398158278111751711911227818826766177996223718837428972784328925743869885232266127727865267881592395643836999244218345184474613129823933659422223685422732186536199153988717455568523781673393698356967355875123554797755491181791593156433735591529495984256519631187849654633243225118132152549712643273819314433877592644693826861523243946998615722951182474773173215527598949553185313259992227879964482121769617218685394776778423378182462422788277997523913176326468957342296368178321958626168785578977414537368686438348124283789748775163821457641135163495649331144436157836647912852483177542224864952271874645274572426458614384917923623627532487625396914111582754953944965462576624728896917137599778828769958626788685374749661741223741834844643725486925886933118382649581481351844943368484853956759877215252766294896496444835264357169642341291412768946589781812493421379575569593678354241223363739129813633236996588711791919421574583924743119867622229659211793468744163297478952475933163259769578345894367855534294493613767564497137369969315192443795512585"
listed = list(map(int, numbers))
endnum = 0
over = 0
for i in range(2120):
  if i+1060 <= 2119 and listed[i] == listed[i+1060]:
    endnum += listed[i]
  elif i+1060 > 2119:
    over = i+1060-2120
    if listed[i] == listed[over]:
      endnum = endnum+listed[i]
print(endnum)
"""
#-------------------------------------------------------------------------------------------------------------------------
#DAY TWO PART ONE

"""storage = []
numbers = [790,99,345,1080,32,143,1085,984,553,98,123,97,197,886,125,947,302,463,59,58,55,87,508,54,472,63,469,419,424,331,337,72,899,962,77,1127,62,530,78,880,129,1014,93,148,239, 288,357,424,2417,2755,254,3886,5336,3655,5798,3273,5016,178,270,6511,223,5391,1342,2377,68,3002,3307,166,275,1989,1611,364,157,144,3771,1267,3188,3149,156,3454,1088,1261,21,1063,1173,278,1164,207,237,1230,1185,431,232,660,195,1246,49,1100,136,1491,647,1486,112,1278,53,1564,1147,1068,809,1638,138,117,158,3216,1972,2646,3181,785,2937,365,611,1977,1199,2972,201,2432,186,160,244,86,61,38,58,71,243,52,245,264,209,265,308,80,126,129,1317,792,74,111,1721,252,1082,1881,1349,94,891,1458,331,1691,89,1724,3798,202,3140,3468,1486,2073,3872,3190,3481,3760,2876,182,2772,226,3753,188,2272,6876,6759,218,272,4095,4712,6244,4889,2037,234,223,6858,3499,2358,439,792,230,886,824,762,895,99,799,94,110,747,635,91,406,89,157,2074,237,1668,1961,170,2292,2079,1371,1909,221,2039,1022,193,2195,1395,2123,8447,203,1806,6777,278,2850,1232,6369,398,235,212,992,7520,7304,7852,520,3928,107,3406,123,2111,2749,223,125,134,146,3875,1357,508,1534,4002,4417]
listed = list(numbers)
anum = 0
'''for i in range(256):
  if listed[i] == " ":
    listed[i] = ","
joined = "".join(listed)
print(joined)'''
#print(numbers.replace("  ", ","))
rowcount = 0
for x in range(16):
  for y in range(rowcount, rowcount+16):
    storage.append(numbers[y])
  anum += (max(storage)-min(storage))
  print(anum)
  rowcount += 16
  storage = []
"""
#------------------------------------------------------------------------------------------------------
#DAY TWO PART TWO
"""storage = []
numberss = [790,99,345,1080,32,143,1085,984,553,98,123,97,197,886,125,947,302,463,59,58,55,87,508,54,472,63,469,419,424,331,337,72,899,962,77,1127,62,530,78,880,129,1014,93,148,239, 288,357,424,2417,2755,254,3886,5336,3655,5798,3273,5016,178,270,6511,223,5391,1342,2377,68,3002,3307,166,275,1989,1611,364,157,144,3771,1267,3188,3149,156,3454,1088,1261,21,1063,1173,278,1164,207,237,1230,1185,431,232,660,195,1246,49,1100,136,1491,647,1486,112,1278,53,1564,1147,1068,809,1638,138,117,158,3216,1972,2646,3181,785,2937,365,611,1977,1199,2972,201,2432,186,160,244,86,61,38,58,71,243,52,245,264,209,265,308,80,126,129,1317,792,74,111,1721,252,1082,1881,1349,94,891,1458,331,1691,89,1724,3798,202,3140,3468,1486,2073,3872,3190,3481,3760,2876,182,2772,226,3753,188,2272,6876,6759,218,272,4095,4712,6244,4889,2037,234,223,6858,3499,2358,439,792,230,886,824,762,895,99,799,94,110,747,635,91,406,89,157,2074,237,1668,1961,170,2292,2079,1371,1909,221,2039,1022,193,2195,1395,2123,8447,203,1806,6777,278,2850,1232,6369,398,235,212,992,7520,7304,7852,520,3928,107,3406,123,2111,2749,223,125,134,146,3875,1357,508,1534,4002,4417]
rowcount = 0
total = 0
def division():
  counter = 0
  global numberss,rowcount,storage,total
  for rep in range(16):
    for v in range(16):
        if storage[counter] > storage[v]:
          val = storage[counter]/storage[v]
          print(val)
          if storage[counter]%storage[v] == 0:
            total+=val
    counter+=1
  print(total)
for z in range(16):
  for x in range(rowcount, rowcount+16):
    storage.append(numberss[x])
  rowcount+=16
  division()
  storage = []
print(total)
'''def divisiontest():
  counter = 0
  global numberss,rowcount,anum,storage,total
  for rep in range(4):
    for v in range(4):
        if storage[counter] > storage[v]:
          val = storage[counter]/storage[v]
          if storage[counter]%storage[v] == 0:
            total+=val
            
    print(total)
    counter+=1
        
divisiontest()
  '''
"""
#-------------------------------------------------------------------------------------------------------
#Day 3 PART ONE
"""
numcount = 1
loopcount = 3
x = 0
y = 0
x+=1
numcount +=1
y+=1
numcount+=1
x-=loopcount-1
numcount += loopcount-1
y-=loopcount-1
numcount += loopcount-1
x+=loopcount-1
numcount += loopcount-1
loopcount = 4
print(loopcount)
print(numcount)
print(x,y)
targetnum = 265149
for z in range(460):
  x+=1
  numcount += 1
  if numcount == targetnum:
    print("(", x, ",", y,")")
    break
  for a in range(1, loopcount):
    y+=1
    numcount+=1
    if numcount == targetnum:
      print("(", x, ",", y,")")
      break
  for b in range(loopcount):
    x-=1
    numcount += 1
    if numcount == targetnum:
      print("(", x, ",", y,")")
      break
  for c in range(loopcount):    
    y-=1
    numcount += 1
    if numcount == targetnum:
      print("(", x, ",", y,")")
      break
  for d in range(loopcount):
    x+=1
    numcount += 1
    if numcount == targetnum:
      print("(", x, ",", y,")")
      break    
  loopcount+=2
  
dist=181+abs(257)
print(dist)
"""
#Day 3 PART TWO
"""
curnum = 1
sqco = 1
array = []
max_x = 2
max_y = 2
numcount = 1
curnum = 0
array.append(numcount)
loopcount = 3
x = 0
y = 0

x+=1
curnum+=1
numcount = array[curnum-1]
array.append(numcount)
y+=1
if x!=max_x and x*-1 !=max_x:
  try:
    fuckthisshit = (curnum - sqco**2) - 1
    numcount += array[fuckthisshit]
    print(numcount)
  except:
    print("no diagonal num found")
"""
#x-=loopcount-1
#y-=loopcount-1
#x+=loopcount-1
#loopcount = 4
#print(loopcount)
#print(numcount)
#print(x,y)
"""
targetnum = 265149
for z in range(460):
  x+=1
  numcount += 1
  if numcount > targetnum:
    print("(", x, ",", y,")")
    break
  for a in range(1, loopcount):
    y+=1
    numcount+=1
    if numcount == targetnum:
      print("(", x, ",", y,")")
      break
  for b in range(loopcount):
    x-=1
    numcount += 1
    if numcount == targetnum:
      print("(", x, ",", y,")")
      break
  for c in range(loopcount):    
    y-=1
    numcount += 1
    if numcount == targetnum:
      print("(", x, ",", y,")")
      break
  for d in range(loopcount):
    x+=1
    numcount += 1
    if numcount == targetnum:
      print("(", x, ",", y,")")
      break    
  loopcount+=2
"""
#DAY FOUR PART ONE

arra = """sayndz zfxlkl attjtww cti sokkmty brx fhh suelqbp
xmuf znkhaes pggrlp zia znkhaes znkhaes
nti rxr bogebb zdwrin
sryookh unrudn zrkz jxhrdo gctlyz
bssqn wbmdc rigc zketu ketichh enkixg bmdwc stnsdf jnz mqovwg ixgken
flawt cpott xth ucwgg xce jcubx wvl qsysa nlg
qovcqn zxcz vojsno nqoqvc hnf gqewlkd uevax vuna fxjkbll vfge
qrzf phwuf ligf xgen vkig elptd njdm gvqiu epfzsvk urbltg dqg
sfpku viwihi fje umdkwvi ejzhzj qrbl sfpku sad nawnow ksnku
nzhj mfudick ueaa jnhz kpy pzk
euiin xvl elaoelu wbdd xlv jtm nohtq gfdbgdg gdfggdb edtym
xfmkn wyww woe hwysuh gjw dtk utryasc dela eluk vmmun
nmag qfwe cwslmgd nlhf hpf
ifs sszo iod isf jna
pjptwg wreera leyb hmlbpf qcrbma ylgue
rwlpo jhla rprxvgs quguh pyybwgl qqvcb
rxtcpdy wmpci mpcwi vwvdzdn nfpnj rcsxinl itatg ycy hrctg ron wveju
zmkfn wip pyiz pyiz tnyg dvftf elks ezhotbj wip
sgmtfdd xdl sch sch yaxzh wphgksh knzrixp yaxzh etm czqbaa jldta
gnbr rnpd upe eeb sbq sbq oxc rwvugoj
cshk thcc emfxx emfxx pbtcf jpim vltkqar czy iudkac jhpcc nqs
uzbvx fkiuyk izxdiu yutntvn dixuzi hkyfnud oyz ynutntv
ewl mfns idy fphu yqccb pte unukirt unukirt fdx
lzn tin fgena qbql qycbdw gbtn lctlysx adhjfq blu aiv
ites ites pbxzunl vljzh lqgerta pbxzunl
vmk wjfzvhn pqkidze qfwh
tqprmc exypl caf kwikh mdyyljc pbo hhxxo skna
sqxgejb ejc fvup hpesvs luz fcxqwhr ypxof fxlcp pxyk xiczjri
vjg qcw fsyqaoj mxf jha feclqqr vzdqnk verw mvmvm pvdqtcd xsfu
fwwn ktvdh aecfv acfve yjozxwo cnujw bcgde lphnk knlph bqwlqju
uwwapm dlln uwwapm uwwapm
huupab ewetcte huupab ewetcte
wjs zipivpd klwafr ipcczg wbv uujstsw hykn
mgojdyh hlm xruta lbmaxit pabqrnp vkyigd ptpzr glin gfau pbo
tbwx baqxq vtz jwex tvz tzv
efopwx wfknzb ogaxln tqzrh jne zugd zpxikma
rdjsa arjds hqdldw fjrtl midt qjv jfrlt
dggqohj bidaaty iah lgmug wwmlbc lggmu laonaoq erkqrb tqolnns iygv qnonlst
msc glwn xjfnij itt pka irrafjd euazydj silo
zsyut znsht ldky zsyut dzcdft znsht
iit cyteu pib fgvrs iux ffctql pib zuzp zsbb ieoi
xxtwlu kqfxjhq isj xqjhfkq dohrs haovzc cgfwfrt munqon vuyexz nouqnm
eptpqgi uiflvd acj livzq ejtt bniud cjdh jkrcken lspfy tpxri zibj
zxme dpo fumup gly bkdcwxn lsly eglhe
uoshw ijoyiql rcskaa vjbqv roiinzi fppqdu
xuw vdbxie oypcx khxq xebjt oypcx uitqep vdbxie hoz
lrjv tdksk uebo wktebvx nlapmp udhhxh uliqbm cklyyf jlzw xrmdlvx
fosspck fosspck fosspck qyidyur hxnxmb dkpj
rmrvlms susvos idw hzy idw tjgxbc lhgqxr tjgxbc uuq
etjmbdr hwqe lnfwzni lnfwzni good eisci etjmbdr
yqde bmlcc yuel vpyplss vyvhho kslgiu lllhc jtkijdj uclz hfbqsf
tlohlvv tlohlvv bdqahw tlohlvv qavcqrn penia saafy
lvtzyt qffe eaikhv eaikhv wbnl mdkg mdkg utfrm
luowwk magp luowwk oyao oyao hsb yms
gnxply vsdqum nprf jik axdp ariqjpc hjqcc
izbo nkqkb xpqg pgxq qpxg gpm jxbkvu resj
hsgyxar hvsl ner zzmcn lcpdvqn ern
rfjlhu xkyh hafs cvvk drg vjsk mymc iab ycmlubx kpwemiw
wlci qhhpr vhpr oyrili cnynh sivdso ldjya wilc ioiyrl
cdfwd mbtk sienxui jsmxzo yxbeyl bybtc covxaq yuxn ktbvztl ktbvztl rcekjhk
ptenhqv tzdt phetqvn mfkdz
hmezeak pqvqld amsih jxqacc uferfyh nfqjsz rtuqdzz pohcx qia cpxho hgpqs
iygny dluc uxqz nlujm xkdtlm xbdgepg jwn ohl wpfll
lnqf pcxy cpit enp zpj lqfn oowgw yoxdff ohvcfcf fuvz qkpmb
oydu jlscilm pzxen nmtdngu tslcupx ntdgmun uztpx nlhh jqn llsv
euyx epn gyvg cwtoe ruyap yaurp uryap obbl ovo
pgo irm ksrxe qotuygd afwh qfhzfsr wafh dqjbwce dzfo hew skrxe
dpvel dpvel ipljjxs vrrsob iakey uheuu swxu qmnmn mpjkb jqrwfmv jozj
sempz plzxqe qvyg sempz fejux
cqgqvg zhqir rqzih vyu fmb mfb
uejl kjh ayz dzimg yzafvg dem vlogg
htfkd htfkd hwykmm htfkd
oxvgq wtai rkyyxya ldkecdv
lvlrsu rsullv pptnrwi slvulr vxrk dpzti
gde ixwoz nnsx nhc nzi
dsadkj qtgya wco psyondq jayad crc lswwm purrad pof
nocibgs hxqdejv nlqxdpu dvzd
jfaws aiwnjm tqjpgs fuiobz gwnemv hjevs xkbbgiq sakgv zmwpkuq grjllw
xrr jwhtchs boaqkg wjhdr xrr
vyapct tgw juzgwkz odddvof juzgwkz
unuu kubdd dxr drwg
qpefzz iemo fwa vhdcxx
hseqy copss gytzub lxi mrxtwc hxqqdfx ijt kcy tafjs jit
uevse rrq zmwyjfe xljx lhgnyzt rngvwqd
gfvpyhq xpdhind eocgpiz ebs pcmsgjy swni iwns thspnh yvbzxz fgb
hxr ehw ekfd ncxcs gxjmd oqszdjp fgu gwuoafw zumenf qltbw whzuxov
wfc pawqo pim jxgt dtiwzil hdptivc slkazm htafjih hzheez rkk amy
mgoatiy pkec ddvwyni zuya aqrcjes ubkaeus nuhhad upe qfem bpcc
rmyeg qfq bia lzk fusqfb ltvgry vggr xaxi avwdkbg zhlzt
zkjoeee dyi sxdwfqa irqljmw gek dgdb mrakr ddaznn zlh ajzzacf juv
kmqcy pohbej hujdgao rsxfkn vlu
scnpa hvl cybql lvh lbcyq msw deqqb yjpsndq
ndhjooo dpf ziey jtjlc eesag ldhgoif
tysbae wkpst kjz stpkw sil yetsba
ghvlfq flhvgq tgkjie gqlvfh
oimn vlmsljl ocala vokhrs odyv msn dzly wcky
cfjwmh rpsdor bttnkg jxenm mwdk mer jgsusdz cslf
ialvxk bvc qjfikr caw puhmmfl xpmsx
tyoey egcf dijg vywd enued uxkshz nav bdrn hjugffi iobqwiy
eykhxck shpfjhk vlqg alkenz kuj okxs oeth mqbr nfvqvkv xfvyi mboo
zbw curcajm mel jxqcw mpdscxq rhadty zrddeh wmedc wkcwt yvwm
iee hzeofmh pqlkkb azlam fpj hzeofmh ripi
sawaqek oyoiwtb npq pisadk nnd bzgo wiqme lxnvn
obqx ffiegn obxq for xobq
zwway wwazy aqxg gaxq
ebssilw nuscati mofyc sogyacc yujmdwu ehxsx qcaf udvoo nlcfaz eov
vnbe wtzzjn bczyxt crmvas zujy kukq zujy kukq
gvltk kgltv kglvt zflikic
hby pium gut fjqn sksoqyq kcliapa
tbonrr prf vga jqgw ulze ukfig
zafixw hia omgwoi noeiox fqbket iviidgp bebune kwcuotp slvy wcx
fjq cyecn fhxvj byv kojvj iaqd aaxva rkogp
vqbbt sjmr mxu mxu rlfj yqhtzv cuar yde yrs sjmr
iyxiyp auepgw dtpbyvu thuoai fpsfkpn bemgbsk lni ozy jogp xldyvvx fpsfkpn
jtha ibn ahbkh xzxkei tql mycvmyh ioyw
mpsc pvdiuu wqixxlo cqwmlrw cttoz lad
srl xxlnofu dqf snxd zjlp htxzd
fkv berlbyh kyna wkme qjzgh thpw frup
irhreaj udkpbza qmgp ormlipa lbyuc
empizc apcb ossmtj awk ttsgi bfoymzd ftx jkicph qqjv tywp fwzfe
zaqkd ysn zaluvs rljdk ast fjp amjqr uabrya ufswzjg vcldkxt hzsmrbl
qvy tqgnwj akibr tfjevhv vav
mhe sxg hacoa emh kasf hid jklfy ijk dih
qvwbenk akdctm jztmsx aqvpodu vmknns nck letcrk poba
lhve kkvff iiixid vtsun uvgte mmlxk pgd
gktphd aaoqwz lrvsuw ofcyvmi suvwrl dpqiol wjgj uqigjx
tbp xoc lmz dyzlvp bjleh pxj xjp xbil
gpzgvj tctszm tctszm pnp upqtmm rribg tctszm sllsbr
hpm qvjnd lyqg bybpwn etz pwfigbg uqgrvpg cvniubo
tpowus bdncyxg gmm ebfg zwoue izgkwtx gmtfeg xvudp xgmjp atrvn aqgl
wlrxvo wvonohi owxlvr owhnvoi
knyo aiixyi sjtqb kukhgv qkj qiuefb syhfc aoana okmot tdsmnoj eyzqjn
szhto szhto szhto fxpsavu dtcz hnwqdvk iza
poykme rboczge tuyiw sxr
lpgbp bpmf aiqy exzqt gxdoow yjp fxwdmt eoklc jnps zbnbiwr ppvl
huecy jjhyz pwcea ffofmj tts
ahbmkw brz xdenmw mwexnd ncdxgf gcxnfd
yhfnra vqljz bkyxzt vhtsyde ysaxt qbw
gqhiej rofhmp soeebdp rcuiblb rcuiblb rrnh nses
pxrwe suil iihzf lhcgmfm mqasxh ttpp kqitdyf cuabaa
cxl cwsp qyseogj dimvv igsoxu ncrexla ubrvpp oum usluv
rkmo jqqcdjb mobqcta pbcmoi afjlh mork
nmohoeq fezpxh fezpxh yec
yxlncrt ivi dajo tjpim tjpim
hzhy rcjs uhyvwz tdpxlqw itoiyf
ded apfmhe stfk ugyujv drwks zagqnw mbbzmvc aoupemq
iezre wivdwif xzytxe xwytd vpnol pljx aot phln ztncw
ozblu asda tkxh xqe pvijnl qwwh uvp bdhtgjt uynwtav cdz uqmvp
eukgtsy kdfb bdfk tnv dfkb ewdemb
rsf cxnk cid qsa zwk oetnggn
fpq oim zetbmlk fpq oim xgv cbaj cjrqm
phgldt fhmkc efkztj qidri vsv bvjf lfwfgm wfuoln toamg wfuoln idrs
iuc rrdnk rrdnk asqhnz qxkigmo eeoim mmdtgif akk
rfvsyy kopfhmd tnv ibo demeqm gxrxw hwk ukorln bep
ialo eogif sxlj xfegx nanch egoif eymwt
kttrpjq gbnyiat kptg oarewx vkmt gbnyiat szyokf
tjll xviodi tjll efc rliugl wfbbpq wsqvdli jur tjll bguqyu
uecm yzjhn vqf labnc xyaksj
hjtef zzq ellr wtrodcg drwqo ernt uzx sqiokam
izmh ddutl bdzft jvfthh
ecr xqrp qlxstu kgprd gqvtwni mkughf bulabe bvoxkx
jwsna vjwq swkycg cpp dvmyal xotxviy qkiva ffa eakwp fww yirri
ufnl lpuxw rjki nggh ajdkpvo oeuaemy bjisma vsjzc
ctxu aavlw rap fzxtcp msufn fzxtcp sdlaom vgvdvpc
rftw cyf twyxi orifavd
ogiht ertz wcw jnqdup phvp lbw
tplpyq jeh aobamqe bvaim qptac gssi mkjbaj
nmklyg iitx iczojzr vjspqb uooky uooky hjk
ggnekbb bnebggk sepzjd fvqfgr
wnfwrn yaiogv mbusuy cpbcgs thjea
atndjc dbjgdz guedeay rasa kfhame pusuu dbjgdz
xivzyml xivzyml eqsykxo bshvz xivzyml
nfe ayx gscy ylyp oqyl isatnpx poaelm zsrw dpd eyrdjpq yllk
feqktz mlm jhi yxigeu xzqa qwv yquxw emken jgqsp rojfcu
ruvfcud poubal xswer hfhpyp guf pzgzoq pzgzoq jwgxafi guf kqzzlu apg
rxwcsdc rxwcsdc ywu rxwcsdc
dmgsey xrtx wldwyxz avi
yxnqv ewlx fvif ozfcbxb zqapa yudqksk wlxe mjpvgz
ozoa ozoa hwkbp ozoa
qcv drtqn uqv kcsavgn ybzs tkw
njmloq wapa srm srm ifurca
ezm ccj rub yuaww xhee liikjee kcabgic sbgqx vrpyo pzmesdp ksvv
hycyne raaksm nylsc lcpgn akasrm vxwoaum
zhugs pqquitv bae lyozb fhij pcdcc bae rygsgm pqquitv pizz
oxx bzk grpis qiqljwh svkn
qcq qqc fzgn sqg
lclad motw ukz zghp
glr okzfs zgv ygsvv sauuog glr amxr vvmwmu khy eyh
ukpxpy rgnqyaw ncm coeblf
qdbr ortzo spvnrnq uomtj vffbeva
miwar bidfxp eibo qyee
yldec ghwj mxlemvi imac klkvmg fekxhp kevlzfr fcgnoq fncgqo
hlm vlol qdic rltij nlzxfys rzpoh
krpwspb yrosr hioqla dbpgzgu dvkvvc vvdckv lcjzb qbsbr acbi rtnk
iqtvk jcldzuv smly whmnte mdwlse mkxw mfnkv mkxw kes owkfh
iwcjmkt rnb bjcdjl furhzuu exs
kjwu iuaj ixkujoa jzeau whpn
tvj zrdy fwsbagh zrdy czuzum lxotprx wbohaai
crsyzod jouf osxntw iwzzie bodu scze gjxn vgxvqo gjxn mmthykb
dabjfb vjqz cvr gsymwoe qzpusj twvwhw gyvlqd kdrdkzm bdljp cvr
vmswdz lgjsvxz yjkgqkg tzmjkfp uzbmwxe kuqa dzomt hep jjlibs oxvpvq cix
iqgd btwdjd ncdrovj ltxqc orwhdlo orwhdlo
nxro uxj ovgha elvzl xmlzssr wonimvb urecfx dbfn kope
tbes cgyh fypswue fgxjqtd dxdrfm pzhnaeu kugspa
eouzw qrpokyb fyhpb bcvfvze brdwey gpaa fpqutw pbqkroy axtc egamku gxk
xdrovpt peeww wkcin suir gvrbix
hgsjks juvod jtii iijt
yaw hzifa wpagkd tgvmc iru yyeuy mgcvt fhiza
lsk lks kls edypaxo
tjz qjs mgoyd gomyd ztjbex nprwk vvw rtjsq quvf vuziqtb oygdm
kftodz xua lyxt zfadf fgdwt zfadf xua ehwykd wniahd mqoarg
qgiapb xptk iscyf zfspn qvrpva egufqte zfspn hksw xwxrs dkdruku vegfs
wqifs wfsevg iwnjjpi oajju tkvhpl lemuw
rzbmhso pbvb lfgpq fzjwxxh pqlgf rbhsomz
ufi aiyd gxozgx hygjp dtma uughdc ojumcf yuadt
caami tqzkvor tqzkvor tqzkvor
vhtnvyx myxdywi mwpwq hjxadd qkcj vvytxnh dmbea
jvjtcjg mbiwyad cup xkrfk puz uxpmutf rjxyxyn mfchc
ocrak zprfbgu pjjzl zoehfkm xqn qki uxq tcv emknqjp wvmkas
nxg myr myr vnfzpoy
gwu ezt kbmeouj sxue cxax gcquz ieegnal xecusia vxf
xermi xermi qporwc mzemns ticltnz ddpsstr ddpsstr slgbn
xnujwtw bvzv xjwntuw unxwtjw
tipo akp fkmcls wglmjq fnrtsv
fan dfbya qrp lcvxqqu ldpm gucmeky mrzy fixaph rygneb ocm pjh
ovtrqs ujmbnal geihpe mijhy eewuic toaxbp ipy tvb evlmrtd lbujmna
lsmbwwd hvurk ihbuek hvoyq erzomhn gue lpq dihon dgzvst
fuoshq hfrzeu zfrhue ufqohs
icgwnbi gmhogxu gmguohx toixb hfwj haxlav hbe jdpxeyi xtgfi
vfakk ioil hddqu sdztx hduqd bmiuyr vmas
mcvjjhf sfgt sfgt lambvp dnqc pfecquk
xgr omy bmoadg afbna mar nicpazd iveku zdioyo
rpipon dwg wgd pironp
fkyx wjefuy mfesst ztlf gnnceb rsbvuk ckilt kliqnm iuifcvu
lmgzx oknwr wmttry luipa vcttj nuqdmy
iota efrxkk daqzm certtoi nnvqrwz qrqgza tllwp efrxkk
alde wqmdjy erh txrtqm zuljg hspbnrd pvsnebh bkue pvsnebh txrtqm txtthn
hgggm rswwfpj uctzrv bylqeen dpbnw ostsjwn jtjiyuh ofxu mmmqlg ayhza opbgdrv
qmhkh orbeokv agosach lhujcju jzpp wmxtcy jcxglu iuwmzrv xwkgz sxlzld
dzcdm lwal xpujjm xpujjm lpfojz lqqcon qmqrg
gmwugq ceslt rxcogaq jwkraq
joxr brdy yixlou brdy lnr lnr
wbut pxlsclt igigapq zeacg jxiezn hvws wwz ujpbl fdjtfjw opod kea
tsodswf pufo zqrt zvcpu
nyy mrqmg zkt tslzsf zkt
hxywv lbmogd hhv npyzgjy whfvv mlfqjr ggjz owijo zmesslo gtvizw
xzz dvpzxbd wxwlp cye rcqpgrr gynzo nhy gzpk fpfmb
nhaakbv iazpdc yadqbe kmqm dffq lidnh cegjosw kgd hwivd wijj
cwmdyf huoy awihev qav cwmdyf rdwck hahj pesfyk uoju zrirjdu
qabl vwcwbb phnd xnp huuzwxl rukbp kod sfu ngcvgrt buncnfw
regyd gjzfwf hpuv zmm vphu gwffjz
rdf emo crsoeo bksetj aqfzm pphny
opbmboi iakvj ymjwm vxoq qvox yafk zkch adlusz
qhm jul zasv xhu qnhjwzx
mjmyvd mezfuls upbdpzw awc qxta bzrx tjpjmj dxfyewc zorm
bko kfokm htcpoqc liuvj xhmpcu ccqphot dthvo pfj dtxpmu xoocm cmxoo
kxv eenns qhpfsvo gqoyv jzjho aoscl fetug agxmfea aygpt
javmegf jlmt epdwy egfs hwv uszcqvn foixpz iukh dbuhqgs zgb
zrex zrex xtx ydan maomp hqdhh mfvan broh wvwhqbu
phatsot joipm pmniq arqzmbe vurl bgy iwbwk oyhngcv vnzbzgm bgy
xprufgn vhca nrs abuh zwsxmhk mqrj tyslsij ojkdzom wepxg koodzv ypvyy
vop nnpz mcod mlli ntyhz laqztb kauqkla gmrfte pcuhaci
vrenj lypors prknc djbdkzv amofdx
lgig lojnrw obusoc fkwe ggnv pydcraq bvdivl vev mrojjs rxa
qeg tap jocwlsm vqxa lmjscow
gptlrgq vdasm erdc oparmw
rgbsa nacqhvm pczf anupcp upudwgp
jbnobi ifhzrd ihrkkf osw wos lrnwv
aiuntpl fcxpmz fplacs fplacs tipm gfotkx
fsbnd qoc ozmbi rqv fmbxh tuso kfoxvjn ocja zzs jwplx
muaklvq ghozoxh nwxbh mgoou ufptl ouhh reyuf jougckd dgprag
gwbnqwv dtrd mkzxinl erxl zmfa skuu crxmp wwao wwvdpk nxbn lglzy
qeejk wvnypc yfzyfcr eeqkj
nmcp fmkgfyi grfthau azw
kkallxz rjke ukbt ixkhfb bktu jkre
pxj mnwe djrjde gpsc enqz pdbydx cktfs jjeddr
mgplj yyunujc vis odee ccesa yyg yjcnuyu doo utse
flyy juvxomm vcdcyva lfyy ozxnuzw bmgns
kmsypi zpbyiv rrycnb qos sslwyeo jgbyv njltzt fuwk nwfb ozcf xqnf
sdcvgmy sdcvgmy hzv uyq sdcvgmy
fyox vmgxahj ywaxbmm ugy ruwc mys yrjwr ozsxb vaq
gjpyc sgdn kgm fbvq cziui nzy bwu ezjkkus jrag
kxcr tgjxss xkcr bembjv rbbiw bwbri
dcz rrhvdc zbonfzy ubjt
rvq yjnzswt vatkopb xlj dwxig dqlt qts iva
lylclc jptz rbidu lbt byxk
lwre vwriwh afixsi vwriwh
kmvbflr nfptw fbglxh pyas dxmn hemf segaz zrs
dvbey zmj xfoi bma udtxhb
yryng geiwgz bbrvjp ala
olzicp olzicp qhhslry olzicp
exf xdmwh xdwhm nhjsssn rmlkdb excguia fex
xkwgeso htys sjdk jizciy gjjl phgqdjh wzdb izew zcrumu llxfp
frkohf oifsm aisebkt ijsfkot ukk
koqf xvoior tpe erfpnp npnx
sneysk nsxki wpmhd mdor akrpvgz moicncj sbsj owfhj exw
oqqbvk xztx gtxlms icmo
lfy ltq dlzqlvi ovbrsa gzm nhcjq umbtgm nhcjq
iuopdzq cqaeuu xuzngq kxlx laml slvvr frtml tvioiez vyoomw xickbqh
ckahov mepeku gtaf gtaf
tlto cnnz kzsbkjo kzsbkjo
kqf comkf dvrkyl jdsqi rnwvb vxvd pok
hncq xcx yuykfs egrruvw yqh smcou
tywyq xeq cix yywqt jhzptci hybcoe
zsw zsgot wnu sumd azmuos qawjaz rpf zkxgwdu iom igh
vmxmelt gll ysbbt yboqoyz ykdglk cnypf otn owsz ipn epfeka bkmy
wxjpce etzyavi whb sxzft bfu dgwnbgc nfw sxcteis qqpk
kofv dgoyme vlza oxhbo lrqt uic tvfqiyy iaqm afnk
nsmpg wkibdcz dxbw tlxzm zgwe nqwjji eacbhn blk
shlgws eencr rtufah kjyvqw transt ecsq otbf
obs xsjceex ffqj sob djpq jcda zlskve
rfqtle klarp mtzrx rasr eisqovk rpt vymibt zwrif ilsnd
ldu ffd ldu tizfexr fwpmyan
flxso tzec pzn flxso kzdouon tkvkj
tvd arh qywql uev btvnpm
wtwx kzafvk ybyzmhv mdbrphy vamlvr gbxhod tyulba krcqj ikotmla qfhpa
bnfin ebngj agfdfzu rhjtj aaqzh fsyp nilar uwurjnu hhmso hhmso
uanmesj vshh syosjdt xkormf syosjdt ifvytwl qnw vshh jkg
epyzcn pgdxgye lecnx nebg jzdhvge hfy imiyft
zonbcnv vuvg sxtuty zdhmiow lmud cuegzg
bxgft mxhzrh unqd pqpsnce khykn qlb oujdxpq pxrd jzxjuxr tij
qss mqirowz ijjswjm jjer utwn kuedqxx bxshuok qkfag dmfwcr
jgln zdohd xitfbge xbokj xxeuv wqhvhjo erg cua fhc mhwy
euo ousht ipxt tpzq vnbmlo wvbjpb yjg bwpjbv nzvsea aerhsqv
axhmi bcf zdx vplso xhmai qsk psolv
ydnpmyo pfba zmo nat ykwxvm ydnpmyo rtd uuvqqr hcfccbd rtd
ytp guw ydmyf rww oucmpf gemhpj labc
edpbefn awgg qzpe aat cupig
mmi ghdaoh ibx fbyj gge vmmssen nplt mmqcra omcvm uwa fxypxfc
kjaw mtijne cfmsigd zwcjjd ajxjlqr tbp bnilc
fse ele vcsyiv bfe udny vznrao mgrjfgw
hadl nikvvpf gmdg bkmgt ugj
xkis qmr cgz nresp gms zrii coxkke vfsqiil
wmicbf bkk wcwklfg vpcbeg kfmjab vabc dax tnao tnao fvvzeyq fqm
bct tvj tra soo stqao kqua ikupoy wulcu nauxkkb pvqxy bfu
wpz txdduxq gaehfki kxo lvjzpxu iqon swr eyihl nbbec
fuphnbj bdtz huwu zdtb ilgzpa uyaut vpy viff tuuya
cvusbh bgy apsao qsupha
jtzlbd ljfvh wkjrw xsah sef jygb pqym zbcwok zdmug qpym
hbibuax iorqc dqjrs daeb iorqc qiw sagyt rkc sagyt khbr
shz mgn pqrdbm jvace gfhnq ann zosq wdwzmuf kswsg dzt brlavyo
qiw cdvwds dckpruy pybjra lfvgfn cwj bajtud pojehb rzrzvwe
txfyk zkgeeu zkgeeu zkgeeu wskcv nccoz
eettnxq gbgr uiqonyz wqtgs ozfjbn gbgr
svd thmmr rbbtxn sxkq isxlnhf tamdlbe bqrgvu nmpvlkc spko
qmn rspbjme ikjddkq kdb ugpegi egipgu
ufffijo revqpep zfw kwd pnya blqo rnntzx anpy
piaeyf vbeye uuqd vbeye
hamd hap ekk lgla twto
isniinr crz sjpmfxn uskwj
lzeofk tavbq ijcglqy lvy jliqcyg lwlip
uhyyyw itlrf tdc iabeocv jzwnjh vqxll nefze pyrxmx eispxnm hzlksce
ucuh mlam bhyej rgzkew ctbo iswqnvg
ytmb toppqgp ytmb gqgpr gqgpr vps ebv
eavn atkqltv bjvojs kaskr vqltakt uiktr xglc eyb rkkas fhnf eaorqm
jmfipc ujggeh hdxpfa xtab ydkibi ycxn ujggeh icheh vpznael oprbf
xazqxg khlemu awh uwz vhnixk vdcty hkk
gcl kayi hfozask grpseyn zviy tzoum qywnr wqkhq
ctrrcpw wqfbylp wqfbylp wqfbylp
gtk lqohf hqeaku mdj zrfkmxn bcqgf msing
luhpel kexokpx vojap ldaexs bbbtz
oimnqb esg zyjmbfh dfyhcf khpo zjtgm yelztbs ugj zjtgm mxro xyfxpk
dgtsu vvk wwfugbx aai zlxab beyxcg bpx chc bnxui
irrwbo orwibr lqt qtl tqknh
ihjsg ihjsg powwy pycyqo ihjsg
xdcu outh fnqrc eihkss bdylm sjunib eihkss
jpnw ycimse rffu ismyce uhxl feai
yyodnh dvwshkx vulh pvxj ydhyno hyodny
vuuweg pfguvyu orhei orhei wrm amkr xecja lmnveth
wriwe xgtnvj tdmxf gadtqh bezjvz lifu
euft tchbm xmtlwji tchbm
cfi zudn zludl pwiu axe psed
dbtfwf ajxcudj uaxdjcj dxuajjc zouyy
fmycmej bqhe jyfecmm kkrv kcdvjoy
grtb uzs rkxzt hivhic brtg hwyc lsl iivhch qbcp
ymn xfpka hqm sldz dblvsoe
qrcapma hntgmy difrkpk difrkpk xlsph
flvqh akcw boxrz ywhq boxrz esnxzv boxrz
zrvh jskaw mfs fkj
abveb qxfnlfq abveb kbwiyvd abveb
pgarl nbfrenx rnxgx bdlkix liltdm dzcokeg fubupcg iwp xfayp obfaz nevfw
nuhvaci blyv fcsp adlanka sjy syj ysxl
avwakn dkoya yzuszuk lqrr oqfyd dmgbhd lqrr
pxa mcvtoug nlweso yffqc dtuagcd ovvrkz ggfhw wnlseo bpqbn ohxzs rxzo
djkcl kbgyfir ogquot uoqotg jtmyd ohudvle xrnbt yvsln wykqt hntc xlrhqrb
ykt tkxfmd exas kty
zebstke msbbndq itmli ubexmht vekvd xbmb iajbj wac sta
ptdg oftwo goiulah tfmsrqs jffxvnv ozaluj qlhqjy wyffa
xeq ezmlpw xgno xorvfo yzq vwif wsi
hdove hqbzhu pjrxlj uafuh rizlb advmkca
jzk ddoisdh tfjh yuvikps ixpkf hnu
kixa djx uksr ogxty dxj clda ukrs
xgiy diwbvn vphdbg qnelyz tqptqig lenyzq ecsswj
alx awj fpasmmg zukuh qaanvb too nvskuk too gnria
suo suo brw nazq suo dqv
tan uxiz oqa xyezcd lsaicjr bosiak rmmh
bidpomf dimcj qekero wbrc lewt kmgmlao
bciacj eye lxfpef cbdshd dhdsbc qwnhil iuokc
zduefht lrgfjn nclksm wpjpjr hkeqd oprsjcw
chhdr bram swdfjr yikqra xkzsloc otptp agec hhdrc uofljf toppt wpbyrwo
bwlpb nishr knnrysj bvr ftnb iedskch weo
czo hsfp wblh cru kzalun intt
jvob rppz rkwv hgyhrqg
sgo hued jnygge izf ztan kjgpcn fagff jsi ijcxzoi tgqjjp tgqjjp
ltjq zidjy rfmy yevuaa nlhfyg xytdtle wsqvzzx wfflboo nawhv golhf xhsti
bmtzlml xcbsquq vnfsux voep lkss ioim
ntfffh gcncwu mmymn wkwlswa gcncwu iaeyumz
kcgdm rbaau cwsoya pznnnn xzz zbbdlhw zxuelq xzz pjeq
xrmnuct kwvykx khxr ioua xnmtrcu xrnctum ujq imnt ecee
xjsgx fby fby fby ggtpgdm jqvuj qshewki tkml ymsazcq
sdbyhwg kewtrte novhdcp wbuaoh dtytgtx zez whygbds hpg
tjvaqo yrycda yrycda ldbp yrycda
kloi tmsocmx dza sqtxc wgevs zlevs vtm
ftnx drvdm ryjfdgw nerynh cwfjpa mddvr
wsqjyn svg ncw aesn hvuq vybajti aesn bql atxhp ipu
eye romgxj gumuke jwi jrf dtt kcj wmg waw
ptltud oymklv fgnmbc ete apanovb vpt vyospi
clkguhu rbxs lxtnmy ferdx qbmrpg pvojnj zbcffbp
itngp dvtlq fzxp cxrf gbxxqp aafls pfe bpxgxq
nmikrui ddsq srfilr gnuvghu mwnacz nlbdm zcjm uylgev umzu mftz nmikrui
bow jmnxyen bow hvz
lksibxk lefzh lksibxk nkxsi nkxsi pldvhk
osjlzns pihvr zpeu zxjgjb xplykfk xplykfk
hajmfss cardd kaddjw uicfde taue
rgwdjra sgifh ggt mpzx usghkos oob fvzx ghnyxr sblcif
dtu gnihpry kjdpiny xvax itmluk fxvgaap bei xuq wzcy rhb hailtgo
wwob ueldq ueldq glxc umimwv onu dxhmhis ebottoa lnysfiu
zfbyi eyq etaj idpbkf
qshcfjb ozzqigv raztm ymcv sgivwoc kightf dcaglk udah fdm
jmxr jrcnck enffwfl jycc jmxr cylnigo enffwfl
bkslhv tykqw tykqw mbeqrbt tykqw
vogf nhqltpt nhqltpt vogf kpc
ryayz ddktu rfhkmx xok xninjcm ijcrw fxu
cmezfj zaamjrs whlcuoo mug lcaqhkb ymkdci qexa onhgk pgy
hcrcok qri fki wbiog ptj pmgtdt
xsl mpfxwbz bmzxpwf hrysu bmfxwzp xfja
gybzho ktokndy rzkbr jcnp ahicq weccg pgrodkt che vaglyn omhmpo
vdv bngjox srs faymg xrmf enseu aygfm gvsd
nuzi xodkbag eevovl bfjuv nuzi xmejqn
kcswegw bpa dgil insf insf
stg tklrut poi knurfpf
pcs dgirfie yep lvkfk ype hntt athvad clfybsq ofjhegj epy qwawns
wjtpgd wjtpgd vxnapp mwyfsm vxnapp rvcswcs jksa
ckzslrg wdzeimw cqhp nfgk zgukvd yyt tra erkx wdzeimw
hsww avl vkmzej hsww
mum oczj jfew rag zjoc wjfe yqynjqt cbkcsgo mri
vjhfqdi vjhfqdi npfa pzdmy utlyw bwvbfm nqdv iiap ygpky bwvbfm eocya
ewkqi ckb yviuro mqz vtrdam yzkqzv ppbj lhmj blkafo juxvwke lvewc
ljrewgx sutnb hfsavbu jofr ltml mjzkzz nmjii sutnb eonegt
cxzv nepyrb wmejdo vwqi aeqys
sbx fmne obzdz rdnfb gmb sbx ykcae hbzom ncwju rhpiao obzdz
lsgfun cbmfjwk fya ktzxbwt
ica bpsk bwjwkp obloxdx uwoqdo bnnhjuc tlsx qtaacp bdooxxl jamy ade
psus wmtkg ikvfx fkvesj upqlhfs ueje nyt abxvo
adlbl hzskbrp ooht nps
wtcgnvy nvqtvx tvgnycw ntvcygw kkxcp zyjmpbh
xfxww xsddqe ewvmgw qxqwy wpabtz ppe zuiw zubcc onaqii
kkaeec xhcakul wrrvi dtlqfy ahqdilw bnt gwimw espaivx nam yfv
lxz jtc nkwgz nbgsao olsck emtltf xidwcvm lcjxq
eav dzh hnbp hnbp yeg
egaq yvat kavsige csar zsi sptai
pofijc ibdnoe caoazp azlnjk dqp chik lowll iby gpvjv ohm
ors lexk zcneaj rmesx jman uqkb kvkq zfufmn
qgsyzxd hlm juerg ortfzw hxjzg
fxwy lcoc fyxw pzhynp yfn zdzrz
datmws ckwghgr gbtyf lqrpfgl mbgpd dyjilr fgybt hxpg
mxw facxdnu wxm urltwtf qfo wtpwrj
esa srypq jauwv dpm wdgqq hrke icvudq bdmubb ellhfjh ttpjjd gxmg
gvwvqwj cbzzuvj eckube adqinpa djutlue wcpw vrt ucqwu ekruwsn
fhj fst zmtb yhwk dxlbozs fcb vjvuxin dxlbozs rixdvu
egfoep cvq icd prwj icyg
aojaa ezmcuf udreyi bja cyrtpl wjl
gjeka bsbufp tbqqq vbmnqg sfqtgac odhq xzsxt
yse gujdr ugjdr sye
tax hntqw phf eixjwfh qkylnu nkyuql ugsuj
wyh egum zizhfc jrq htbyug lop dsu
exh vfdoosj ajrna jbiaz lqsgvks xklqgjv abtmdud
juqc ormfa sab tucsfln detqfo feg kifsion juqc ovhra
hvcrh oddhme omzmu vmy she xulvfa fecmgi
ayo gspge nkmy yblsj lrsre nkmy pwocjz gdexqqx ovovm
acy sqcz ijl htt yjsi rly vea bck
bniafe yore xnh rkcfd hxfuzw xlr nkzmmcs ekwggiu kgoboi wfuzxh hwfxuz
weq crkeq cccphe dtozviy kzkkdr yku cephcc ctq zbau dewpi
vfla rzpl bnmx uvggon foivrb fval
ziaove lawkpdn ddwl sxj krroj rqmffxv babb
bdw dsifr kuueet hugddwt piz dwb sjixveg kmsoknq
czl feyxf soyvbj tnmpjn kklwi akx nqepntc
nrmhc tkkn jrxgc jrxgc tkkn
ufzn mrhiapi qrme kjlf qrme xpp qrme loyzizz xqm coli
qvaoye mysv ydfxr iixrw
dql tqarux fxqfn haoinu lyati xml
kyve obatly dgfjt fjz sqrz xlbst lgwlt zovih aepy otrpl oifid
ymawam afgye lcnpkmv feilfws vonseh rxrdco
tqij kuawg dmova slds imdtb sjsafo ffkzzl pxxenva wuakg efbgx
yrwoaos vpw ijjpua jnbxl sev yvgdxzr mpqa vpe lboh sev
krwdtd uglxtcz mljcgdk lqj fgpfle nuui cqk exr nuu oyn
dwd nwt idhclm vgkh rpubq wybhapp
hskhgpy gzvz jztbr jwv vcx vdjmnjr jrsp
ikml ceuhcng biu zoo gra bnnforx abzan hwsmd lmki tsl yvogo
kqfc younaz azvgfz gesajr tmwxvyb vmcdu dclwh rfjwhic slfym
pbrhjml rsacryg jga qvgks neh fcq qmi mwb juezk mjteeg alkb
pcj ujstl fkrqm eeczrle hbkcvm upbo mrb qrspjt
jbq rrk xjl rgokbnx hor ogg szxqu hysy vqj piorq wtrtrdk
bnq ntvhcrf vrm puer kde xaxkja sfxgjf
pgcicus hqeqkkx xqekqhk qqkxhke
puquxi hmeaehh oxe tasipw qzyg hyvy wcmpwe
hvs fxq wvfy zjepsl dvrfxnc xnvg
xle crcuc qkhnv crcuc oedez bjw pmwq
xzzpiy cjwss jwscs apb bpa
ydjhhf yeltadb lwi cjdcb ovaox xrdm vkxub
zax xza admbc lvpzfeh auxn rwasj
kebx eild nrskdr meja jxczomh gcne"""
'''
arra = arra.strip().split()
anocount = 0
emp = []
invalid = 0
current = 0
print(len(arra)-len(set(arra)))
print(len(arra))
for z in range(len(arra)):
  emp.append(arra[z])
  if emp.count(emp[current])!= 1:
    invalid += 1
  if emp.count(emp[current])>2:
    print("uhoh")
    print(emp.count(emp[current]))
    invalid -= 2
  current+=1
  print(invalid)
'''
#----------------------------------------------------------------------------------------------------------------------
#DAY 5 PART ONE
"""
numarray = '''0
1
0
0
1
-3
0
0
2
-2
-6
-3
2
-5
-6
-3
-3
0
-8
-12
1
-9
-12
-9
0
-7
-17
-6
-18
-7
-6
-21
-28
-14
-23
-14
-17
-5
-35
-17
-26
-14
1
-27
-19
-40
-32
-44
2
-14
-15
-12
-35
0
-49
-12
-7
-46
-47
-32
-33
-47
-7
-62
-20
-35
-4
-35
-8
-3
-61
-38
-63
-27
-33
-57
-48
-66
-68
-11
-61
-50
-34
-31
-36
-79
-49
-71
1
-34
-65
-61
-91
-12
-21
-82
-85
-51
-89
0
-83
-53
-44
-7
1
-19
-39
-27
-94
-36
-31
-35
-97
-45
-90
-15
-106
-30
-79
-18
-25
-105
-30
-63
-109
-32
-91
-96
-87
-121
-116
-103
-71
-1
-113
-10
-47
-109
-107
-38
-66
-26
-8
-38
-31
-129
-42
-91
-89
-107
-125
-75
-118
-81
-45
-111
-27
-63
-106
-110
-64
-63
-80
-44
-33
-130
-55
-90
-144
-15
-132
-122
-155
-122
-94
-159
-5
-89
-6
-97
-129
-159
-15
-44
-156
-124
-113
-154
-95
-96
-29
-121
-30
-73
-118
-57
-76
-141
-138
-108
-185
-56
-136
-161
-138
-192
2
-126
-12
-39
-60
-125
-149
-193
-146
-116
-101
-16
-207
-122
-92
-204
-42
-112
-28
-93
-96
-57
-136
-19
-36
-107
-170
-19
-20
-96
-229
-59
-172
-58
-89
-31
-57
-223
-37
-189
-43
-135
-90
-150
-22
-152
-243
-37
-231
-112
-57
-168
-30
-77
-162
-181
-176
-202
-138
-206
-183
-190
-257
-181
-47
-23
-248
-114
-98
-77
-143
-168
-166
-30
-155
-237
-51
-113
-243
-41
-142
-231
-139
-20
-190
-262
-142
-238
-200
-270
-113
-35
-296
-146
-205
-129
-198
-68
-139
-56
-196
-133
-16
-229
-258
-91
-63
-249
-274
-156
-273
-182
-166
-115
-154
-296
-115
-89
-120
-201
-44
-287
-8
1
-260
-297
-282
-114
-323
-326
-166
-241
-109
-21
-236
-280
-19
-80
-77
-271
-292
-340
-300
-206
-308
-99
-156
-277
-245
-132
-56
-172
-53
-271
-32
-5
-235
-329
-1
-150
-247
-268
-133
-341
-221
-2
-43
-229
-190
-337
-40
-71
-72
-149
-25
-253
-44
-113
-164
-370
-284
-235
-9
-234
-291
1
-152
-302
-393
-47
-289
-75
-140
-349
-140
-353
-298
-27
-292
-380
-55
-62
-208
-221
-41
-316
-411
-367
-220
-248
-59
-177
-372
-55
-241
-240
-140
-315
-297
-42
-118
-141
-70
-183
-153
-30
-63
-306
-110
-8
-356
-80
-314
-323
-41
-176
-165
-41
-230
-132
-222
-2
-404
-38
-130
2
-16
-141
-136
-336
-245
-6
-348
-172
-267
-208
-291
-285
-67
-219
-216
-136
-325
-27
-382
-242
-50
-284
-149
-454
-336
-346
-293
-402
-76
-324
-219
-336
-24
-446
-123
-185
-196
-295
-173
-400
-137
-414
-14
-104
-62
-252
-17
-398
-490
-440
-89
-347
-101
-142
-228
-301
-396
-320
-52
-508
-122
-436
-311
-344
-240
-434
-220
-197
-31
-295
-44
-452
-269
-430
-373
-409
-438
-365
-13
-241
-418
-20
-24
-141
-1
-148
-307
-63
-423
-254
-8
-438
-326
-19
-135
-109
-394
2
-398
-273
-158
-453
-346
-86
-431
-536
-549
-379
-483
-85
-476
-483
-104
-87
-462
-249
-540
-164
-360
-100
-238
-45
-390
-59
-156
-248
-257
-150
-164
-160
-545
-520
-364
-384
-237
-456
-28
-366
-147
0
-303
-583
-420
-370
-299
-154
-380
-188
-491
-258
-598
-429
-349
-333
-569
-4
-556
-421
-182
-441
-407
-542
-364
-370
-384
1
-529
-45
-319
-395
-279
-160
-575
-193
-25
-565
-548
-445
-266
-304
-361
-348
-303
-159
-39
-75
-437
-608
-622
-556
-108
-343
-283
-68
-632
-393
-68
-140
-126
-531
-87
-519
-334
-56
-70
-275
-247
-370
-439
-118
-497
-630
-594
-612
-541
-161
-646
-397
-100
-284
-313
0
-59
-200
-601
-663
-529
-676
-610
-7
-228
-50
-494
-382
-250
-306
-274
-163
-110
-375
-124
-237
-98
-645
-692
-495
-593
-647
-178
-531
-336
-697
-646
-671
-633
-542
-461
-200
-658
-525
-389
-643
-258
-329
-656
-400
-692
-557
-506
-594
-67
-623
-113
-459
-211
-713
-115
-602
-131
-181
-30
-227
-53
-719
-631
-641
-434
-552
-716
-368
-19
-439
-443
-552
-85
-79
-449
-254
-620
-474
-121
-210
-285
-608
-456
-513
-496
-13
-418
-399
-437
-258
-15
-623
-178
-336
-379
-721
-299
-729
-742
-64
-13
-438
-603
-666
-278
-767
-200
-686
-497
-256
-541
-491
-360
-615
-326
-682
-759
-524
-580
-323
-578
-793
-478
-107
-440
-657
-790
-605
-21
-163
-392
-560
-336
-430
-613
-182
-15
-782
-607
-281
-269
-25
-699
-89
-593
-280
-269
-438
-103
-359
-387
-157
-747
-619
-176
-772
-500
-735
-691
-797
-612
-573
-36
-617
-630
-357
-718
-210
-48
-185
-20
-556
-206
-722
-559
-416
-578
-745
-564
-273
-62
-300
-218
-711
-744
-805
-277
-522
-346
-280
-762
-438
-381
-379
-198
-737
-555
-466
-218
-511
-334
-353
-259
-225
-675
-350
-585
-647
-52
-395
-324
-106
-826
-279
-81
-396
-611
-312
-529
-291
-129
-594
-437
-188
-649
-820
-237
-673
-6
-387
-195
-503
-350
-83
-88
-626
-30
-313
-13
-633
-403
-319
-832
-185
-146
-839
-9
-557
-799
-841
-700
-465
-669
-769
-235
-849
-863
-819
-76
-912
-931
-909
-762
-607
-522
-64
-769
-377
-133
-414
-772
-206
-746
-730
-393
-901
-72
-33
-811
-372
-298
-835
-637
-302
-481
-958
-878
-867
-25
-260
-448
-21
-930
-903
-581
-547
-664
-843
-140
-337
-383
-513
-368
-221
-474
-169
-673
-728
-266
-862
-753
-815
-647
-106
-15
-728
-912
-147
-828
-6
-694
-434
-737
-335
-183
-732
-841
-364
-155
-116
-966
-822
-65
-22
-853
-208
-326
-826
-472
-491
-436
-771
-1009
-98
-401
-915
-275
-574
-313
-884
-648
-935
-94
-326
-553
-744
-723
-782
-719
-175
-868
-190
-153
-48
-218
-414
-721
-715
-995
-991
-575
-264
-70
-366
-381
-130
-409
-817
-258
-1028
-552
-878
-449
-138
-900
-45
-119
-677
-844
-869
-985
-1019
-60
-649
-915
-93
-1053
-121
-631
-156
-332
-193'''
numarray = numarray.strip().split()
print(len(numarray))
currentnumb = 0
numarray = list(map(int, numarray))
escaped = False
attempts = 0
while escaped == False:
  try:
    if numarray[currentnumb] >= 3:
      numarray[currentnumb] -= 1
      currentnumb += numarray[currentnumb]+1
      attempts+=1
    elif numarray[currentnumb] <3:
      numarray[currentnumb] +=1
      currentnumb += numarray[currentnumb]-1
      attempts += 1
  except:
    escaped = True
    print(attempts)
"""
#DAY SIX PART ONE AND TWO
"""
empty = []
maxval = 0
array = [2,8,8,5,4,2,3,1,5,5,1,2,15,13,5,14]
count = 0
notfound = True
z = 0
while notfound:
  z+=1
  maxval = np.argmax(array)
  numcount = maxval
  for x in range(0, max(array)):
    try:
      array[numcount+1] += 1
      array[maxval]-=1
      numcount +=1
      count+=1
    except:
      numcount = 0
      array[numcount] += 1
      array[maxval]-=1
  number = copy.deepcopy(array)
  empty.append(number)
  for f in range(len(empty)):
    if empty.count(empty[f]) is not 1:
      print("found!: ", z)
      print(f)
      notfound = False"""
      
#DAY 8 PART ONE 

c = 14
c+=1 i
