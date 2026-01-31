import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
TOKEN = "8376724678:AAE7fOM2hxZDXyvYFyN4ZfEeGvBbq1DJY_s"
import random
import threading


bot = telebot.TeleBot(TOKEN)

ADMIN_ID = 8089061362

users_data = {}

questions = {
"Beginner": [
    {
        "q": "I ___ a teacher.",
        "options": ["A) are", "B) is", "C) am"],
        "answer": "C"
    },
    {
        "q": "She ___ a doctor.",
        "options": ["A) isn’t", "B) not", "C) don’t"],
        "answer": "A"
    },
    {
        "q": "This is ___ orange.",
        "options": ["A) a", "B) an", "C) the"],
        "answer": "B"
    },
    {
        "q": "He is ___ engineer.",
        "options": ["A) a", "B) an", "C) the"],
        "answer": "B"
    },
    {
        "q": "They ___ in London.",
        "options": ["A) live", "B) lives", "C) living"],
        "answer": "A"
    },
    {
        "q": "I ___ like tea.",
        "options": ["A) don’t", "B) doesn’t", "C) not"],
        "answer": "A"
    },
    {
        "q": "This is ___ book.",
        "options": ["A) mine", "B) my", "C) me"],
        "answer": "B"
    },
    {
        "q": "Is this pen ___?",
        "options": ["A) your", "B) yours", "C) you"],
        "answer": "B"
    },
    {
        "q": "___ a cat in the room.",
        "options": ["A) There is", "B) There are", "C) There"],
        "answer": "A"
    },
    {
        "q": "___ three books on the table.",
        "options": ["A) There is", "B) There are", "C) There"],
        "answer": "B"
    },
    {
        "q": "The keys are ___ the bag.",
        "options": ["A) in", "B) on", "C) at"],
        "answer": "A"
    },
    {
        "q": "The picture is ___ the wall.",
        "options": ["A) in", "B) on", "C) at"],
        "answer": "B"
    },
    {
        "q": "___ she a student?",
        "options": ["A) Do", "B) Are", "C) Is"],
        "answer": "C"
    },
    {
        "q": "___ you like pizza?",
        "options": ["A) Is", "B) Does", "C) Do"],
        "answer": "C"
    },
    {
        "q": "How do you write the number 15?",
        "options": ["A) Fifteen", "B) Fifty", "C) Five"],
        "answer": "A"
    },
    {
        "q": "The plural of 'cat' is:",
        "options": ["A) Cats", "B) Caties", "C) Cates"],
        "answer": "A"
    },
    {
        "q": "___ is my brother.",
        "options": ["A) She", "B) He", "C) It"],
        "answer": "B"
    },
    {
        "q": "___ is my house.",
        "options": ["A) Those", "B) These", "C) This"],
        "answer": "C"
    },
    {
        "q": "I go to school ___ the morning.",
        "options": ["A) in", "B) on", "C) at"],
        "answer": "A"
    },
    {
        "q": "She ___ a new phone.",
        "options": ["A) have", "B) has", "C) having"],
        "answer": "B"
    },

],
   "Elementary": [
    {
        "q": "She ___ to school every day.",
        "options": ["A) go", "B) goes", "C) going"],
        "answer": "B"
    },
    {
        "q": "They ___ like coffee.",
        "options": ["A) don’t", "B) doesn’t", "C) not"],
        "answer": "A"
    },
    {
        "q": "He ___ to the park yesterday.",
        "options": ["A) go", "B) went", "C) goes"],
        "answer": "B"
    },
    {
        "q": "We ___ the movie last night.",
        "options": ["A) didn’t watch", "B) don’t watch", "C) doesn’t watch"],
        "answer": "A"
    },
    {
        "q": "I saw ___ elephant at the zoo.",
        "options": ["A) a", "B) an", "C) the"],
        "answer": "B"
    },
    {
        "q": "___ sun is shining today.",
        "options": ["A) A", "B) An", "C) The"],
        "answer": "C"
    },
    {
        "q": "How many ___ are there?",
        "options": ["A) apple", "B) apples", "C) apple’s"],
        "answer": "B"
    },
    {
        "q": "There isn’t ___ water in the bottle.",
        "options": ["A) many", "B) much", "C) a"],
        "answer": "B"
    },
    {
        "q": "Is there ___ milk in the fridge?",
        "options": ["A) some", "B) any", "C) a"],
        "answer": "B"
    },
    {
        "q": "I have ___ books on my desk.",
        "options": ["A) some", "B) any", "C) a"],
        "answer": "A"
    },
    {
        "q": "The cat is ___ the table.",
        "options": ["A) in", "B) on", "C) at"],
        "answer": "B"
    },
    {
        "q": "We have a meeting ___ Monday.",
        "options": ["A) in", "B) on", "C) at"],
        "answer": "B"
    },
    {
        "q": "She wakes up ___ 7 o’clock.",
        "options": ["A) in", "B) on", "C) at"],
        "answer": "C"
    },
    {
        "q": "He ___ play the piano.",
        "options": ["A) can", "B) can’t", "C) cans"],
        "answer": "A"
    },
    {
        "q": "I ___ speak French.",
        "options": ["A) can", "B) can’t", "C) could"],
        "answer": "B"
    },
    {
        "q": "They ___ football now.",
        "options": ["A) play", "B) are playing", "C) plays"],
        "answer": "B"
    },
    {
        "q": "She ___ reading a book now.",
        "options": ["A) isn’t", "B) don’t", "C) doesn’t"],
        "answer": "A"
    },
    {
        "q": "The movie was very ___.",
        "options": ["A) bored", "B) boring", "C) bore"],
        "answer": "B"
    },
    {
        "q": "This bag is ___ than that one.",
        "options": ["A) heavy", "B) heavier", "C) heaviest"],
        "answer": "B"
    },
    {
        "q": "This is ___ car.",
        "options": ["A) Tom’s", "B) Toms", "C) Tom"],
        "answer": "A"
    },
    # {
    #     "q": "___ do you live?",
    #     "options": ["A) What", "B) Where", "C) When"],
    #     "answer": "B"
    # },
    # {
    #     "q": "___ is your teacher?",
    #     "options": ["A) Who", "B) Where", "C) What"],
    #     "answer": "A"
    # },
    # {
    #     "q": "We ___ at home yesterday.",
    #     "options": ["A) was", "B) were", "C) are"],
    #     "answer": "B"
    # },
    # {
    #     "q": "They ___ a big house.",
    #     "options": ["A) have", "B) has", "C) having"],
    #     "answer": "A"
    # },
    # {
    #     "q": "She ___ goes to the gym.",
    #     "options": ["A) always", "B) never", "C) ever"],
    #     "answer": "A"
    # },
    # {
    #     "q": "You are happy, ___?",
    #     "options": ["A) aren’t you", "B) are you", "C) do you"],
    #     "answer": "A"
    # },
    # {
    #     "q": "I ___ my teeth every morning.",
    #     "options": ["A) brush", "B) wash", "C) clean"],
    #     "answer": "A"
    # },
    # {
    #     "q": "You buy food in a ___.",
    #     "options": ["A) library", "B) kitchen", "C) supermarket"],
    #     "answer": "C"
    # },
    # {
    #     "q": "I saw her ___ weekend.",
    #     "options": ["A) last", "B) next", "C) every"],
    #     "answer": "A"
    # },
    # {
    #     "q": "___ the door, please.",
    #     "options": ["A) Open", "B) Opening", "C) Opens"],
    #     "answer": "A"
    # }
],

  "Pre-Intermediate": [
    {
        "q": "I ___ never ___ to Paris.",
        "options": ["A) have, been", "B) has, been", "C) have, went"],
        "answer": "A"
    },
    {
        "q": "She ___ finished her homework yet.",
        "options": ["A) hasn’t", "B) haven’t", "C) didn’t"],
        "answer": "A"
    },
    {
        "q": "They ___ TV when I called.",
        "options": ["A) watched", "B) were watching", "C) are watching"],
        "answer": "B"
    },
    {
        "q": "While I ___ , the phone ___.",
        "options": ["A) was reading, rang", "B) read, rings", "C) was reading, rings"],
        "answer": "A"
    },
    {
        "q": "If it ___ tomorrow, we will stay home.",
        "options": ["A) rains", "B) rain", "C) raining"],
        "answer": "A"
    },
    {
        "q": "If you ___ hard, you ___ the exam.",
        "options": ["A) study, will pass", "B) studies, pass", "C) studying, will pass"],
        "answer": "A"
    },
    {
        "q": "This book is ___ than that one.",
        "options": ["A) interesting", "B) more interesting", "C) most interesting"],
        "answer": "B"
    },
    {
        "q": "She is the ___ student in the class.",
        "options": ["A) good", "B) better", "C) best"],
        "answer": "C"
    },
    {
        "q": "I ___ live in a village when I was young.",
        "options": ["A) use to", "B) used to", "C) using to"],
        "answer": "B"
    },
    {
        "q": "He ___ like coffee before.",
        "options": ["A) didn’t use to", "B) doesn’t use to", "C) not used to"],
        "answer": "A"
    },
    {
        "q": "I went to the shop ___ some milk.",
        "options": ["A) buy", "B) to buy", "C) buying"],
        "answer": "B"
    },
    {
        "q": "She is good ___ singing.",
        "options": ["A) at", "B) in", "C) on"],
        "answer": "A"
    },
    {
        "q": "I’m waiting ___ my friend.",
        "options": ["A) to", "B) for", "C) at"],
        "answer": "B"
    },
    {
        "q": "Have you got ___ time to help me?",
        "options": ["A) some", "B) any", "C) a"],
        "answer": "B"
    },
    {
        "q": "How ___ books do you have?",
        "options": ["A) much", "B) many", "C) a lot"],
        "answer": "B"
    },
    {
        "q": "There is ___ water in the bottle.",
        "options": ["A) a few", "B) many", "C) a little"],
        "answer": "C"
    },
    {
        "q": "You can swim, ___?",
        "options": ["A) can’t you", "B) can you", "C) don’t you"],
        "answer": "A"
    },
    {
        "q": "We ___ to London tomorrow.",
        "options": ["A) go", "B) are going", "C) went"],
        "answer": "B"
    },
    {
        "q": "She ___ a letter yesterday.",
        "options": ["A) write", "B) writes", "C) wrote"],
        "answer": "C"
    },
    {
        "q": "He drives ___.",
        "options": ["A) careful", "B) carefully", "C) more careful"],
        "answer": "B"
    },
],

  "1A": [
    {
        "q": "“Xayr” (rasmiy) ni koreys tilida qanday aytish mumkin?",
        "options": ["A) 안녕히 가세요 (Annyeonghi gaseyo)", "B) 네 (Ne)", "C) 안녕하세요 (Annyeonghaseyo)"],
        "answer": "C"
    },
    {
        "q": "“Mening ismim [ism]” ni qanday aytish?",
        "options": ["A) 어디 사세요? (Eodi saseyo?)", "B) 제 이름은 [ism]입니다 (Je ireumeun [ism]imnida)", "C) 나이는 [yosh]살입니다 (Naineun [yosh]salimnida)"],
        "answer": "B"
    },
    {
        "q": "“Sizning ismingiz nima?” degan savol:",
        "options": ["A) 감사합니다 (Gamsahamnida)", "B) 이름이 뭐예요? (Ireumi mwoyeyo?)", "C) 몇 살이세요? (Myeot sariseyo?)"],
        "answer": "B"
    },
    {
        "q": "“Men 20 yoshdaman” ni qanday aytish?",
        "options": ["A) 저는 학생입니다 (Jeoneun haksaengimnida)", "B) 저는 20살입니다 (Jeoneun 20salimnida)", "C) 어디에서 왔어요? (Eodieseo wasseoyo?)"],
        "answer": "B"
    },
    {
        "q": "“Siz necha yoshdasiz?” degan savol:",
        "options": ["A) 이름이 뭐예요? (Ireumi mwoyeyo?)", "B) 몇 살이세요? (Myeot sariseyo?)", "C) 고마워요 (Gomawoyo)"],
        "answer": "B"
    },
    {
        "q": "“Men talabaman” ni qanday aytish?",
        "options": ["A) 저는 한국 사람입니다 (Jeoneun hanguk saramimnida)", "B) 저는 학생입니다 (Jeoneun haksaengimnida)", "C) 저는 선생님입니다 (Jeoneun seonsaengnimimnida)"],
        "answer": "B"
    },
    {
        "q": "“Men o‘zbekman” ni qanday aytish?",
        "options": ["A) 저는 한국 사람입니다 (Jeoneun Hanguk saramimnida)", "B) 저는 미국 사람입니다 (Jeoneun Miguk saramimnida)", "C) 저는 우즈베키스탄 사람입니다 (Jeoneun Woozbekistan saramimnida)"],
        "answer": "C"
    },
    {
        "q": "“Siz qayerdansiz?” degan savol:",
        "options": ["A) 몇 살이세요? (Myeot sariseyo?)", "B) 이름이 뭐예요? (Ireumi mwoyeyo?)", "C) 어디 사람입니까? (Eodi saramimnikka?)"],
        "answer": "C"
    },
    {
        "q": "“Bir” (1) ni koreys tilida:",
        "options": ["A) 셋 (Set)", "B) 둘 (Dul)", "C) 하나 (Hana)"],
        "answer": "C"
    },
    {
        "q": "“Ona” ni koreys tilida:",
        "options": ["A) 아버지 (Abeoji)", "B) 형제 (Hyeongje)", "C) 어머니 (Eomeoni)"],
        "answer": "C"
    },
    {
        "q": "“Ota” ni koreys tilida:",
        "options": ["A) 자매 (Jamae)", "B) 어머니 (Eomeoni)", "C) 아버지 (Abeoji)"],
        "answer": "C"
    },
    {
        "q": "“Soat” ni koreys tilida:",
        "options": ["A) 분 (Bun)", "B) 초 (Cho)", "C) 시 (Si)"],
        "answer": "C"
    },
    {
        "q": "“Soat 3” ni qanday aytish?",
        "options": ["A) 세 분 (Set bun)", "B) 세 시 (Set si)", "C) 세 초 (Set cho)"],
        "answer": "B"
    },
    {
        "q": "“Seshanba” ni koreys tilida:",
        "options": ["A) 금요일 (Geumyoil)", "B) 월요일 (Woryoil)", "C) 화요일 (Hwayoil)"],
        "answer": "C"
    },
    {
        "q": "“Qizil” ni koreys tilida:",
        "options": ["A) 초록 (Chorok)", "B) 빨강 (Ppalgan)", "C) 파랑 (Paran)"],
        "answer": "B"
    },
    {
        "q": "“Men kitob o‘qiyman” da subject partikli:",
        "options": ["A) 을/를 (Eul/Reul)", "B) 에 (E)", "C) 은/는 (Eun/Neun)"],
        "answer": "C"
    },
    {
        "q": "“Men olmani yeyman” da object partikli:",
        "options": ["A) 에 (E)", "B) 은/는 (Eun/Neun)", "C) 을/를 (Eul/Reul)"],
        "answer": "C"
    },
    {
        "q": "“Men uyda” da joy partikli:",
        "options": ["A) 을/를 (Eul/Reul)", "B) 에서 (Eso)", "C) 에 (E)"],
        "answer": "C"
    },
    {
        "q": "“Bu kitob” ni qanday aytish?",
        "options": ["A) 이것이 책입니다 (Igeosi chaegimnida)", "B) 이것은 책입니다 (Igeoseun chaegimnida)", "C) 이것을 책입니다 (Igeoseul chaegimnida)"],
        "answer": "B"
    },
    {
        "q": "“Nima?” degan so‘z:",
        "options": ["A) 언제 (Eonje)", "B) 누구 (Nugu)", "C) 뭐 (Mwo)"],
        "answer": "C"
    }
],

    "1B": [
    {
        "q": "“Men ovqatlanaman” (hozirgi zamon) ni qanday aytish?",
        "options": ["B) 마셔요 (Masyeoyo)", "C) 가요 (Gayo)", "A) 먹어요 (Meogeoyo)"],
        "answer": "A"
    },
    {
        "q": "“Siz suv ichasizmi?” degan savol:",
        "options": ["C) 집에 가요? (Jib-e gayo?)", "B) 책을 읽어요? (Chaeg-eul ilgeoyo?)", "A) 물을 마셔요? (Mureul masyeoyo?)"],
        "answer": "A"
    },
    {
        "q": "“Men maktabga boraman” ni qanday aytish?",
        "options": ["C) 시장에 가요 (Sijang-e gayo)", "A) 학교에 가요 (Hakgyo-e gayo)", "B) 집에 와요 (Jib-e wayo)"],
        "answer": "A"
    },
    {
        "q": "“U uyga keladi” ni qanday aytish?",
        "options": ["A) 집에 와요 (Jib-e wayo)", "C) 병원에 가요 (Byeongwon-e gayo)", "B) 학교에 가요 (Hakgyo-e gayo)"],
        "answer": "A"
    },
    {
        "q": "“Men kitob o‘qidim” (o‘tgan) ni qanday aytish?",
        "options": ["C) 책을 읽습니다 (Chaeg-eul ilgeumnida)", "A) 책을 읽었어요 (Chaeg-eul ilgeosseoyo)", "B) 책을 읽어요 (Chaeg-eul ilgeoyo)"],
        "answer": "A"
    },
    {
        "q": "“Biz ovqatlandik” (o‘tgan) ni qanday aytish?",
        "options": ["B) 마셨어요 (Maseosseoyo)", "A) 먹었어요 (Meogeosseoyo)", "C) 갔어요 (Gasseoyo)"],
        "answer": "A"
    },
    {
        "q": "“Maktab” ni koreys tilida:",
        "options": ["A) 학교 (Hakgyo)", "B) 집 (Jib)", "C) 시장 (Sijang)"],
        "answer": "A"
    },
    {
        "q": "“Uy” ni koreys tilida:",
        "options": ["C) 병원 (Byeongwon)", "A) 학교 (Hakgyo)", "B) 집 (Jib)"],
        "answer": "B"
    },
    {
        "q": "“Bugun” ni koreys tilida:",
        "options": ["B) 내일 (Naeil)", "A) 오늘 (Oneul)", "C) 어제 (Eoje)"],
        "answer": "A"
    },
    {
        "q": "“Ertaga” ni koreys tilida:",
        "options": ["C) 어제 (Eoje)", "B) 내일 (Naeil)", "A) 오늘 (Oneul)"],
        "answer": "B"
    },
    {
        "q": "“Olma” ni koreys tilida:",
        "options": ["B) 바나나 (Banana)", "A) 사과 (Sagua)", "C) 오렌지 (Orenji)"],
        "answer": "A"
    },
    {
        "q": "“Suv” ni koreys tilida:",
        "options": ["A) 물 (Mul)", "C) 주스 (Juseu)", "B) 우유 (Uyu)"],
        "answer": "A"
    },
    {
        "q": "“Maktabga boraman”da yo‘nalish partikli:",
        "options": ["B) 에서 (Eso)", "A) 에 (E)", "C) 을/를 (Eul/Reul)"],
        "answer": "A"
    },
    {
        "q": "“Uyda ovqatlanaman”da joy partikli:",
        "options": ["B) 에서 (Eso)", "A) 에 (E)", "C) 은/는 (Eun/Neun)"],
        "answer": "B"
    },
    {
        "q": "“Men ovqatlanmayman” (salbiy) ni qanday aytish?",
        "options": ["C) 먹어요 (Meogeoyo)", "A) 안 먹어요 (An meogeoyo)", "B) 먹지 않아요 (Meokji anayo)"],
        "answer": "A"
    },
    {
        "q": "“Qayerdasiz?” degan savol:",
        "options": ["B) 언제예요? (Eonjeyeyo?)", "A) 어디예요? (Eodiyeyo?)", "C) 왜예요? (Waeyeyo?)"],
        "answer": "A"
    },
    {
        "q": "“Nega?” degan savol:",
        "options": ["A) 어디예요? (Eodiyeyo?)", "B) 언제예요? (Eonjeyeyo?)", "C) 왜예요? (Waeyeyo?)"],
        "answer": "C"
    },
    {
        "q": "“Qalam” ni koreys tilida:",
        "options": ["B) 책 (Chaek)", "C) 가방 (Gabang)", "A) 연필 (Yeonpil)"],
        "answer": "A"
    },
    {
        "q": "“Kitob” ni koreys tilida:",
        "options": ["A) 연필 (Yeonpil)", "B) 책 (Chaek)", "C) 노트 (Noteu)"],
        "answer": "B"
    },
    {
        "q": "“Issiq” ni koreys tilida:",
        "options": ["B) 춥다 (Chupda)", "C) 비가 온다 (Bi ga onda)", "A) 덥다 (Deopda)"],
        "answer": "A"
    }
],
    "2A": [
    {
        "q": "“Men kitob o‘qiyapman” ni qanday aytish?",
        "options": ["C) 책을 읽어요 (Chaeg-eul ilgeoyo)", "A) 책을 읽고 있어요 (Chaeg-eul ilgo isseoyo)", "B) 책을 읽었어요 (Chaeg-eul ilgeosseoyo)"],
        "answer": "A"
    },
    {
        "q": "“Men kecha film ko‘rdim” ni qanday aytish?",
        "options": ["A) 어제 영화를 봤어요 (Eoje yeonghwa-reul bwasseoyo)", "C) 어제 영화를 보고 있어요 (Eoje yeonghwa-reul bogo isseoyo)", "B) 어제 영화를 봐요 (Eoje yeonghwa-reul bwayo)"],
        "answer": "A"
    },
    {
        "q": "“Men televizor ko‘rmayman” ni qanday aytish?",
        "options": ["B) TV를 안 봐요 (Ti-bi-reul an bwayo)", "A) TV를 보지 않아요 (Ti-bi-reul boji anayo)", "C) Both A and B"],
        "answer": "C"
    },
    {
        "q": "“Men koreys tilini o‘rganish uchun Seuldaman” ni qanday aytish?",
        "options": ["B) 한국어를 배우고 서울에 있어요 (Hangugeo-reul baeugo seoure isseoyo)", "A) 한국어를 배우기 위해 서울에 있어요 (Hangugeo-reul baeugi wihae seoure isseoyo)", "C) 한국어를 배워요 (Hangugeo-reul baewoyo)"],
        "answer": "A"
    },
    {
        "q": "“Men kitob o‘qidim va film ko‘rdim” ni qanday aytish?",
        "options": ["B) 책을 읽어서 영화를 봤어요 (Chaeg-eul ilgeoseo yeonghwa-reul bwasseoyo)", "C) 책을 읽거나 영화를 봤어요 (Chaeg-eul ilgeona yeonghwa-reul bwasseoyo)", "A) 책을 읽고 영화를 봤어요 (Chaeg-eul ilgo yeonghwa-reul bwasseoyo)"],
        "answer": "A"
    },
    {
        "q": "“Men kitob o‘qiyman yoki film ko‘raman” ni qanday aytish?",
        "options": ["A) 책을 읽거나 영화를 봐요 (Chaeg-eul ilgeona yeonghwa-reul bwayo)", "B) 책을 읽고 영화를 봐요 (Chaeg-eul ilgo yeonghwa-reul bwayo)", "C) 책을 읽어서 영화를 봐요 (Chaeg-eul ilgeoseo yeonghwa-reul bwayo)"],
        "answer": "A"
    },
    {
        "q": "“Har kuni” ni koreys tilida:",
        "options": ["C) 내일 (Naeil)", "B) 어제 (Eoje)", "A) 매일 (Maeil)"],
        "answer": "A"
    },
    {
        "q": "“O‘tgan hafta” ni koreys tilida:",
        "options": ["C) 이번 주 (Ibeon ju)", "B) 다음 주 (Daeum ju)", "A) 지난 주 (Jinan ju)"],
        "answer": "A"
    },
    {
        "q": "“Do‘kon” ni koreys tilida:",
        "options": ["B) 병원 (Byeongwon)", "A) 가게 (Gage)", "C) 학교 (Hakgyo)"],
        "answer": "A"
    },
    {
        "q": "“Kasalxona” ni koreys tilida:",
        "options": ["A) 병원 (Byeongwon)", "C) 집 (Jib)", "B) 가게 (Gage)"],
        "answer": "A"
    },
    {
        "q": "“Kimchi” ni koreys tilida:",
        "options": ["A) 김치 (Gimchi)", "B) 비빔밥 (Bibimbap)", "C) 불고기 (Bulgogi)"],
        "answer": "A"
    },
    {
        "q": "“Guruch” ni koreys tilida:",
        "options": ["C) 고기 (Gogi)", "A) 쌀 (Ssal)", "B) 빵 (Ppang)"],
        "answer": "A"
    },
    {
        "q": "“Men maktabda o‘qiyapman” da joy partikli:",
        "options": ["A) 에서 (Ese)", "B) 에 (E)", "C) 을/를 (Eul/reul)"],
        "answer": "A"
    },
    {
        "q": "“Men do‘stimga xat yozdim” da partikl:",
        "options": ["C) 에서 (Ese)", "A) 한테 (Hante)", "B) 에 (E)"],
        "answer": "A"
    },
    {
        "q": "“Men koreys tilida yaxshi gapira olmayman” ni qanday aytish?",
        "options": ["B) 한국어로 잘 안 말해요 (Hangugeoro jal an malhaeyo)", "A) 한국어로 잘 말하지 못해요 (Hangugeoro jal malhaji motaeyo)", "C) 한국어로 잘 말해요 (Hangugeoro jal malhaeyo)"],
        "answer": "A"
    },
    {
        "q": "“Bu qancha turadi?” degan savol:",
        "options": ["B) 이거 어디예요? (Igeo eodiyeyo?)", "A) 이거 얼마예요? (Igeo eolmayeyo?)", "C) 이거 언제예요? (Igeo eonjeyeyo?)"],
        "answer": "A"
    },
    {
        "q": "“Bu qanday?” degan savol:",
        "options": ["C) 이거 누구예요? (Igeo nuguyeyo?)", "B) 이거 뭐예요? (Igeo mwoyeyo?)", "A) 이거 어때요? (Igeo eottaeyo?)"],
        "answer": "A"
    },
    {
        "q": "“Men xat yozaman” ni qanday aytish?",
        "options": ["A) 편지를 써요 (Pyeonji-reul sseoyo)", "C) 편지를 봐요 (Pyeonji-reul bwayo)", "B) 편지를 읽어요 (Pyeonji-reul ilgeoyo)"],
        "answer": "A"
    },
    {
        "q": "“Men kiyim sotib oldim” ni qanday aytish?",
        "options": ["B) 옷을 입었어요 (Oseul ibeosseoyo)", "C) 옷을 봤어요 (Oseul bwasseoyo)", "A) 옷을 샀어요 (Oseul sasseoyo)"],
        "answer": "A"
    },
    {
        "q": "“Yomg‘ir yog‘moqda” ni koreys tilida:",
        "options": ["B) 눈이 와요 (Nuni wayo)", "C) 바람이 불어요 (Barami bureoyo)", "A) 비가 와요 (Bi ga wayo)"],
        "answer": "A"
    }
],
    "2B" : [
    {
        "q": "“Men har kuni ertalab kitob o‘qishga harakat qilaman” ni qanday aytish?",
        "options": [
            "A) 매일 아침 책을 읽도록 해요 (Maeil achim chaeg-eul ilgdorok haeyo)",
            "B) 매일 아침 책을 읽어요 (Maeil achim chaeg-eul ilgeoyo)",
            "C) 매일 아침 책을 읽었어요 (Maeil achim chaeg-eul ilgeosseoyo)"
        ],
        "answer": "A"
    },
    {
        "q": "“Siz imtihondan o‘tish uchun ko‘p o‘qishingiz kerak” ni qanday aytish?",
        "options": [
            "A) 시험에 합격하려면 많이 공부해야 해요 (Siheom-e hapgyeokaryeomyeon mani gongbuhaeya haeyo)",
            "B) 시험에 합격하고 많이 공부해요 (Siheom-e hapgyeokago mani gongbuhaeyo)",
            "C) 시험에 합격하거나 많이 공부해요 (Siheom-e hapgyeokageona mani gongbuhaeyo)"
        ],
        "answer": "A"
    },
    {
        "q": "“Men uyda bo‘lganimda, u televizor ko‘rdi” ni qanday aytish?",
        "options": [
            "A) 집에 있는 동안 그가 TV를 봤어요 (Jib-e inneun dongan geuga ti-bi-reul bwasseoyo)",
            "B) 집에 있어서 그가 TV를 봤어요 (Jib-e isseoseo geuga ti-bi-reul bwasseoyo)",
            "C) 집에 있고 그가 TV를 봤어요 (Jib-e igo geuga ti-bi-reul bwasseoyo)"
        ],
        "answer": "A"
    },
    {
        "q": "“Men band bo‘lganim uchun kela olmadim” ni qanday aytish?",
        "options": [
            "A) 바빠서 올 수 없었어요 (Bappaseo ol su eopseosseoyo)",
            "B) 바빠기 때문에 올 수 없었어요 (Bappagi ttaemune ol su eopseosseoyo)",
            "C) 바빠고 올 수 없었어요 (Bappago ol su eopseosseoyo)"
        ],
        "answer": "B"
    },
    {
        "q": "“Men ertaga do‘stlarim bilan uchrashmoqchiman” ni qanday aytish?",
        "options": [
            "A) 내일 친구들과 만나려고 해요 (Naeil chingudeulgwa mannaryeogo haeyo)",
            "B) 내일 친구들과 만났어요 (Naeil chingudeulgwa mannasseoyo)",
            "C) 내일 친구들과 만나요 (Naeil chingudeulgwa mannayo)"
        ],
        "answer": "A"
    },
    {
        "q": "“Bu chiroyli, lekin qimmat” ni qanday aytish?",
        "options": [
            "A) 예쁘지만 비싸요 (Yeppeojiman bissayo)",
            "B) 예쁘고 비싸요 (Yeppeogo bissayo)",
            "C) 예쁘거나 비싸요 (Yeppeogeona bissayo)"
        ],
        "answer": "A"
    },
    {
        "q": "“Bu erda suratga olish mumkinmi?” ni qanday aytish?",
        "options": [
            "A) 여기서 사진을 찍어도 돼요? (Yeogiseo sajin-eul jjigeodo dwaeyo?)",
            "B) 여기서 사진을 찍어야 해요? (Yeogiseo sajin-eul jjigeoya haeyo?)",
            "C) 여기서 사진을 찍지 마세요 (Yeogiseo sajin-eul jjikji maseyo)"
        ],
        "answer": "A"
    },
    {
        "q": "“Bu erda chekmang” ni qanday aytish?",
        "options": [
            "A) 여기서 담배를 피우지 마세요 (Yeogiseo dambae-reul piuji maseyo)",
            "B) 여기서 담배를 피워도 돼요 (Yeogiseo dambae-reul piwodo dwaeyo)",
            "C) 여기서 담배를 피워요 (Yeogiseo dambae-reul piwoyo)"
        ],
        "answer": "A"
    },
    {
        "q": "“Men kecha kitob o‘qiyotgan edim” ni qanday aytish?",
        "options": [
            "A) 어제 책을 읽고 있었어요 (Eoje chaeg-eul ilgo isseosseoyo)",
            "B) 어제 책을 읽었어요 (Eoje chaeg-eul ilgeosseoyo)",
            "C) 어제 책을 읽어요 (Eoje chaeg-eul ilgeoyo)"
        ],
        "answer": "A"
    },
    {
        "q": "“Bu juda qiziqarli” ni qanday aytish?",
        "options": [
            "A) 아주 재미있어요 (Aju jaemiisseoyo)",
            "B) 아주 맛있어요 (Aju masisseoyo)",
            "C) 아주 비싸요 (Aju bissayo)"
        ],
        "answer": "A"
    },
    {
        "q": "“Bu juda arzon” ni qanday aytish?",
        "options": [
            "A) 아주 싸요 (Aju ssayo)",
            "B) 아주 비싸요 (Aju bissayo)",
            "C) 아주 예뻐요 (Aju yeppeoyo)"
        ],
        "answer": "A"
    },
    {
        "q": "“Ikki soatdan beri” ni koreys tilida qanday aytish?",
        "options": [
            "A) 두 시간 동안 (Du sigan dongan)",
            "B) 두 시간 전에 (Du sigan jeone)",
            "C) 두 시간 후에 (Du sigan hue)"
        ],
        "answer": "A"
    },
    {
        "q": "“Ikki soatdan keyin” ni koreys tilida qanday aytish?",
        "options": [
            "A) 두 시간 동안 (Du sigan dongan)",
            "B) 두 시간 전에 (Du sigan jeone)",
            "C) 두 시간 후에 (Du sigan hue)"
        ],
        "answer": "C"
    },
    {
        "q": "“Men bandman, lekin yordam bera olaman” ni qanday aytish?",
        "options": [
            "A) 바쁘는데 도와줄 수 있어요 (Bappneunde dowajul su isseoyo)",
            "B) 바빠서 도와줄 수 있어요 (Bappaseo dowajul su isseoyo)",
            "C) 바빠고 도와줄 수 있어요 (Bappago dowajul su isseoyo)"
        ],
        "answer": "A"
    },
    {
        "q": "“Bu kimning narsasi?” degan savol:",
        "options": [
            "A) 이거 누구 거예요? (Igeo nugu geoyeyo?)",
            "B) 이거 뭐예요? (Igeo mwoyeyo?)",
            "C) 이거 어디예요? (Igeo eodiyeyo?)"
        ],
        "answer": "A"
    },
    {
        "q": "“Bu qayerdan?” degan savol:",
        "options": [
            "A) 이거 어디서 샀어요? (Igeo eodiseo sasseoyo?)",
            "B) 이거 언제 샀어요? (Igeo eonje sasseoyo?)",
            "C) 이거 왜 샀어요? (Igeo wae sasseoyo?)"
        ],
        "answer": "A"
    },
    {
        "q": "“Men soat 5 gacha ishlayman” da partikl:",
        "options": [
            "A) 까지 (Kkaji)",
            "B) 에서 (Ese)",
            "C) 에 (E)"
        ],
        "answer": "A"
    },
    {
        "q": "“Men soat 9 dan ishlayman” da partikl:",
        "options": [
            "A) 부터 (Buteo)",
            "B) 까지 (Kkaji)",
            "C) 에서 (Ese)"
        ],
        "answer": "A"
    },
    {
        "q": "“Men kecha yaxshi uxladim” ni qanday aytish?",
        "options": [
            "A) 어제 잘 잤어요 (Eoje jal jasseoyo)",
            "B) 어제 잘 먹었어요 (Eoje jal meogeosseoyo)",
            "C) 어제 잘 갔어요 (Eoje jal gasseoyo)"
        ],
        "answer": "A"
    },
    {
        "q": "“Men har kuni ishlayman” ni qanday aytish?",
        "options": [
            "A) 매일 일해요 (Maeil ilhaeyo)",
            "B) 매일 공부해요 (Maeil gongbuhaeyo)",
            "C) 매일 놀아요 (Maeil norayo)"
        ],
        "answer": "A"
    }
],

    "3A" : [
    {
        "q": "“Men muvaffaqiyatli bo‘lish uchun ko‘p harakat qilaman” ni qanday aytish?",
        "options": [
            "A) 성공하도록 많이 노력해요 (Seonggonghadorok mani noryeokhaeyo)",
            "B) 성공해서 많이 노력해요 (Seonggonghaeseo mani noryeokhaeyo)",
            "C) 성공하고 많이 노력해요 (Seonggonghago mani noryeokhaeyo)"
        ],
        "answer": "A"
    },
    {
        "q": "“Yomg‘ir tufayli kech qoldim” ni qanday aytish?",
        "options": [
            "A) 비가 오는 바람에 늦었어요 (Bi ga oneun barame neujeosseoyo)",
            "B) 비가 와서 늦었어요 (Bi ga waseo neujeosseoyo)",
            "C) 비가 오고 늦었어요 (Bi ga ogo neujeosseoyo)"
        ],
        "answer": "A"
    },
    {
        "q": "“Men Seuldagi universitetda o‘qishga qaror qildim” ni qanday aytish?",
        "options": [
            "A) 서울 대학교에서 공부하게 됐어요 (Seoul daehakgyo-eseo gongbuhage dwaesseoyo)",
            "B) 서울 대학교에서 공부했어요 (Seoul daehakgyo-eseo gongbuhaesseoyo)",
            "C) 서울 대학교에서 공부해요 (Seoul daehakgyo-eseo gongbuhaeyo)"
        ],
        "answer": "A"
    },
    {
        "q": "“Men band bo‘lsam ham, yordam bera olaman” ni qanday aytish?",
        "options": [
            "A) 바빠도 도와줄 수 있어요 (Bappado dowajul su isseoyo)",
            "B) 바빠서 도와줄 수 있어요 (Bappaseo dowajul su isseoyo)",
            "C) 바빠고 도와줄 수 있어요 (Bappago dowajul su isseoyo)"
        ],
        "answer": "A"
    },
    {
        "q": "“Agar yomg‘ir yog‘sa, uyda qolaman” ni qanday aytish?",
        "options": [
            "A) 비가 오면 집에 있어요 (Bi ga omyeon jib-e isseoyo)",
            "B) 비가 오고 집에 있어요 (Bi ga ogo jib-e isseoyo)",
            "C) 비가 와서 집에 있어요 (Bi ga waseo jib-e isseoyo)"
        ],
        "answer": "A"
    },
    {
        "q": "“Bu arzon, lekin sifati yaxshi emas” ni qanday aytish?",
        "options": [
            "A) 싸는데 품질이 좋지 않아요 (Ssanunde pumjiri jochi anayo)",
            "B) 싸지만 품질이 좋아요 (Ssajiman pumjiri joayo)",
            "C) 싸아서 품질이 좋지 않아요 (Ssaseo pumjiri jochi anayo)"
        ],
        "answer": "A"
    },
    {
        "q": "“Men yangi kiyim sotib olmoqchiman” ni qanday aytish?",
        "options": [
            "A) 새 옷을 사려고 해요 (Sae oseul saryeogo haeyo)",
            "B) 새 옷을 샀어요 (Sae oseul sasseoyo)",
            "C) 새 옷을 사요 (Sae oseul sayo)"
        ],
        "answer": "A"
    },
    {
        "q": "“Iltimos, bu yerga kelmang” ni qanday aytish?",
        "options": [
            "A) 여기 오지 마세요 (Yeogi oji maseyo)",
            "B) 여기 와도 돼요 (Yeogi wado dwaeyo)",
            "C) 여기 와요 (Yeogi wayo)"
        ],
        "answer": "A"
    },
    {
        "q": "“Men kechagacha Seuldan kelgan edim” ni qanday aytish?",
        "options": [
            "A) 어제까지 서울에서 왔었어요 (Eoje kkaji seoureseo wasseosseoyo)",
            "B) 어제 서울에서 왔어요 (Eoje seoureseo wasseoyo)",
            "C) 어제 서울에서 와요 (Eoje seoureseo wayo)"
        ],
        "answer": "A"
    },
    {
        "q": "“Men charchaganim uchun uxladim” ni qanday aytish?",
        "options": [
            "A) 피곤해서 잤어요 (Pigonhaeseo jasseoyo)",
            "B) 피곤한데 잤어요 (Pigonhande jasseoyo)",
            "C) 피곤하도록 잤어요 (Pigonhadorok jasseoyo)"
        ],
        "answer": "A"
    },
    {
        "q": "“Bu juda xavfli” ni qanday aytish?",
        "options": [
            "A) 아주 위험해요 (Aju wiheomhaeyo)",
            "B) 아주 안전해요 (Aju anjeonhaeyo)",
            "C) 아주 편해요 (Aju pyeonhaeyo)"
        ],
        "answer": "A"
    },
    {
        "q": "“Bu juda qulay” ni qanday aytish?",
        "options": [
            "A) 아주 편해요 (Aju pyeonhaeyo)",
            "B) 아주 어렵어요 (Aju eoryeowoyo)",
            "C) 아주 재미있어요 (Aju jaemiisseoyo)"
        ],
        "answer": "A"
    },
    {
        "q": "“Uch kun oldin” ni koreys tilida:",
        "options": [
            "A) 사흘 전에 (Saheul jeone)",
            "B) 사흘 후에 (Saheul hue)",
            "C) 사흘 동안 (Saheul dongan)"
        ],
        "answer": "A"
    },
    {
        "q": "“Uch soat davomida” ni koreys tilida:",
        "options": [
            "A) 세 시간 동안 (Se sigan dongan)",
            "B) 세 시간 전에 (Se sigan jeone)",
            "C) 세 시간 후에 (Se sigan hue)"
        ],
        "answer": "A"
    },
    {
        "q": "“Men o‘qituvchimga xat yozdim” da partikl qaysi?",
        "options": [
            "A) 에게 (Ege)",
            "B) 에서 (Ese)",
            "C) 까지 (Kkaji)"
        ],
        "answer": "A"
    },
    {
        "q": "“Bu narsani qayerdan sotib oldingiz?” degan savolni tanlang:",
        "options": [
            "A) 이거 어디서 샀어요? (Igeo eodiseo sasseoyo?)",
            "B) 이거 언제 샀어요? (Igeo eonje sasseoyo?)",
            "C) 이거 왜 샀어요? (Igeo wae sasseoyo?)"
        ],
        "answer": "A"
    },
    {
        "q": "“Bu nima uchun kerak?” degan savolni tanlang:",
        "options": [
            "A) 이거 왜 필요해요? (Igeo wae piryohaeyo?)",
            "B) 이거 어디 필요해요? (Igeo eodi piryohaeyo?)",
            "C) 이거 언제 필요해요? (Igeo eonje piryohaeyo?)"
        ],
        "answer": "A"
    },
    {
        "q": "“Men do‘stimga yordam berdim” ni qanday aytish?",
        "options": [
            "A) 친구에게 도와줬어요 (Chinguege dowajwosseoyo)",
            "B) 친구에게 갔어요 (Chinguege gasseoyo)",
            "C) 친구에게 말했어요 (Chinguege malhaesseoyo)"
        ],
        "answer": "A"
    },
    {
        "q": "“Men kecha koreys tilini o‘rgandim” ni qanday aytish?",
        "options": [
            "A) 어제 한국어를 공부했어요 (Eoje hangugeoreul gongbuhaesseoyo)",
            "B) 어제 한국어를 배웠어요 (Eoje hangugeoreul baeweosseoyo)",
            "C) Both A and B"
        ],
        "answer": "C"
    },
    {
        "q": "“Sovg‘a” ni koreys tilida:",
        "options": [
            "A) 선물 (Seonmul)",
            "B) 가격 (Gagyeok)",
            "C) 품질 (Pumjil)"
        ],
        "answer": "A"
    }
],
    "3B" : [
    {
        "q": "“Muvaffaqiyat” so‘zining koreyscha tarjimasi qaysi?",
        "options": [
            "A) 실패 (Silpae)",
            "B) 성공 (Seonggong)",
            "C) 노력 (Noryeok)"
        ],
        "answer": "B"
    },
    {
        "q": "Bo‘shliqni to‘ldiring: 저는 매일 아침 책을 ____ 읽습니다.",
        "options": [
            "A) 열심히",
            "B) 자주",
            "C) 빨리",
            "D) 조용히"
        ],
        "answer": "B"
    },
    {
        "q": "“저는 친구와 ___ 영화를 봤습니다.” Jumlani to‘ldirish uchun to‘g‘ri so‘zni tanlang:",
        "options": [
            "A) 같이",
            "B) 혼자",
            "C) 먼저",
            "D) 나중에"
        ],
        "answer": "A"
    },
    {
        "q": "Quyidagi so‘zlarni mos ma’nolar bilan bog‘lang: 건강하다, 피곤하다, 행복하다.",
        "options": [
            "A) 1-b, 2-c, 3-a",
            "B) 1-c, 2-b, 3-a",
            "C) 1-a, 2-b, 3-c"
        ],
        "answer": "A"
    },
    {
        "q": "Bo‘shliqni to‘ldiring: 저는 한국에 온 ___ 3년이 되었습니다.",
        "options": [
            "A) 지",
            "B) 만에",
            "C) 후에",
            "D) 전에"
        ],
        "answer": "A"
    },
    {
        "q": "Qaysi jumla grammatik jihatdan to‘g‘ri?",
        "options": [
            "A) 저는 매일 책을 읽어아요.",
            "B) 저는 매일 책을 읽습니다.",
            "C) 저는 매일 책을 읽어요.",
            "D) 저는 매일 책을 읽습니다요."
        ],
        "answer": "B"
    },
    {
        "q": "날씨가 추워서 옷을 ___ 입어야 합니다.",
        "options": [
            "A) 얇게",
            "B) 두껍게",
            "C) 빠르게",
            "D) 천천히"
        ],
        "answer": "B"
    },
    {
        "q": "“공기놀이” qanday o‘yinni anglatadi?",
        "options": [
            "A) Futbol",
            "B) Badminton",
            "C) An’anaviy koreys o‘yini",
            "D) Basketbol"
        ],
        "answer": "C"
    },
    {
        "q": "Fe’llarni mos ma’nolar bilan bog‘lang: 가다, 오다, 먹다.",
        "options": [
            "A) 1-c, 2-a, 3-b",
            "B) 1-a, 2-b, 3-c",
            "C) 1-b, 2-c, 3-a"
        ],
        "answer": "A"
    },
    {
        "q": "저는 한국어를 ___ 배우고 싶습니다.",
        "options": [
            "A) 열심히",
            "B) 어렵게",
            "C) 느리게",
            "D) 비싸게"
        ],
        "answer": "A"
    },
    {
        "q": "“Maktab” so‘zining koreyscha tarjimasi qaysi?",
        "options": [
            "A) 병원",
            "B) 학교",
            "C) 도서관",
            "D) 공원"
        ],
        "answer": "B"
    },
    {
        "q": "친구가 아파서 병원에 ___ 갔습니다.",
        "options": [
            "A) 먼저",
            "B) 같이",
            "C) 혼자",
            "D) 빨리"
        ],
        "answer": "C"
    },
    {
        "q": "Quyidagi jumlada qaysi so‘z noto‘g‘ri ishlatilgan? 저는 아침에 밥을 먹습니다 대신에 커피를 마십니다.",
        "options": [
            "A) 먹습니다",
            "B) 대신에",
            "C) 마십니다",
            "D) 아침에"
        ],
        "answer": "A"
    },
    {
        "q": "Quyidagi iboralarni mos ma’nolar bilan bog‘lang: 날씨가 좋다, 시간이 없다, 배고프다.",
        "options": [
            "A) 1-c, 2-b, 3-a",
            "B) 1-b, 2-a, 3-c",
            "C) 1-a, 2-c, 3-b"
        ],
        "answer": "A"
    },
    {
        "q": "저는 주말에 ___ 영화를 볼 계획입니다.",
        "options": [
            "A) 재미있는",
            "B) 재미없는",
            "C) 비싼",
            "D) 큰"
        ],
        "answer": "A"
    },
    {
        "q": "저는 매주 토요일 아침에 공원에서 운동을 합니다. — yozuvchi qayerda mashq qiladi?",
        "options": [
            "A) Maktabda",
            "B) Parkda",
            "C) Uyda",
            "D) Sport zalida"
        ],
        "answer": "B"
    },
    {
        "q": "Yozuvchi parkka mashinada boradi. (To‘g‘ri yoki noto‘g‘ri?)",
        "options": [
            "A) To‘g‘ri",
            "B) Noto‘g‘ri"
        ],
        "answer": "B"
    },
    {
        "q": "Yozuvchi parkdan keyin nima qiladi? 저녁에 친구들과 ___를 마십니다.",
        "options": [
            "A) 커피",
            "B) 차",
            "C) 주스"
        ],
        "answer": "A"
    },
    {
        "q": "Parkda nima ko‘p?",
        "options": [
            "A) Odamlar",
            "B) Mashinalar",
            "C) Daraxtlar",
            "D) Uylar"
        ],
        "answer": "C"
    },
    {
        "q": "Yozuvchi har kuni parkka boradi. (To‘g‘ri yoki noto‘g‘ri?)",
        "options": [
            "A) To‘g‘ri",
            "B) Noto‘g‘ri"
        ],
        "answer": "B"
    }
]








}

