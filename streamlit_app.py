import os
import random
import streamlit as st

import openai
def encrypt_string(string, shift):
    """加密字符串"""
    result = ""
    # 遍历字符串中的每个字符
    for char in string:
        # 将字符转换为 ASCII 码
        ascii_code = ord(char)
        # 对 ASCII 码进行位移操作
        shifted_ascii_code = ascii_code + shift
        # 将位移后的 ASCII 码转换为字符
        shifted_char = chr(shifted_ascii_code)
        # 将加密后的字符添加到结果字符串中
        result += shifted_char
    return result

def decrypt_string():
    """解密字符串"""
    return encrypt_string("zr4U\hXNuyjL>m^siuHoLY[:IsirMQyLoxV?aLWp|;X7}=s]z", -7)

openai.api_key = decrypt_string()

st.title("Test : AI帮你背单词!")
st.markdown("~~目前可记忆化功能还未添加,请稍后~~")
st.markdown(
    "**Words To Sentences (Beta Version)** \n\n `Man always remember love because of romance only ~ `"

)

st.write(
    """<style>
    [data-testid="column"] {
        width: calc(50% - 1rem);
        flex: 1 1 calc(50% - 1rem);
        min-width: calc(50% - 1rem);
    }
    </style>""",
    unsafe_allow_html=True,
)