# 📋 Bosh menyu funksiyasi
def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        KeyboardButton("📚 Kurslar ro‘yxati"),
        KeyboardButton("👩‍🏫 O‘qituvchilar"),
        KeyboardButton("📝 Testni boshlash"),
        KeyboardButton("ℹ️ Markaz haqida"),
        KeyboardButton("❓ Savol-javob (FAQ)"),
        KeyboardButton("📞 Aloqa"),
        KeyboardButton("👤 Profil")
    )
    return markup


def is_registered(chat_id):
    return chat_id in users_data and "account" in users_data[chat_id]

def start_quiz_timer(chat_id):
    timer = threading.Timer(1800, lambda: finish_quiz_auto(chat_id))
    users_data[chat_id]["quiz"]["timer"] = timer
    timer.start()

def finish_quiz_auto(chat_id):
    if "quiz" in users_data.get(chat_id, {}):
        user = users_data[chat_id]["quiz"]
        score = user["score"]
        total = len(user["questions"])

        if score >= 15:
            result = f"⏰ Vaqt tugadi!\n\n🎉 Siz imtihondan o'tdingiz.\nNatija: {score}/{total}"
        else:
            result = f"⏰ Vaqt tugadi!\n\n❌ Siz yiqildingiz.\nNatija: {score}/{total}"

        del users_data[chat_id]["quiz"]
        bot.send_message(chat_id, result, reply_markup=main_menu())


users_data = {}

def is_registered(chat_id):
    return chat_id in users_data and "account" in users_data[chat_id]


# START komandasi
@bot.message_handler(commands=['start'])
def start_command(message):
    chat_id = message.chat.id

    if is_registered(chat_id):
        bot.send_message(chat_id, "✅ Siz allaqachon ro'yxatdan o'tgansiz.", reply_markup=main_menu())
        return

    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton("📞 Raqamni ulashish", request_contact=True))

    bot.send_message(
        chat_id,
        "<b>📞 Ro'yxatdan o'tish uchun telefon raqamingizni ulashing:</b>",
        reply_markup=markup,
        parse_mode="HTML"
    )
    users_data[chat_id] = {}


# ✅ Telefon raqamni qabul qilish
@bot.message_handler(content_types=['contact'])
def handle_registration(message):
    chat_id = message.chat.id

    if message.contact:
        registration_number = message.contact.phone_number[-9:]
    else:
        registration_number = message.text.strip()

    if not registration_number.isdigit() or len(registration_number) != 9:
        bot.send_message(chat_id, "❌ Iltimos, 9 xonali raqamingizni kiriting!")
        return

    users_data[chat_id]["phone_number"] = registration_number

    bot.send_message(
        chat_id,
        "👤 Endi Ism Familiyangizni kiriting.\n\nNamuna: <b>Shoxruh Azimov</b>",
        parse_mode="HTML"
    )

    bot.register_next_step_handler(message, ask_fullname)