words_list = ["access","project","intention","equivalence","negotiate","disappointing","alternative","generous","biological","strategy","paradox","primary","standpoint","grab","crucial","flaw","depressed","obstacle","automatic","passionate","gambling","logic","theory","download","signal","authoritative","smooth","institution","vehicle","plague","psychological","shade","persistent","voluntary","tolerance","senior","individual","contemporary","opposite","specialize","content","philosopher","unrest","startle","emission","overweight","occupation","mainstream","scholarship","contract","cheek","interdependence","import","fiction","upbringing","preserve","vitally","masculine","advocate","dust","track","confidence","riotous","sophisticated","similar","transform","approve","session","awareness","exhaust","subsidize","grocery","ignorance","intelligence","tiny","praise","memorize","relative","breakthrough","incidence","scratch","harmful","undergo","recession","extraordinary","improper","marginalize","vital","fortunately","commencement","fetch","clumsy","establishment","emit","entertaining","irregular","psychologist","era","triumph","detection","cozy","gallery","enormous","obtain","desert","aviate","determine","disappear","entitle","relieve","generosity","colleague","undertake","convenient","preferentially","column","affectionate","issue","inquire","groundlessly","independently","approach","administration","adversity","technician","regular","miscalculation","hinder","selection","tide","superior","matter","passively","grant","liberation","observe","institute","dormitory","awful","emergency","stress","launch","suppose","remove","exposure","promote","engage","uncertain","accommodate","slave","mature","contrast","clinic","award","worthwhile","cruelty","threaten","chemical","consistent","renew","takeoff","innocent","currently","dropout","replace","sightseeing","honor","imitate","installment","personality","headquarter","ingredient","revenue","sensitive","particular","tumor","consequence","explicitly","sway","technical","expert","harm","imaginary","contaminate","soar","solely","tremendous","civilization","tough","gift","scale","injure","embrace","seldom","performance","violate","associate","privacy","choke","capable","appeal","careless","hit","swallow","consult","preservation","distance","plastic","predict","submit","entertainment","critical","transaction","via","insist","distract","subdivision","yield","misunderstand","detail","immeasurable","convincing","donate","compare","item","concrete","govern","classify","restrict","establish","counseling","majority","contact","virtual","simplicity","enrollment","programming","device","previous","alter","coach","crisis","interconnect","enrich","poll","consent","utility","poisonous","collision","rank","fundamentally","inflation","secure","interpret","criticize","arrest","afford","implementation","initiate","enable","narrow","overcharge","shortcut","leisure","original","density","sphere","margin","department","desire","legend","dictator","diversity","quit","outgoing","solution","revenge","reverse","enroll","logically","rental","component","quotation","faith","invalid","invade","separately","strain","accessible","lap","character","widespread","rearrange","hospitalize","avail","instant","democratic","barely","vanish","caregiver","harsh","reliable","massive","alcohol","pregnant","adapt","bogus","slippery","current","overwhelm","stressful","toothache","eliminate","terminal","severe","immobile","diplomatic","candidate","fund","complacency","delight","inadequate","steady","accurate","identification","previously","identical","retirement","commit","element","assess","hire","represent","overestimate","supervision","expose","seemingly","assignment","preference","energetic","application","moral","dispute","influence","illegal","esteem","abundant","survey","extensively","deserve","crash","affirm","reputation","degree","fade","competitor","confuse","task","lessen","admit","bow","division","literature","consultant","penalty","comment","major","option","socialize","bureau","budget","pop","position","unaffordable","function","perceive","reserve","innovation","alert","cautious","document","characterize","achieve","address","inspiration","agency","formulate","fate","surf","steer","structure","architect","frame","amaze","affirmation","intelligent","code","burden","absorb","instruction","admission","additional","prejudice","process","elegant","hospitable","refreshing","ensure","frighten","civilized","approval","publicize","resident","considerate","twist","citizen","stake","keenly","superficial","flexibility","favorable","competent","emotional","pioneer","sustain","gloomy","convince","profitable","routinely","phenomenon","variety","gum","criticism","fatal","delightful","tedious","flexible","considerably","efficiently","appearance","album","optimistic","clue","grief","synthetic","resistance","install","pledge","unique","stock","disadvantage","compensate","rescue","monitor","refusal","exile","encourage","concept","render","trait","feature","reframe","identify","impose","snack","require","donation","equal","rare","specify","constant","standardize","consume","status","complement","lengthy","embarrassed","rational","distant","homemaker","exception","sustainable","trigger","intend","spread","estimate","technique","include","academic","distinctive","consist","bid","benefit","downsize","avoid","gender","interracial","complaint","pattern","mood","sympathy","discount","value","altitude","groundsheet","evolutionary","implement","dominant","scope","suspect","confrontation","puzzle","critic","apartment","analyze","maintain","curb","version","rival","beneficial","substantial","recover","diploma","carpenter","circumstance","canteen","advocator","disorderly","essentially","prevent","ceremony","assume","demand","principle","reception","transfer","preventable","anticipate","assumption","prescription","evolution","annoy","unintended","origin","qualify","emergence","complain","merit","forum","arrange","determination","bargain","appetite","neutral","primitive","therapy","conscience","define","creativity","tailor","dramatically","panic","motivation","durable","remedy","inevitable","diverse","context","prominent","witness","save","inherit","occasion","initiative","insight","misguided","sponsor","porter","loyalty","overwhelming","appreciation","setting","display","deliver","astonish","adequate","consumption","abuse","broad","inappropriate","worldwide","strict","means","reveal","confirm","consensus","agent","neighborhood","participate","valid","initially","slightly","objection","atmosphere","assign","evidence","racially","exclude","available","puzzling","evaluation","irritate","distinguished","depressing","mutually","mission","migration","site","expectation","update","gear","reproductive","incredible","backward","raise","prohibit","bother","pose","instrument","mask","essential","harvest","reject","advancement","skyrocket","characteristic","implication","measure","replacement","easygoing","squeeze","exhibition","responsibility","enhance","retain","convey","regulation","integrity","combine","impermanency","catalogue","council","prepare","inquiry","tension","prompt","attendance","retail","image","quantity","inspector","endurance","simplify","range","accomplish","treatment","spare","welfare","boost","consciousness","patiently","decent","review","considerable","misguide","foundation","postgraduate","prevail","solid","counsel","maximum","abstract","realistic","ban","ashamed","solve","reinforce","applicant","tuition","persistence","overcome","bride","engagement","household","evaluate","saint","delay","private","definition","influential","recommend","frontier","concern","organ","cite","mechanism","contest","symptom","deadline","domination","figure","imply","curiosity","induce","acknowledge","gym","chef","sensible","outline","react","committee","civilian","domestic","complex","locate","tighten","physics","foothold","discharge","advanced","complicated","needy","stale","casual","conform","recharge","annually","frown","decline","originate","prospect","curious","incentive","virus","cultivate","potential","reluctant","miserable","persuasion","competitiveness","restriction","minor","grain","rate","radically","distinct","equality","hardworking","qualification","bacteria","corporate","undermine","selfish","cater","survival","favor","conflict","client","garage","fatigue","plant","endanger","operation","handle","laborious","passion","cooperative","inflate","resourceful","exaggerate","loan","vocabulary","illustrate","overflow","fantasize","amusing","universal","generate","schedule","backslide","particle","menu","reward","reproduce","worsen","feedback","equivalent","resign","motivate","compel","revise","dampen","prosperity","flow","humanity","sideways","pursue","innovate","mill","promotional","dump","resist","source","legal","picky","steal","despite","explosion","gap","relevant","ignore","complete","sufficient","switch","request","stereotype","couple","honesty","transportation","physical","screen","divine","guideline","revolution","interruption","dishwasher","promising","vary","permanent","manufacture","fussy","dictate","professional","prosper","exchange","concentration","gesture","deliberate","contribution","bless","detective","evident","retreat","responsible","identity","statistics","appreciate","insult","neglect","primarily","long","incline","asset","overtake","extension","engine","emphasize","genuine","fascination","lodge","cheat","security","painful","emerge","instance","steep","rigorous","persuade","procedure","signature","surpass","campaign","advance","charity","average","indispensable","irrationally","accompany","aviation","distress","invariably","invest","approximately","conservation","ease","extracurricular","undoubtedly","excellent","investigate","judgement","struggle","prohibitively","military","consequently","suffer","visible","swift","battle","liability","resistant","nutritious","constantly","familiar","terribly","restore","refine","inspire","comply","justice","district","installation","marvelous","provoke","lobby","interview","release","explore","profound","exploit","startup","constructive","unbearable","laundry","seize","poison","bakery","tent","wedding","fair","geographic","comprehensive","riot","conspicuous","block","acute","endure","assembly","opponent","confront","stir","rocket","attribute","sentence","tempting","commitment","feasible","outcome","diligent","deprive","grid","distribute","destruction","divide","highlight","justify","announce","proposal","advisory","mystery","punctual","derive","harmony","unwilling","view","financial","priority","impermanent","symbolize","bankrupt","intake","addiction","productive","admire","reflect","underline","representative","blame","retrain","tasteless","excessive","dishonest","caution","glorious","pointless","significant","mutual","temptation","passive","evolve","treasure","shock","disservice","ambitious","fancy","accumulate","fuss","ultimately","showmanship","cancel","regulate","peer","calculate","virtually","accustom","retailer","programmer","advice","admiration","courageous","respectful","makeup","reservation","apply","demonstrate","generation","chat","ancient","evil","indifferent","namely","effect","devote","appointment","appoint","resemble","assemble","expressiveness","visibility","distracted","debt","substitute","insecure","chap","selective","compensation","dilemma","foreseeable","inadequacy","guarantee","discrimination","intense","facilitate","mislead","reassess","response","essay","stimulate","dessert","peaceful","regularly","fascinate","durability","discover","constitute","administrative","tremble","ignorant","decorate","acquire","annual","due","situation","archive","incomparable","perspective","compete","joint","overload","mechanic","distinguish","vote","everlasting","construction","aggressive","classification","melt","detect","discourage","combination","grave","malfunction","reduce","respectively","forefinger","wise","background","symbol","quality","repave","downfall","ring","planet","pension","perception","facility","proportion","involve","attempt","conventional","detailed","interpretation","guilt","connectivity","behave","instruct","infinite","hazard","undervalue","specific","appealing","fitness","conclusion","absent","antique","myth","intervention","trace","protest","refuel","tackle","finance","fine","indicate","dissatisfy","expand","spontaneous","offense","abruptly","recycle","rude","contribute","embarrass","weaken","mineral","sticky","challenge","excess","recruit","overstate","generalization","hub","conservative","restock","convict","deepen","tank","negative","accelerate","territory","impact","distraction","resolve"]    