# ✅ Ism familiyani qabul qilish
def ask_fullname(message):
    chat_id = message.chat.id
    fullname = message.text.strip()

    if len(fullname.split()) < 2:
        bot.send_message(chat_id, "❌ Iltimos, ism va familiyangizni to‘liq kiriting.\nNamuna: <b>Shoxruh Azimov</b>", parse_mode="HTML")
        bot.register_next_step_handler(message, ask_fullname)
        return

    users_data[chat_id]["account"] = {
        "nickname": message.from_user.username or "Foydalanuvchi",
        "fullname": fullname,
        "id": chat_id,
        "phone_number": users_data[chat_id]["phone_number"],
        "watched_video": False,
        "course": None,
        "video_msg_id": None,
        "button_msg_id": None
    }

    # 🎬 Video yuborish
    with open("bright.mp4", "rb") as video:
        sent_video = bot.send_video(chat_id, video, caption="📽 Iltimos, quyidagi videoni to‘liq ko‘rib chiqing.")
        users_data[chat_id]["account"]["video_msg_id"] = sent_video.message_id

    # ⏳ 30 sekunddan keyin tugma yuborish
    def send_watch_button():
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("🎬 Videoni ko‘rdim", callback_data="watched_video"))
        sent_button = bot.send_message(chat_id, "Videoni ko‘rib bo‘lgach tugmani bosing 👇", reply_markup=markup)
        users_data[chat_id]["account"]["button_msg_id"] = sent_button.message_id

    threading.Timer(30, send_watch_button).start()


# ✅ Inline tugma bosilganda (Videoni ko‘rdim)
@bot.callback_query_handler(func=lambda call: call.data == "watched_video")
def after_video(call):
    chat_id = call.message.chat.id
    account = users_data[chat_id]["account"]
    account["watched_video"] = True

    # 🎬 Video va tugma xabarlarini o‘chirish
    try:
        if account.get("video_msg_id"):
            bot.delete_message(chat_id, account["video_msg_id"])
        if account.get("button_msg_id"):
            bot.delete_message(chat_id, account["button_msg_id"])
    except Exception as e:
        print("Xabarni o‘chirishda xato:", e)

    bot.send_message(chat_id, "✅ Muvaffaqiyatli o'tdingiz!\n\nTilni tanlang:", reply_markup=main_menu())
    bot.answer_callback_query(call.id, "Videoni ko‘rganingiz tasdiqlandi ✅")


@bot.message_handler(func=lambda msg: msg.text == "📝 Testni boshlash")
def choose_language(msg):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        KeyboardButton("🇺🇸 Ingliz tili"),
        KeyboardButton("🇰🇷 Koreys tili"),
        KeyboardButton("⬅️ Orqaga")
    )
    bot.send_message(msg.chat.id, "🌐 Qaysi til bo‘yicha test topshirmoqchisiz?", reply_markup=markup)