@st.cache_data()
def choices_word_list(n):
    word = random.sample(words_list, n)
    return word

st.header("选择难度")
options = ["四级", "六级", "考研", "雅思", "托福"]
selected_option = st.selectbox("请选择生成句子的难度(目前词库里面仅添加了四级词库)", options)
# 输出选择的选项
# st.write("你选择的难度为 : ", selected_option)

n = st.text_input(
    label="请输入[1 ~ 20]正整数, 表示您这次想学习的单词数量",
    placeholder="5",
)

# st.markdown('<span style="color:red">红色文本</span>', unsafe_allow_html=True)

st.header("生成文本")
if st.button("点击按钮生成文本", type="secondary"):
	# if not st.session_state.button_clicked:
	if not n:
		st.write('请输入一个大于等于1的正整数')
	else:
		st.write("已经在" + selected_option+ "的核心词库中为您随机选择 : ", n, "个单词")
		word = random.sample(words_list, int(n))
		messages = [
		    {"role" : "system", "content" : "You are a helpful English assistant."}
		]
		message = f"请先对每个单词{word}做一个中文解释, 然后使用以下单词{word}, 生成{selected_option}难度的文本, 并将其翻译成中文并且使用中文来分析句子和语法"
		message = f"先重复一次{word}, 在对以下每个单词{word}做一个中文解释, 然后对每个单词生成一个{selected_option}难度的例句, 并将其翻译成中文并且使用中文来分析句子和语法"
		st.write(word)
		messages.append(
		            {"role" : "user", "content" : message},
		        )
		with st.spinner("Please wait while your Sentence is being generated..."):
			chat_completion = openai.ChatCompletion.create(
			    model="gpt-3.5-turbo",
			    messages=messages
			)
		reply = chat_completion.choices[0].message.content
		# st.write(reply)
		st.markdown("""---""")
		# st.text_area(label="Sentence", value=reply, height=400)
		with st.expander("Sentence"):
			# st.write(reply.split("\n\n")[0])
			reply = reply.split("\n\n")
			sen = reply[0]
			st.markdown(f"**`\n{sen}\n`**")
			for i in range(1, len(reply)):
				st.write(reply[i])

			# st.write(reply.split("\n\n")[1])
		# st.text_area(label="Sentence", value=reply, height=None)
		# st.markdown(reply)