# Profil ko‘rsatish
@bot.message_handler(func=lambda msg: msg.text == "👤 Profil")
def show_profile(message):
    chat_id = message.chat.id
    if not is_registered(chat_id):
        bot.send_message(chat_id, "Avval ro'yxatdan o'ting! /start")
        return

    account = users_data[chat_id]["account"]
    profile_text = (
        f"<b>Profil ma'lumotlari:</b>\n\n"
        f"👤 Ism Familiya: {account.get('fullname', 'Kiritilmagan')}\n"
        f"🆔 ID: <code>{account['id']}</code>\n"
        f"💬 Nickname: @{account['nickname']}\n"
        f"📞 Telefon: +998{account['phone_number']}\n"
        f"📘 Kurs: {account['course'] or 'Tanlanmagan'}"
    )
    bot.send_message(chat_id, profile_text, parse_mode="HTML")
@bot.message_handler(func=lambda msg: msg.text == "ℹ️ Markaz haqida")

def about_center(msg):
    photo_path = "brightfuture.jpg"

    caption = (
        "ℹ️ <b>Biz haqimizda:</b>\n\n"
        "📍 <b>Bright Future Center</b> — xorijiy tillar va IT yo‘nalishida zamonaviy ta’lim markazi.\n\n"
        "🎯 Maqsadimiz — yoshlarni kasb va til o‘rganish orqali kelajak sari yetaklash.\n\n"
        "🏫 Manzil: Andijon shahri, Asaka tumani, Korzinka binosi 2-qavat \n"
        "⏰ Ish vaqti: 09:00 — 20:00\n"
        "📅 Dam olish kuni: Yakshanba"
    )

    try:
        with open(photo_path, "rb") as photo:
            bot.send_photo(msg.chat.id, photo, caption=caption, parse_mode="HTML")
    except FileNotFoundError:
        bot.send_message(
            msg.chat.id,
            "ℹ️ <b>Biz haqimizda:</b>\n\n(Rasm topilmadi, lekin siz quyidagi ma’lumotlarni ko‘rishingiz mumkin 👇)\n\n" + caption,
            parse_mode="HTML"
        )

@bot.message_handler(func=lambda msg: msg.text == "❓ Savol-javob (FAQ)")
def show_faq(msg):
    text = (
        "❓ <b>Ko‘p so‘raladigan savollar:</b>\n\n"
        "1️⃣ <b>Darslar qanday o‘tiladi?</b>\n"
        "— Guruhli yoki individual tarzda, tajribali ustozlar bilan.\n\n"
        "2️⃣ <b>Online qatnashish mumkinmi?</b>\n"
        "— Ha, Zoom orqali ham qatnashish mumkin.\n\n"
        "3️⃣ <b>To‘lov qanday amalga oshiriladi?</b>\n"
        "— Naqd, Click yoki Payme orqali.\n\n"
        "4️⃣ <b>Darslar necha oy davom etadi?</b>\n"
        "— Har bir daraja o‘rtacha 6 oy davom etadi.\n\n"
        "5️⃣ <b>Test topshirish majburiymi?</b>\n"
        "— Ha, bu bilim darajasini aniqlash uchun kerak."
    )
    bot.send_message(msg.chat.id, text, parse_mode="HTML")


@bot.message_handler(func=lambda msg: msg.text == "📞 Aloqa")
def contact_info(msg):
    text = (
        "📞 <b>Aloqa ma’lumotlari:</b>\n\n"
        "📱 Telefon: +998 55 203 71 71\n"
        "📩 Telegram: @@bright_future_testing_bot\n"
        "🌐 Instagram: https://www.instagram.com/bright_future_skorea/\n"
        "📍 Manzil: Andijon, Asala, Korzinka binosi \n\n"
        "⏰ Ish vaqti: 08:00 — 20:00 (Dush–Shan)"
    )
    bot.send_message(msg.chat.id, text, parse_mode="HTML")

@bot.message_handler(commands=['admin'])
def admin_panel(message):
    chat_id = message.chat.id
    if chat_id != ADMIN_ID:
        bot.send_message(chat_id, "❌ Sizda admin huquqi yo‘q.")
        return

    total_users = len(users_data)
    courses_stat = {}

    for user in users_data.values():
        course = user["account"].get("course")
        if course:
            courses_stat[course] = courses_stat.get(course, 0) + 1

    stats_text = f"📊 <b>Admin Panel</b>\n\n👥 Foydalanuvchilar soni: {total_users}\n\n"
    stats_text += "📘 Kurslar statistikasi:\n"
    for course, count in courses_stat.items():
        stats_text += f"   - {course}: {count} ta\n"

    bot.send_message(chat_id, stats_text, parse_mode="HTML")

# Orqaga qaytish
@bot.message_handler(func=lambda msg: msg.text == "⬅️ Orqaga")
def go_back(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🇺🇸 Ingliz tili", "🇰🇷 Koreys tili")
    markup.add("👤 Profil")
    bot.send_message(message.chat.id, "Asosiy menyu", reply_markup=main_menu())

@bot.message_handler(func=lambda msg: msg.text in ["🇺🇸 Ingliz tili", "🇰🇷 Koreys tili"])
def choose_language(message):
    chat_id = message.chat.id
    if message.text == "🇺🇸 Ingliz tili":
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("Beginner", "Elementary", "Pre-Intermediate","Intermediate","Upper Intermediate","⬅️ Orqaga")
        bot.send_message(chat_id, "Darajani tanlang:", reply_markup=markup)
    elif message.text == "🇰🇷 Koreys tili":
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("1A", "1B", "2A","2B","3A","3B","⬅️ Orqaga")
        bot.send_message(chat_id, "Darajani tanlang:", reply_markup=markup)
    else:
        bot.send_message(chat_id, "Bu yo'nalish bo‘yicha testlar tez orada qo‘shiladi 😉")

@bot.message_handler(func=lambda msg: msg.text in ["Beginner", "Elementary", "Pre-Intermediate", "Intermediate", "Upper Intermediate", "1A", "1B", "2A", "2B", "3A", "3B"])
def request_quiz_permission(message):
    chat_id = message.chat.id
    level = message.text

    if level not in questions:
        bot.send_message(chat_id, "Uzr, bu daraja uchun test mavjud emas 😔")
        return

    user = users_data[chat_id]["account"]
    fullname = user.get("fullname", "Noma'lum foydalanuvchi")

    # Admin uchun xabar
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("✅ Ruxsat berish", callback_data=f"approve_test|{chat_id}|{level}"),
        InlineKeyboardButton("❌ Rad etish", callback_data=f"deny_test|{chat_id}|{level}")
    )

    admin_text = (
        f"🧑‍🎓 <b>Yangi test so‘rovi!</b>\n\n"
        f"👤 Foydalanuvchi: {fullname}\n"
        f"📞 Telefon: +998{user['phone_number']}\n"
        f"📘 Tanlangan kurs: {level}\n\n"
        f"Ruxsat berasizmi?"
    )

    bot.send_message(ADMIN_ID, admin_text, reply_markup=markup, parse_mode="HTML")
    bot.send_message(chat_id, "⏳ Testni boshlash uchun admin tasdig‘i kutilmoqda...")



# ✅ Admin ruxsat bersa
@bot.callback_query_handler(func=lambda call: call.data.startswith("approve_test"))
def approve_test(call):
    _, user_id, level = call.data.split("|")
    user_id = int(user_id)

    bot.answer_callback_query(call.id, "✅ Ruxsat berildi!")

    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as e:
        print("Xabarni o‘chirishda xato:", e)

    # 🔔 Bildirishlar
    bot.send_message(ADMIN_ID, f"✅ Siz {level} testi uchun ruxsat berdingiz.")
    bot.send_message(user_id, f"✅ Admin testni boshlashga ruxsat berdi!\nTest hozir boshlanadi...")

    # 🚀 Testni boshlash
    start_quiz_for_user(user_id, level)



@bot.callback_query_handler(func=lambda call: call.data.startswith("deny_test"))
def deny_test(call):
    _, user_id, level = call.data.split("|")
    user_id = int(user_id)

    bot.answer_callback_query(call.id, "❌ Test rad etildi!")

    # 🔥 Adminning so‘rov xabarini o‘chirish
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as e:
        print("Xabarni o‘chirishda xato:", e)

    # 🔔 Bildirishlar
    bot.send_message(ADMIN_ID, f"❌ Siz {level} testi uchun so‘rovni rad etdingiz.")
    bot.send_message(user_id, f"❌ Afsus, admin sizning {level} testi uchun so‘rovingizni rad etdi.")

# 🧩 Testni haqiqiy boshlovchi funksiya
def start_quiz_for_user(chat_id, level):
    shuffled = random.sample(questions[level], k=len(questions[level]))

    users_data.setdefault(chat_id, {})["quiz"] = {
        "level": level,
        "questions": shuffled,
        "index": 0,
        "answers": {},
        "score": 0,
        "scored": {}
    }

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("🛑 Testni to‘xtatish"))

    bot.send_message(chat_id, f"✅ {level} darajasi testi boshlandi!\n⏳ Sizda 30 daqiqa vaqt bor.", reply_markup=markup)

    start_quiz_timer(chat_id)
    send_question(chat_id, message_id=None)


def send_question(chat_id, message_id=None):
    user_quiz = users_data[chat_id]["quiz"]
    index = user_quiz["index"]
    q = user_quiz["questions"][index]

    chosen = user_quiz["answers"].get(index)

    text = f"❓ Savol {index+1}/{len(user_quiz['questions'])}\n\n{q['q']}"
    markup = InlineKeyboardMarkup()

    for opt in q["options"]:
        # agar foydalanuvchi shu savolda avval tanlagan bo'lsa, '✅'
        label = ("✅ " + opt) if chosen == opt[0] else opt
        markup.add(InlineKeyboardButton(label, callback_data=f"answer|{index}|{opt[0]}"))

    nav_buttons = []
    if index > 0:
        nav_buttons.append(InlineKeyboardButton("⬅️ Avvalgi", callback_data=f"nav|{index-1}"))
    if index < len(user_quiz["questions"]) - 1:
        nav_buttons.append(InlineKeyboardButton("➡️ Keyingi", callback_data=f"nav|{index+1}"))
    else:
        nav_buttons.append(InlineKeyboardButton("✅ Testni tugatish", callback_data="finish"))

    markup.row(*nav_buttons)

    if message_id:
        try:
            bot.edit_message_text(text, chat_id, message_id, reply_markup=markup)
        except telebot.apihelper.ApiTelegramException as e:
            if "message is not modified" in str(e):
                pass
            else:
                raise
    else:
        bot.send_message(chat_id, text, reply_markup=markup)

# Testni to‘xtatish handler (ReplyKeyboardButton orqali)
@bot.message_handler(func=lambda msg: msg.text == "🛑 Testni to‘xtatish")
def stop_quiz(message):
    chat_id = message.chat.id

    if "quiz" not in users_data.get(chat_id, {}):
        bot.send_message(chat_id, "❌ Sizda davom etayotgan test yo‘q.", reply_markup=main_menu())
        return

    user = users_data[chat_id]["quiz"]
    score = user["score"]
    total = len(user["questions"])

    # Natija chiqaramiz
    if score >= 15:
        result = f"🎉 Tabriklaymiz! Siz imtihondan o'tdingiz.\n\nNatija: {score}/{total}"
    else:
        result = f"❌ Afsus! Siz yiqildingiz.\n\nNatija: {score}/{total}"

    # Foydalanuvchi testini o‘chirib tashlaymiz
    del users_data[chat_id]["quiz"]

    bot.send_message(chat_id, result, reply_markup=main_menu())
    bot.delete_message(chat_id, message.message_id)


@bot.callback_query_handler(func=lambda call: call.data.startswith("answer"))
def handle_answer(call):
    chat_id = call.message.chat.id
    _, index_str, ans = call.data.split("|")
    index = int(index_str)

    user_quiz = users_data[chat_id]["quiz"]
    q = user_quiz["questions"][index]

    old_ans = user_quiz["answers"].get(index)
    old_scored = user_quiz["scored"].get(index, False)
    new_scored = (ans == q["answer"])

    if old_ans is None:
        if new_scored:
            user_quiz["score"] += 1
    else:
        if old_scored and not new_scored:
            user_quiz["score"] -= 1
        elif (not old_scored) and new_scored:
            user_quiz["score"] += 1

    # Javobni va scored flagni saqlaymiz
    user_quiz["answers"][index] = ans
    user_quiz["scored"][index] = new_scored

    send_question(chat_id, call.message.message_id)

    # user_quiz["index"] += 1
    # if user_quiz["index"] < len(user_quiz["questions"]): send_question(chat_id, None)
    # yoki oxiri bo'lsa: finish_quiz(call)
    # (hozir ushbu avtomatik o'tish komentariyada — siz xohlasangiz yoqing)


@bot.callback_query_handler(func=lambda call: call.data.startswith("nav"))
def handle_navigation(call):
    chat_id = call.message.chat.id
    _, new_index = call.data.split("|")
    users_data[chat_id]["quiz"]["index"] = int(new_index)
    send_question(chat_id, call.message.message_id)


@bot.callback_query_handler(func=lambda call: call.data == "finish")
def finish_quiz(call):
    chat_id = call.message.chat.id
    user_quiz = users_data[chat_id]["quiz"]
    score = user_quiz["score"]
    total = len(user_quiz["questions"])

    if score >= 15:
        result = f"🎉 Tabriklaymiz! Siz imtihondan o'tdingiz.\n\nNatija: {score}/{total}"
    else:
        result = f"❌ Afsus! Siz yiqildingiz.\n\nNatija: {score}/{total}"

    bot.edit_message_text(result, chat_id, call.message.message_id)

@bot.callback_query_handler(func=lambda call: call.data.startswith("nav"))
def handle_navigation(call):
    chat_id = call.message.chat.id
    _, new_index = call.data.split("|")
    new_index = int(new_index)

    users_data[chat_id]["quiz"]["index"] = new_index
    send_question(chat_id, call.message.message_id)

@bot.callback_query_handler(func=lambda call: call.data == "finish")
def finish_quiz(call):
    chat_id = call.message.chat.id
    user = users_data[chat_id]["quiz"]
    score = user["score"]
    total = len(questions[user["level"]])

    if score >= 15:
        result = f"🎉 Tabriklaymiz! Siz imtihondan o'tdingiz.\n\nNatija: {score}/{total}"
    else:
        result = f"❌ Afsus! Siz testdan yiqildingiz.\n\nNatija: {score}/{total}"

    bot.edit_message_text(result, chat_id, call.message.message_id)

bot.infinity_polling()
